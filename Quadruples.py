from semantic_cube import semantic_cube
from constants import types, Type, Operator
from Operand import Operand
from MemoryManager import MemoryManager
from AddressTable import AddressTable


class Quadruples:

    def __init__(self):
        # Our stacks.
        self.quadruples = []
        self.operators = []
        self.operands = []
        self.types = []
        self.jumps = []
        self.returns = []

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

        # Generating the first quadruple which is a GOTO main.
        self.generate_quadruple(Operator.GOTO, None, None, None)

    def get_AT(self):
        return self.AT

    def print_all(self):
        print("quadruples: ")
        for i, q in enumerate(self.quadruples):
            print(i, q)

    def generate_quadruple(self, a, b, c, d):
        quad = [a, b, c, d]
        self.quadruples.append(quad)
        self.q_count += 1

    def add_operator(self, operator):
        self.operators.append(operator)

    def add_operand(self, str_operand, is_assigned=False):
        operand = self.build_operand_object(
            str_operand, is_assigned=is_assigned)
        self.operands.append(operand)
        self.add_type(operand.get_type())

    def pop_fake_bottom(self):
        self.operators.pop()

    def add_existing_operand(self, operand):
        self.add_type(operand.get_type())
        self.operands.append(operand)

    def build_operand_object(self, str_operand, is_assigned=False):
        t = type(str_operand)
        operand = Operand(str_operand, is_assigned=is_assigned)
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
                address = self.AT.get_constant_address(str_operand, Type.STRING)
                if address == -1:  # It doesn't exist.
                    address = self.memory_manager.setConstantAddress(
                        Type.STRING)
                    self.AT.add_constant_address(
                        str_operand, Type.STRING, address)
                operand.set_address(address)

            else:  # Variable
                address = None
                for key, value in func.vars.items():
                    if value.str_operand == str_operand:
                        address = value.address
                if address == None:
                    address = self.memory_manager.setAddress(
                        'local', Type.STRING)
                operand.set_address(address)

        return operand

    def add_type(self, _type):
        self.types.append(_type)

    def add_jump(self, jump):
        self.jumps.append(jump)

    def get_operator(self):
        if len(self.operators):
            return self.operators[-1]
        return None

    def get_operand(self):
        if len(self.operands):
            return self.operands[-1]
        return None

    def get_jump(self):
        if len(self.jumps):
            return self.jumps[-1]
        return None

    def get_q_count(self):
        return self.q_count

    def pop_operator(self):
        val = self.operators[-1]
        self.operators = self.operators[:-1]
        return val

    def pop_operand(self):
        val = self.operands[-1]
        self.operand = self.operand[:-1]
        return val

    def pop_jump(self):
        val = self.jumps[-1]
        self.jumps = self.jumps[:-1]
        return val

    # def solve_operation(self, l_operand, r_operand, operator):
    #     operator =
    #     res = eval(
    #         f"{l_operand.get_str_operand()} {operator} {r_operand.get_str_operand()}")
    #     if type(res) == bool:
    #         res = 1 if res else 0
    #     return res

    def register_condition(self):
        self.types.pop()
        # expression_type = self.types.pop()
        # print(expression_type)
        # if expression_type == Type.ERROR:
        #     return 'Type mismatch.'
        expression_result = self.operands.pop()
        self.generate_quadruple(Operator.GOTOF, expression_result, None, None)
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

    def init_assignment(self, var_name):
        func = self.AT.funcs[self.AT.current_func_name]
        operand = None
        if func.is_var(var_name):
            operand = func.get_var(var_name)
        else:
            raise NameError(f"Variable not declared.")
        self.add_existing_operand(operand)

    def assign(self):
        l_operand = self.operands.pop()
        l_type = self.types.pop()
        assigning_variable = self.operands.pop()
        assigning_type = self.types.pop()

        # Semantic cube checking.
        if not semantic_cube[assigning_type][l_type][Operator.ASSIGN]:
            return f'Type mismatch'
        self.generate_quadruple(
            Operator.ASSIGN, l_operand.address, None, assigning_variable.address)
        self.operands.append(assigning_variable)
        self.types.append(assigning_type)

    def do_print(self, string=None):
        operand = self.operands.pop()
        operand_type = self.types.pop()
        self.generate_quadruple(Operator.PRINT, None, None, operand)

    def add_return(self):
        return_val = self.operands.pop()
        return_type = self.types.pop()
        self.returns.append(self.q_count)
        self.generate_quadruple(Operator.RETURN, return_val, None, None)

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
        func.assign_return_type(func_type)

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
            # temp.set_str_operand(temp.get_address())
            self.curr_t_count += 1

            # result = self.solve_operation(l_operand, r_operand, operator)
            # self.add_operand(temp)
            self.operands.append(temp)
            self.types.append(result_type)
            # self.add_type(result_type)

            # Development note: Beware, operands are objects now. Everything is perfectly fine... maybe.
            self.generate_quadruple(
                operator, l_operand.address, r_operand.address, address)

    def calling_func(self, func_id):
        if self.AT.is_func(func_id):
            self.current_function_call = func_id
        else:
            raise NameError(f"Calling undefined function: {func_id}")

        func = self.AT.funcs[func_id]
        self.generate_quadruple(Operator.ERA, func_id, func.num_params, func.num_temp_vars)
        self.param_count = 0

    def validate_param(self, param):
        argument = self.operands.pop()
        argument_type = self.types.pop()

        if self.param_count < self.AT.funcs[self.current_function_call].num_params:
            self.param_count += 1
            self.generate_quadruple(Operator.PARAM, argument.get_address(), None, "param" + str(self.param_count))
        else:
            raise NameError(f"Passing more arguments than expected.")


    def validate_function_call(self):
        if self.param_count != self.AT.funcs[self.current_function_call].num_params:
            raise NameError(f"Wrong number of parameters passed. Expected {self.AT.funcs[self.current_function_call].num_params}. {self.param_count} were given.")
        else:
            self.generate_quadruple(Operator.GOSUB, self.current_function_call, None, self.AT.funcs[self.current_function_call].first_quadruple)

    def increment_local_var_count(self):
        curr_func = self.AT.current_func_name
        self.AT.funcs[curr_func].num_local_vars += 1

    def add_var(self, var_name, is_param=False):
        func = self.AT.get_func(self.AT.current_func_name)
        var_address = self.memory_manager.setAddress(
            scope='local', var_type=types[self.last_var_type])
        operand = Operand(
            str_operand=var_name, op_type=types[self.last_var_type], address=var_address)
        func.add_var(operand)
        if is_param:
            func.num_params += 1
