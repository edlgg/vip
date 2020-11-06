from Quadruples import Quadruples
from constants import Operator, Scope
from RuntimeMemory import RuntimeMemory


class VirtualMachine():
    def __init__(self, quadruples, constants):
        self.quadruples = quadruples
        self.constants = constants
        self.quad_pointer = 0
        self.memories = []
        self.g_memory = RuntimeMemory(Scope.GLOBAL, -1)
        self.memories.append(self.g_memory)

    def get_value_from_address(self, address):
        if self.is_global_address(address):
            return self.g_memory.get_value_from_address_helper(address)
        elif self.is_local_or_temp_address(address):
            return self.memories[-1].get_value_from_address_helper(address)
        else:
            # TODO:Check this later.
            return self.constants[address]

    def set_value_to_address(self, value, address):
        if self.is_global_address(address):
            self.g_memory.set_value_to_address_helper(value, address)
        elif self.is_local_or_temp_address(address):
            self.memories[-1].set_value_to_address_helper(value, address)

    def is_global_address(self, address):
        return address >= self.g_memory.g_int_start and address < (self.g_memory.g_string_start + 1000)

    def is_local_or_temp_address(self, address):
        return address >= self.memories[-1].l_int_start and address < (self.memories[-1].t_string_start + 1000)

    def run(self):
        while self.quad_pointer < len(self.quadruples):
            self.process_quad(self.quadruples[self.quad_pointer])
            self.quad_pointer += 1

    def process_quad(self, quad):
        if quad[0] == Operator.ASSIGN:
            result = self.get_value_from_address(quad[1])
            self.set_value_to_address(result, quad[3])
            return
        elif quad[0] == Operator.GOTO:
            # Operator.GOTO, None, None, destination.
            self.quad_pointer = quad[3] - 1
            return
        elif quad[0] == Operator.GOTOF:
            # Operator.GOTOF, condition, None, destination.
            condition = self.get_value_from_address(quad[1])
            if not condition:
                self.quad_pointer = quad[3] - 1
            return
        elif quad[0] == Operator.ERA:
            new_memory_instance = RuntimeMemory(Scope.LOCAL, -1)
            self.memories.append(new_memory_instance)
            return
        elif quad[0] == Operator.RETURN:
            # WIP
            if self.memories[-1].scope == Scope.GLOBAL:
                self.quad_pointer = len(self.quadruples) - 1

            result = self.get_value_from_address(quad[-3])
            return
        elif quad[0] == Operator.PRINT:
            value_to_print = self.get_value_from_address(quad[3])
            print(value_to_print)
            return
        elif quad[0] == Operator.END:
            self.quad_pointer = len(self.quadruples) - 1
            return


        # Expression operands.
        left_operand = self.get_value_from_address(quad[1])
        right_operand = self.get_value_from_address(quad[2])
        result = None

        if quad[0] == Operator.PLUS:
            result = left_operand + right_operand
        elif quad[0] == Operator.MINUS:
            result = left_operand - right_operand
        elif quad[0] == Operator.TIMES:
            result = left_operand * right_operand
        elif quad[0] == Operator.DIVIDE:
            if right_operand == 0:
                raise NameError(f"Division by zero!")
            result = left_operand / right_operand
        elif quad[0] == Operator.GREATER:
            result = left_operand > right_operand
        elif quad[0] == Operator.LESS:
            result = left_operand < right_operand
        elif quad[0] == Operator.GREATER_EQ:
            result = left_operand >= right_operand
        elif quad[0] == Operator.LESS_EQ:
            result = left_operand <= right_operand
        elif quad[0] == Operator.EQUALS:
            result = left_operand == right_operand
        elif quad[0] == Operator.NOT_EQUAL:
            result = left_operand != right_operand
        elif quad[0] == Operator.AND:
            result = 1 if (left_operand and right_operand) else 0
        elif quad[0] == Operator.OR:
            result = 1 if (left_operand or right_operand) else 0
        else:
            return

        self.set_value_to_address(result, quad[3])