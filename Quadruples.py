from semantic_cube import semantic_cube
from constants import types, Type, Operator, Scope
from Operand import Operand
from MemoryManager import MemoryManager
from AddressTable import AddressTable, Dim, Var


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
        # To keep track of global variable declaration
        self.is_global = False

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

    def set_is_global(self, is_global):
        self.is_global = is_global

    def add_operator(self, operator):
        self.operators.append(operator)

    def add_operand(self, name, is_function_call=False):
        operand = self.build_operand_object(
            name, is_function_call=is_function_call)
        self.operands.append(operand)
        self.add_type(operand.get_type())

    def pop_fake_bottom(self):
        self.operators.pop()

    def add_existing_operand(self, operand):
        self.add_type(operand.get_type())
        # Instead of using the add_operand method we directly append the operand to the stack
        self.operands.append(operand)

    def build_operand_object(self, name, is_function_call=False):
        t = type(name)
        operand = Operand(name,
                          is_function_call=is_function_call)

        if t == int:
            operand.set_type(Type.INT)
            address = self.AT.get_constant_address(name, Type.INT)
            if address == -1:  # It doesn't exist.
                address = self.memory_manager.set_constant_address(Type.INT)
                self.AT.add_constant_address(name, Type.INT, address)
            operand.set_address(address)
        elif t == float:
            operand.set_type(Type.FLOAT)
            address = self.AT.get_constant_address(name, Type.FLOAT)
            if address == -1:  # It doesn't exist.
                address = self.memory_manager.set_constant_address(Type.FLOAT)
                self.AT.add_constant_address(name, Type.FLOAT, address)
            operand.set_address(address)
        elif t == str:
            # if constant
            if name[0] == "\"" and name[-1] == "\"":
                operand.set_type(Type.STRING)
                address = self.AT.get_constant_address(
                    name, Type.STRING)
                if address == -1:  # It doesn't exist.
                    address = self.memory_manager.set_constant_address(
                        Type.STRING)
                    self.AT.add_constant_address(
                        name, Type.STRING, address)
                operand.set_address(address)

            else:  # Variable
                var = self.find_var_in_address_table(name)
                if var == -1:
                    raise NameError(f'Undeclared variable {name}')
                operand.set_address(var.get_address())
                operand_type = self.get_type_from_address(var.get_address())
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

    def get_top_operator(self):
        if len(self.operators):
            return self.operators[-1]
        return None

    def register_condition(self):
        expression_result = self.operands.pop()
        self.types.pop()
        self.generate_quadruple(
            Operator.GOTOF, expression_result.get_address(), None, None)
        self.add_jump(self.q_count - 1)

    def register_else(self):
        self.generate_quadruple(Operator.GOTO, None, None, None)
        false = self.jumps.pop()
        self.add_jump(self.q_count - 1)
        self.fill_jump(false, self.q_count)

    def register_end_if(self):
        end = self.jumps.pop()
        self.fill_jump(end, self.q_count)

    def fill_jump(self, quad_index, jump):
        self.quadruples[quad_index][3] = jump

    def register_start_while(self):
        self.add_jump(self.q_count)

    def register_end_while(self):
        end = self.jumps.pop()
        self.fill_jump(end, self.q_count + 1)
        start_while = self.jumps.pop()
        self.generate_quadruple(Operator.GOTO, None, None, start_while)

    def get_current_func(self):
        if self.AT.current_func_name:
            return self.AT.funcs[self.AT.current_func_name]
        else:
            return None

    def init_assignment(self, var_name, is_array=False):
        # Validate var exists
        var = self.find_var_in_address_table(var_name)
        if var == -1:
            raise NameError('Variable not declared')
        # Array validation
        if is_array:
            self.current_array_call = var
            if not var.is_array:
                raise NameError(f'Variable {var.name} is not an array')

        self.add_existing_operand(var)

    def register_sign(self, sign):
        operator = None
        if sign == '+':
            operator = Operator.POSITIVE_SIGN
        elif sign == '-':
            operator = Operator.NEGATIVE_SIGN
        else:
            operator = Operator.NOT
        self.operators.append(operator)

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

    def do_print(self):
        operand = self.operands.pop()
        self.types.pop()
        self.generate_quadruple(Operator.PRINT, None,
                                None, operand.get_address())

    def end_print(self):
        self.generate_quadruple(Operator.PRINT, None, None, None)

    def add_return(self):
        func = self.get_current_func()
        func_return_type = func.get_return_type()
        if func_return_type == Type.VOID:
            raise NameError(f'Void function should not return a value')
        return_val = self.operands.pop()
        return_type = self.types.pop()
        if not semantic_cube[func_return_type][return_type][Operator.ASSIGN].value:
            raise NameError(
                f'\'{return_type}\' cannot be returned as \'{func_return_type}\'')
        self.returns.append(self.q_count)
        func_global_address = self.AT.get_global_var(
            self.AT.current_func_name).get_address()
        self.generate_quadruple(
            Operator.RETURN, return_val.get_address(), func_global_address, None)

    def end_function(self, is_main=False):
        func = self.get_current_func()
        if func.get_return_type() != Type.VOID:
            if len(self.returns) == 0:
                raise NameError(
                    f'{func.get_return_type()} function {func.get_name()} has no return. Expected at least 1.')
        while len(self.returns):
            self.fill_jump(self.returns.pop(), self.q_count)

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

        if func_type is not Type.VOID:
            func_address = self.memory_manager.set_address(
                Scope.GLOBAL, func_type)
            var = Var(self.AT.current_func_name,
                      func_type, address=func_address)
            self.AT.add_global_address(var)

    def maybe_solve_sign(self):
        operator = self.get_top_operator()

        if operator in (Operator.POSITIVE_SIGN, Operator.NEGATIVE_SIGN, Operator.NOT):
            operand = self.operands.pop()
            operand_type = self.types.pop()
            operator = self.operators.pop()
            result_type = semantic_cube[operand_type][operator]
            if result_type == Type.ERROR:
                raise NameError(f'Type mismatch {operand_type} {operator}')
            temp = Operand(op_type=result_type)
            address = self.memory_manager.set_temp_address(result_type)
            temp.set_address(address)
            self.curr_t_count += 1
            self.generate_quadruple(
                operator, operand.get_address(), None, temp.get_address())

            self.operands.append(temp)
            self.types.append(result_type)

    def maybe_solve_operation(self, operations):
        operator = self.get_top_operator()

        if operator in operations:
            r_operand = self.operands.pop()
            r_type = self.types.pop()
            l_operand = self.operands.pop()
            l_type = self.types.pop()
            operator = self.operators.pop()

            result_type = semantic_cube[l_type][r_type][operator]

            if result_type == Type.ERROR:
                raise NameError(f"Type mismatch {l_type} {operator} {r_type}")

            temp = Operand()
            temp.set_type(result_type)
            address = self.memory_manager.set_temp_address(result_type)
            temp.set_address(address)
            self.curr_t_count += 1

            self.operands.append(temp)
            self.types.append(result_type)

            self.generate_quadruple(
                operator, l_operand.get_address(), r_operand.get_address(), address)

    def calling_func(self, func_id):
        if self.AT.is_func(func_id):
            self.current_function_call = func_id
        else:
            raise NameError(f"Calling undefined function: {func_id}")

        self.generate_quadruple(Operator.ERA, None, None, None)
        self.param_count = 0
        self.operators.append(Operator.FAKE_BOTTOM)

    def validate_param(self, param):
        argument = self.operands.pop()
        self.types.pop()

        if self.param_count < self.AT.funcs[self.current_function_call].num_params:
            func = self.AT.get_func(self.current_function_call)
            param_name = func.param_names[self.param_count]
            var = self.find_var_in_address_table(
                param_name, of_function=self.current_function_call)
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
            tmp_address = self.memory_manager.set_temp_address(
                func_return_type)
            temp = Operand(address=tmp_address)
            func_address = self.AT.get_global_var(
                self.current_function_call).get_address()
            self.generate_quadruple(
                Operator.ASSIGN, func_address, None, tmp_address)
            self.operands.append(temp)
            self.types.append(func_return_type)
        self.operators.pop()

    def find_var_in_address_table(self, name, of_function=None):
        func = self.get_current_func()
        if of_function is not None:
            func = self.AT.get_func(of_function)
        var = -1
        if func:
            var = func.get_var(name)
        if var == -1:
            var = self.AT.get_global_var(name)
        return var

    def add_var(self, var_name, is_param=False, is_array=False):
        func = None
        operand = Operand(
            name=var_name, op_type=types[self.last_var_type], is_array=is_array)
        if self.is_global:
            self.AT.add_global_address(operand)
        else:
            func = self.get_current_func()
            func.add_var(operand)
        if is_param:
            func.num_params += 1
            func.param_names.append(var_name)
        if is_array:
            func.current_var_name = var_name
            self.r = 1
        else:
            # Address is only set for non-arrays for now. Address for arrays should be set after knowing the total needed memory space for the array.
            scope = Scope.GLOBAL if self.is_global else Scope.LOCAL
            var_address = self.memory_manager.set_address(
                scope=scope, var_type=types[self.last_var_type])
            var = self.find_var_in_address_table(var_name)
            var.set_address(var_address)

    def create_dim_node(self):
        dim = Dim()
        self.current_dim = dim

    def end_array_dim(self):
        scope = Scope.GLOBAL if self.is_global else Scope.LOCAL
        var_address = self.memory_manager.set_address(
            scope=scope, var_type=types[self.last_var_type], space_required=self.r)
        func = self.get_current_func()
        var_name = func.current_var_name
        var = self.find_var_in_address_table(var_name)
        var.set_address(var_address)
        var.solve_dims(self.r)

    def register_array_dim_lim_inf(self, lim_inf=0):
        # Register new constant if it hasn't been registered before
        address = self.AT.get_constant_address(lim_inf, Type.INT)
        if address == -1:  # It doesn't exist.
            address = self.memory_manager.set_constant_address(Type.INT)
            self.AT.add_constant_address(lim_inf, Type.INT, address)
        self.current_dim.set_lim_inf(lim_inf)
        self.current_dim_lim_inf_value = lim_inf

    def register_array_dim_lim_sup(self, lim_sup):
        if self.current_dim_lim_inf_value > lim_sup:
            raise NameError(f'Invalid array dimension interval')
        # Register new constant if it hasn't been registered before
        address = self.AT.get_constant_address(lim_sup, Type.INT)
        if address == -1:  # It doesn't exist.
            address = self.memory_manager.set_constant_address(Type.INT)
            self.AT.add_constant_address(lim_sup, Type.INT, address)
        self.current_dim.set_lim_sup(lim_sup)
        func = self.get_current_func()
        var_name = func.current_var_name
        var = self.find_var_in_address_table(var_name)
        var.add_dim(self.current_dim)

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
        s_address = self.operands.pop().get_address()
        self.types.pop()
        dim = var.get_dim(dim_num)
        lim_inf = self.AT.get_constant_address(dim.get_lim_inf(), Type.INT)
        lim_sup = self.AT.get_constant_address(dim.get_lim_sup(), Type.INT)
        self.generate_quadruple(Operator.VER, s_address, lim_inf, lim_sup)

        # Following the formula s1*m1 + s2 + (-k)....
        tmp_address = self.memory_manager.set_temp_address(Type.INT)
        t = Operand(address=tmp_address, op_type=Type.INT)
        m = dim.get_m()
        m_address = self.AT.get_constant_address(m, Type.INT)
        # If it doesn't exist, create a new constant address for it.
        if m_address == -1:
            m_address = self.memory_manager.set_constant_address(Type.INT)
            self.AT.add_constant_address(m, Type.INT, m_address)
        # Multiply m of the current Dim node if it's not the last dim
        if dim_num < self.current_array_dim_number - 1:
            self.generate_quadruple(
                Operator.TIMES, s_address, m_address, tmp_address)
        # Add (-k) if it's the last Dim node
        else:
            k_address = m_address
            self.generate_quadruple(
                Operator.PLUS, s_address, k_address, tmp_address)
        if dim_num != 0:
            aux = self.operands.pop()
            self.types.pop()
            tmp_address_2 = self.memory_manager.set_temp_address(Type.INT)
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
        # To make things easy, our tp are normal temporary address but with negative address value
        tmp_address = self.memory_manager.set_temp_address(Type.INT) * -1
        t = Operand(address=tmp_address)
        # Add base address
        base_address = var.get_address()
        const_address = self.AT.get_constant_address(base_address, Type.INT)
        if const_address == -1:  # It doesn't exist.
            const_address = self.memory_manager.set_constant_address(Type.INT)
            self.AT.add_constant_address(base_address, Type.INT, const_address)
        self.generate_quadruple(
            Operator.PLUS, operand.get_address(), const_address, tmp_address * -1)
        self.operands.append(t)
        self.types.append(Type.INT)

    def validate_is_array(self):
        array_id = self.operands.pop().get_name()
        self.types.pop()
        var = self.find_var_in_address_table(array_id)
        if var == -1:
            raise NameError(f'Variable {array_id} does not exist')
        if not var.is_array:
            raise NameError(f'Variable {array_id} is not an array')
        self.arrays.append((var, 0))
        self.operators.append(Operator.FAKE_BOTTOM)

    def register_read(self, var_name):
        var = self.find_var_in_address_table(var_name)
        if var == -1:
            raise NameError(f"Undefined variable.")
        else:
            self.generate_quadruple(
                Operator.READ, None, var.get_type(), var.get_address())

    def generate_obj_code(self):
        constants = {}
        for value in self.AT.constants_addresses.values():
            constants.update(self.invert_constants(value))

        return self.quadruples, constants

    def invert_constants(self, dict):
        return {value: key for key, value in dict.items()}
