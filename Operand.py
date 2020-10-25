from constants import Type

class Operand:

    def __init__(self, str_operand=None):
        self.__str_operand = str_operand

        self.__type: Type

        self.__address: int

    def __repr__(self):
        return f"{self.__str_operand}"

    def set_str_operand(self, str_operand):
        self.__str_operand = str_operand

    def get_str_operand(self):
        return self.__str_operand

    def set_type(self, type):
        self.__type = type

    def get_type(self):
        return self.__type

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address
