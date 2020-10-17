class Quadruples:

    def __init__(self):
        self.table = []
        self.operators = []
        self.operands = []
        self.jumps = []

    def print_all(self):
        print("operators: ", self.operators)
        print("operands: ", self.operands)

    def add_quadruple(self, quadruple):
        self.table.append(quadruple)

    def add_operator(self, operator):
        self.operators.append(operator)

    def add_operand(self, operand):
        self.operands.append(operand)

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

    def maybe_solve_operation(self, operations):
        operator = self.get_operator()
        if operator in operations:
            r_operand = self.operands.pop()
            l_operand = self.operands.pop()
            operator = self.operators.pop()
            print(r_operand, l_operand, operator)
