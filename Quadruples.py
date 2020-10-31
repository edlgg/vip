from semantic_cube import semantic_cube
from constants import types, Type, Operator
from Operand import Operand
from MemoryManager import MemoryManager


class Quadruples:

    def __init__(self):
        self.quadruples = []
        self.operators = []
        self.operands = []
        self.types = []
        self.jumps = []
        self.returns = []
        self.q_count = 1
        self.curr_t_count = 1

        self.memory_manager = MemoryManager()

    def get_memory_manager(self):
        return self.memory_manager

    def print_all(self):
        # print("operators: ", self.operators)
        print("quadruples: ")
        for i, q in enumerate(self.quadruples):
            print(i+1, q)
        # print('operands: ')
        # for operand in self.operands:
        #     print(operand.get_str_operand())
        # print('pila de saltos', self.jumps)

    def generate_quadruple(self, a, b, c, d):
        quad = [a, b, c, d]
        self.quadruples.append(quad)
        self.q_count += 1

    def add_operator(self, operator):
        self.operators.append(operator)

    def add_operand(self, str_operand):
        operand = self.build_operand_object(str_operand)
        self.operands.append(operand)

    def build_operand_object(self, str_operand):
        t = type(str_operand)
        print('type de t: ', t)
        operand = Operand(str_operand)

        if t == int:
            operand.set_type(Type.INT)
            operand.set_address(self.memory_manager.setAddress('local', Type.INT)) #TODO: Manage local and global.
        elif t == float:
            operand.set_type(Type.FLOAT)
            operand.set_address(self.memory_manager.setAddress('local', Type.FLOAT))
        elif t == str:
            operand.set_type(Type.STRING)
            operand.set_address(self.memory_manager.setAddress('local', Type.STRING))

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
        self.quadruples[false - 1][3] = self.q_count

    def register_end_if(self):
        end = self.jumps.pop()
        self.quadruples[end - 1][3]  = self.q_count

    def register_start_while(self):
        self.jumps.append(self.q_count)

    def register_end_while(self):
        end = self.jumps.pop()
        self.quadruples[end-1][3] = self.q_count + 1
        start_while = self.jumps.pop()
        self.generate_quadruple(Operator.GOTO, None, None, start_while)

    def assign(self):

        print('antes de los pops')
        print('Operands', self.operands)
        print('Types', self.types)

        l_operand = self.operands.pop()
        l_type = self.types.pop()
        assigning_variable = self.operands.pop()
        assigning_type = self.types.pop()

        print('variable: ', assigning_variable)
        print('assigning_type: ', assigning_type)


        # Semantic cube checking.
        if not semantic_cube[assigning_type][l_type][Operator.ASSIGN]:
            return f'Type mismatch'
        self.generate_quadruple(Operator.ASSIGN, l_operand, None, assigning_variable.address)
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

            print(operator)
            print(l_type, r_type)
            print(result_type)

            temp = Operand('t' + str(self.curr_t_count)) # TODO:Borrar esto del constructor despues
            temp.set_type(result_type)
            temp.set_address(self.memory_manager.setTempAddress(result_type))
            temp.set_str_operand(temp.get_address())
            self.curr_t_count += 1

            # result = self.solve_operation(l_operand, r_operand, operator)
            self.add_operand(temp)
            self.add_type(result_type)

            # Development note: Beware, operands are objects now. Everything is perfectly fine... maybe.
            self.generate_quadruple(operator, l_operand, r_operand, temp)
