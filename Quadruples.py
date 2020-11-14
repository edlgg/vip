from semantic_cube import semantic_cube
from constants import types, Type, Operator, Scope
from Operand import Operand
from MemoryManager import MemoryManager
from AddressTable import AddressTable, Dim


class Quadruples:

    def __init__(self):
        # Our stacks.
        self.quadruples = []
        self.operators = []
        self.operands = []
        self.types = []
        self.jumps = []
        self.returns = []
        self.arrays = []

        # To keep track of the next quadruple.
        self.q_count = 0
        # To keep track of params in function_call
        self.param_count = 0
        # To keep track of the next temp to be created.
        self.curr_t_count = 1
        # To keep track of the current function call.
        self.current_function_call = None
        # To keep track of type in var definition.
        self.last_var_type = None

        self.AT = AddressTable()
        self.memory_manager = MemoryManager()

        '''Array utilities'''
        # To keep track of the current array dim declaration.
        self.current_dim = None
        self.r = 1
        self.current_array_dim_number = None
        # To store the lim_inf value (not address) when defining an array dimension
        self.current_dim_lim_inf_value = None
        # To calculate the current array address
        self.current_array_address = 0

        # Generating the first quadruple which is a GOTO main.
        self.generate_quadruple(Operator.GOTO, None, None, None)

    def print_all(self):
        print("quadruples: ")
        for i, q in enumerate(self.quadruples):
            print(i, q)

        self.AT.print_all()

    def generate_quadruple(self, a, b, c, d):
        quad = [a, b, c, d]
        self.quadruples.append(quad)
        self.q_count += 1

    def add_operator(self, operator):
        self.operators.append(operator)

    def add_operand(self, str_operand, is_assigned=False, is_function_call=False):
        operand = self.build_operand_object(
            str_operand, is_assigned=is_assigned, is_function_call=is_function_call)
        self.operands.append(operand)
        self.add_type(operand.get_type())

    def pop_fake_bottom(self):
        self.operators.pop()

    def add_existing_operand(self, operand):
        self.add_type(operand.get_type())
        self.operands.append(operand)

    def build_operand_object(self, str_operand, is_assigned=False, is_function_call=False):
        t = type(str_operand)
        operand = Operand(str_operand, is_assigned=is_assigned, is_function_call=is_function_call)
        func = self.AT.funcs[self.AT.current_func_name]

        if t == int:
            operand.set_type(Type.INT)
            address = self.AT.get_constant_address(str_operand, Type.INT)
            if address == -1:  # It doesn't exist.
                address = self.memory_manager.setConstantAddress(Type.INT)
                self.AT.add_constant_address(str_operand, Type.INT, address)
            operand.set_address(address)
        elif t == float:
            operand.set_type(Type.FLOAT)
            address = self.AT.get_constant_address(str_operand, Type.FLOAT)
            if address == -1:  # It doesn't exist.
                address = self.memory_manager.setConstantAddress(Type.FLOAT)
                self.AT.add_constant_address(str_operand, Type.FLOAT, address)
            operand.set_address(address)
        elif t == str:
            operand.set_type(Type.STRING)
            # if constant
            if str_operand[0] == "\"" and str_operand[-1] == "\"":
                address = self.AT.get_constant_address(
                    str_operand, Type.STRING)
                if address == -1:  # It doesn't exist.
                    address = self.memory_manager.setConstantAddress(
                        Type.STRING)
                    self.AT.add_constant_address(
                        str_operand, Type.STRING, address)
                operand.set_address(address)

            else:  # Variable
                address = None
                for _, value in func.vars.items():
                    if value.name == str_operand:
                        address = value.address
                        operand = value
                if address == None:
                    address = self.memory_manager.setAddress(
                        Scope.LOCAL, Type.STRING)
                operand.set_address(address)
                operand_type = self.get_type_from_address(address)
                operand.set_type(operand_type)

        return operand

    def get_type_from_address(self, address):
        address -= 1000
        address = address % 3000
        if address < 1000:
            return Type.INT
        elif address < 2000:
            return Type.FLOAT
        else:
            return Type.STRING

    def add_type(self, _type):
        self.types.append(_type)

    def add_jump(self, jump):
        self.jumps.append(jump)

    def get_operator(self):
        if len(self.operators):
            return self.operators[-1]
        return None

    def register_condition(self):
        self.types.pop()
        expression_result = self.operands.pop()
        self.generate_quadruple(
            Operator.GOTOF, expression_result.get_address(), None, None)
        self.jumps.append(self.q_count - 1)

    def register_else(self):
        self.generate_quadruple(Operator.GOTO, None, None, None)
        false = self.jumps.pop()
        self.jumps.append(self.q_count - 1)
        self.quadruples[false][3] = self.q_count

    def register_end_if(self):
        end = self.jumps.pop()
        self.quadruples[end][3] = self.q_count

    def register_start_while(self):
        self.jumps.append(self.q_count)

    def register_end_while(self):
        end = self.jumps.pop()
        self.quadruples[end][3] = self.q_count + 1
        start_while = self.jumps.pop()
        self.generate_quadruple(Operator.GOTO, None, None, start_while)

    def init_assignment(self, var_name, is_array=False):
        func = self.AT.funcs[self.AT.current_func_name]
        operand = None
        # Validate var exists
        if func.is_var(var_name):
            operand = func.get_var(var_name)
        else:
            raise NameError('Variable not declared')
        # Array validation
        if is_array:
            self.current_array_call = operand
            if not operand.is_array:
                raise NameError(f'Variable {operand.name} is not an array')

        self.add_existing_operand(operand)

    def assign(self):
        l_operand = self.operands.pop()
        l_type = self.types.pop()
        assigning_variable = self.operands.pop()
        assigning_type = self.types.pop()


        # Semantic cube checking.
        if not semantic_cube[assigning_type][l_type][Operator.ASSIGN].value:
            raise NameError('Type mismatch')
        self.generate_quadruple(
            Operator.ASSIGN, l_operand.get_address(), None, assigning_variable.get_address())
        self.operands.append(assigning_variable)
        self.types.append(assigning_type)

    def do_print(self, string=None):
        operand = self.operands.pop()
        self.types.pop()
        self.generate_quadruple(Operator.PRINT, None,
                                None, operand.get_address())

    def add_return(self):
        func = self.AT.get_func(self.AT.current_func_name)
        func_return_type = func.get_return_type()
        if func_return_type == Type.VOID:
            raise NameError(f'Void function should not return a value')
        return_val = self.operands.pop()
        return_type = self.types.pop()
        if not semantic_cube[func_return_type][return_type][Operator.ASSIGN].value:
            raise NameError(f'\'{return_type}\' cannot be returned as \'{func_return_type}\'')
        self.returns.append(self.q_count)
        self.generate_quadruple(
            Operator.RETURN, return_val.get_address(), None, None)

    def end_function(self, is_main=False):
        while len(self.returns):
            self.quadruples[self.returns.pop()][3] = self.q_count

        if is_main:
            self.generate_quadruple(Operator.END, None, None, None)
        else:
            self.generate_quadruple(Operator.ENDFUNC, None, None, None)
        self.memory_manager.reset_temp_and_local_vars()

    def start_main(self):
        self.quadruples[0][3] = self.q_count
        self.AT.add_func('main')

    def register_func(self, func_name):
        self.AT.add_func(func_name, first_quadruple=self.q_count)

    def register_func_type(self, func_type):
        func = self.AT.get_func(self.AT.current_func_name)
        func_type = types[func_type]
        func.assign_return_type(func_type)
        func_address = self.memory_manager.setAddress(Scope.GLOBAL, func_type)
        self.AT.add_global_address(self.AT.current_func_name, func_type, func_address)

    def maybe_solve_operation(self, operations):
        operator = self.get_operator()

        if operator in operations:
            r_operand = self.operands.pop()
            r_type = self.types.pop()
            l_operand = self.operands.pop()
            l_type = self.types.pop()
            operator = self.operators.pop()
            result_type = semantic_cube[l_type][r_type][operator]

            if result_type == Type.ERROR:
                raise NameError(f"Type mismatch {l_type} {operator} {r_type}")

            # TODO:Borrar esto del constructor despues
            temp = Operand('t' + str(self.curr_t_count))
            temp.set_type(result_type)
            address = self.memory_manager.setTempAddress(result_type)
            temp.set_address(address)
            current_func_name = self.AT.current_func_name
            current_func = self.AT.get_func(current_func_name)
            current_func.num_temp_vars += 1
            self.curr_t_count += 1

            self.operands.append(temp)
            self.types.append(result_type)

            # Development note: Beware, operands are objects now. Everything is perfectly fine... maybe.
            self.generate_quadruple(
                operator, l_operand.get_address(), r_operand.get_address(), address)

    def calling_func(self, func_id):
        if self.AT.is_func(func_id):
            self.current_function_call = func_id
        else:
            raise NameError(f"Calling undefined function: {func_id}")
        
        func = self.AT.funcs[func_id]
        global_func_address = self.AT.get_global_address(func_id, func.get_return_type())
        self.generate_quadruple(Operator.ERA, global_func_address,
                                func.num_params, func.num_temp_vars)
        self.param_count = 0
        self.operators.append(Operator.FAKE_BOTTOM)

    def validate_param(self, param):
        argument = self.operands.pop()
        self.types.pop()

        if self.param_count < self.AT.funcs[self.current_function_call].num_params:
            address_in_func = None
            func = self.AT.get_func(self.current_function_call)
            param_name = func.param_names[self.param_count]
            var = func.get_var(param_name)
            address_in_func = var.get_address()
            self.generate_quadruple(
                Operator.PARAM, argument.get_address(), None, address_in_func)
            self.param_count += 1
        else:
            raise NameError(f"Passing more arguments than expected.")

    def validate_function_call(self):
        if self.param_count != self.AT.funcs[self.current_function_call].num_params:
            raise NameError(
                f"Wrong number of parameters passed. Expected {self.AT.funcs[self.current_function_call].num_params}. {self.param_count} were given.")
        else:
            self.generate_quadruple(Operator.GOSUB, self.current_function_call,
                                    None, self.AT.funcs[self.current_function_call].first_quadruple)
        
        func = self.AT.get_func(self.current_function_call)

        func_return_type = func.get_return_type()
        if func_return_type is not Type.VOID:
            tmp_address = self.memory_manager.setTempAddress(func_return_type)
            temp = Operand(address=tmp_address)
            func_address = self.AT.get_global_address(self.current_function_call, func_return_type)
            self.generate_quadruple(Operator.ASSIGN, func_address, None, tmp_address)
            self.operands.append(temp)
            self.types.append(func_return_type)
        self.operators.pop()

    def increment_local_var_count(self):
        curr_func = self.AT.current_func_name
        self.AT.funcs[curr_func].num_local_vars += 1

    def add_var(self, var_name, is_param=False, is_array=False):
        func = self.AT.get_func(self.AT.current_func_name)

        operand = Operand(
            str_operand=var_name, op_type=types[self.last_var_type], is_array=is_array)
        func.add_var(operand)
        func.current_var_name = var_name
        if is_param:
            func.num_params += 1
            func.param_names.append(var_name)
        if is_array:
            self.r = 1
        else:
            # Address is only set for non-arrays for now. Address for arrays should be set after knowing the total needed memory space for the array.
            var_address = self.memory_manager.setAddress(
                scope=Scope.LOCAL, var_type=types[self.last_var_type])
            func.get_var(var_name).set_address(var_address)

    def create_dim_node(self):
        dim = Dim()
        self.current_dim = dim

    def end_array_dim(self):
        var_address = self.memory_manager.setAddress(
            scope=Scope.LOCAL, var_type=types[self.last_var_type], space_required=self.r)
        func = self.AT.get_func(self.AT.current_func_name)
        var_name = func.current_var_name
        var = func.get_var(var_name)
        var.set_address(var_address)
        var.solve_dims(self.r)

    def register_array_dim_lim_inf(self, lim_inf=0):
        # Register new constant if it hasn't been registered before
        address = self.AT.get_constant_address(lim_inf, Type.INT)
        if address == -1:  # It doesn't exist.
            address = self.memory_manager.setConstantAddress(Type.INT)
            self.AT.add_constant_address(lim_inf, Type.INT, address)
        self.current_dim.set_lim_inf(lim_inf)
        self.current_dim_lim_inf_value = lim_inf

    def register_array_dim_lim_sup(self, lim_sup):
        if self.current_dim_lim_inf_value > lim_sup:
            raise NameError(f'Invalid array dimension interval')
        # Register new constant if it hasn't been registered before
        address = self.AT.get_constant_address(lim_sup, Type.INT)
        if address == -1:  # It doesn't exist.
            address = self.memory_manager.setConstantAddress(Type.INT)
            self.AT.add_constant_address(lim_sup, Type.INT, address)
        self.current_dim.set_lim_sup(lim_sup)
        func = self.AT.get_func(self.AT.current_func_name)
        var_name = func.current_var_name
        func.get_var(var_name).add_dim(self.current_dim)

        # Update r
        self.r *= (self.current_dim.get_lim_sup() -
                   self.current_dim.get_lim_inf() + 1)
        self.current_dim = None

    def ver_index(self):
        var, dim_num = self.arrays.pop()
        if dim_num == 0:
            self.current_array_address = 0
            self.current_array_dim_number = var.get_dim_count()
        if self.current_dim == self.current_array_dim_number:
            raise NameError(f'Trying to access a non-existent dimension')
        s = self.operands.pop().get_address()
        self.types.pop()
        dim = var.get_dim(dim_num)
        lim_inf = self.AT.get_constant_address(dim.get_lim_inf(), Type.INT)
        lim_sup = self.AT.get_constant_address(dim.get_lim_sup(), Type.INT)
        self.generate_quadruple(Operator.VER, s, lim_inf, lim_sup)

        # Following the formula s1*m1 + s2 + (-k)....
        tmp_address = self.memory_manager.setTempAddress(Type.INT)
        t = Operand(address=tmp_address, op_type=Type.INT)
        m = dim.get_m()
        m = self.AT.get_constant_address(m, Type.INT)
        # If it doesn't exist, create a new constant address for it.
        if m == -1:
            m = self.memory_manager.setConstantAddress(Type.INT)
            self.AT.add_constant_address(dim.get_m(), Type.INT, m)
        # Multiply m of the current Dim node if it's not the last dim
        if dim_num < self.current_array_dim_number - 1:
            self.generate_quadruple(Operator.TIMES, s, m, tmp_address)
        # Add (-k) if it's the last Dim node
        else:
            k = m
            self.generate_quadruple(Operator.PLUS, s, k, tmp_address)
        if dim_num != 0:
            aux = self.operands.pop()
            self.types.pop()
            tmp_address_2 = self.memory_manager.setTempAddress(Type.INT)
            self.generate_quadruple(
                Operator.PLUS, aux.get_address(), tmp_address, tmp_address_2)
            t.set_address(tmp_address_2)
        self.operands.append(t)
        self.types.append(Type.INT)
        self.arrays.append((var, dim_num + 1))

    def get_array_dir(self):
        operand = self.operands.pop()
        var, _ = self.arrays.pop()
        self.types.pop()
        tmp_address = self.memory_manager.setTempAddress(Type.INT) * -1
        t = Operand(address=tmp_address)
        # Add base address
        base_address = var.get_address()
        const_address = self.AT.get_constant_address(base_address, Type.INT)
        if const_address == -1:  # It doesn't exist.
            const_address = self.memory_manager.setConstantAddress(Type.INT)
            self.AT.add_constant_address(base_address, Type.INT, const_address)
        self.generate_quadruple(
            Operator.PLUS, operand.get_address(), const_address, tmp_address * -1)
        self.operands.append(t)
        self.types.append(Type.INT)

    def validate_is_array(self):
        array_id = self.operands.pop().get_name()
        self.types.pop()
        var = None
        func = self.AT.get_func(self.AT.current_func_name)
        if func.is_var(array_id):
            var = func.get_var(array_id)
        if var == None:
            raise NameError(f'Variable {array_id} does not exist')
        if not var.is_array:
            raise NameError(f'Variable {array_id} is not an array')
        self.arrays.append((var, 0))
        self.operators.append(Operator.FAKE_BOTTOM)

    def register_read(self, var_name):
        func = self.AT.get_func(self.AT.current_func_name)
        if func.is_var(var_name):
            operand = func.get_var(var_name)
            self.generate_quadruple(
                Operator.READ, None, None, operand.get_address())
        else:
            raise NameError(f"Undefined variable.")

    def generate_obj_code(self):
        constants = {}
        for value in self.AT.constants_addresses.values():
            constants.update(self.invert_constants(value))

        return self.quadruples, constants

    def invert_constants(self, dict):
        return {value: key for key, value in dict.items()}
