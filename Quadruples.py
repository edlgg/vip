from semantic_cube import semantic_cube
from constants import types, Type, Operator
from Operand import Operand


class Quadruples:

    def __init__(self):
        self.quadruples = []
        self.operators = []
        self.operands = []
        self.types = []
        self.jumps = []
        self.q_count = 1

    def print_all(self):
        print("operators: ", self.operators)
        for operand in self.operands:
            print("operand: ", operand.get_str_operand())

    def add_quadruple(self, quadruple):
        self.quadruples.append(quadruple)

    def add_operator(self, operator):
        self.operators.append(operator)

    def add_operand(self, str_operand):
        operand = self.build_operand_object(str_operand)
        self.operands.append(operand)

    def build_operand_object(self, str_operand):
        t = type(str_operand)
        operand = Operand(str_operand)

        if t == int:
            operand.set_type(Type.INT)
        elif t == float:
            operand.set_type(Type.FLOAT)
        elif t == str:
            operand.set_type(Type.STRING)

        return operand

    def add_type(self, _type):
        self.types.append(_type)

    def add_jump(self, jump):
        self.jumps.append(jump)

    def add_while(self):
        self.add_jump(self.q_count)

    def end_while(self):
        pass

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

    def solve_operation(self, l_operand, r_operand, operator):
        res = eval(
            f"{l_operand.get_str_operand()} {operator} {r_operand.get_str_operand()}")
        if type(res) == bool:
            res = 1 if res else 0
        return res

    def assign(self):
        result = self.operands.pop()
        result_type = self.types.pop()
        operand = self.operands.pop()
        operand_type = self.operand.pop()
        # Semantic cube checking.
        if not semantic_cube[operand_type][result_type][Operator.ASSIGN]:
            R


        #  operand (segundo pop) = result (primer pop)

    def maybe_solve_operation(self, operations):
        operator = self.get_operator()

        if operator in operations:
            r_operand = self.operands.pop()
            r_type = self.types.pop()
            l_operand = self.operands.pop()
            l_type = self.types.pop()
            operator = self.operators.pop()
            result_type = semantic_cube[l_type][r_type][operator]
            if result_type == "error":
                raise NameError(f"Type mismatch {l_type} {operator} {r_type}")
            result = self.solve_operation(l_operand, r_operand, operator)
            self.add_operand(result)
            self.add_type(result_type)

            # Development note: Beware, operands are objects now. Everything is perfectly fine... maybe.
            quad = [operator, l_operand, r_operand, result]
            self.add_quadruple(quad)
            self.q_count += 1
            print(quad)
