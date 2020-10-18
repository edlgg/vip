from semantic_cube import semantic_cube
from constants import types, Type

class Quadruples:

    def __init__(self):
        self.quadruples = []
        self.operators = []
        self.operands = []
        self.types = []
        self.jumps = []

    def print_all(self):
        print("operators: ", self.operators)
        print("operands: ", self.operands)

    def add_quadruple(self, quadruple):
        self.quadruples.append(quadruple)

    def add_operator(self, operator):
        self.operators.append(operator)

    def add_operand(self, operand):
        self.operands.append(operand)

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
        res = eval(f"{l_operand} {operator} {r_operand}")
        if type(res) == bool:
            res = 1 if res else 0
        return res

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
            quad = [operator, l_operand, r_operand, result]
            self.add_quadruple(quad)
            print(quad)
