class Quadruples:

    def __init__(self):
        self.table = []
        self.operators = []
        self.operands = []
        self.jumps = []

    def add_quadruple(self, quadruple):
        self.table.append(quadruple)

    def add_operator(self, operator):
        self.operators.append(operator)

    def add_operand(self, operand):
        self.operands.append(operand)

    def add_jump(self, jump):
        self.jumps.append(jump)

    def get_operator(self):
        return self.operators[-1]

    def get_operand(self):
        return self.operands[-1]

    def get_jump(self):
        return self.jumps[-1]

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
