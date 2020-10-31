from constants import Type

class Operand:

    def __init__(self, str_operand=None, op_type=None, address=None):
        self.str_operand = str_operand

        self.type = op_type

        self.address = address

    def __repr__(self):
        return f"{self.str_operand}"

    def set_str_operand(self, str_operand):
        self.str_operand = str_operand

    def get_str_operand(self):
        return self.str_operand

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address
