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

    def set_value_to_address(self, value, address):
        if self.is_global_address(address):
            self.g_memory.set_value_to_address_helper(value, address)
        elif self.is_local_or_temp_address(address):
            self.memories[-1].set_value_to_address_helper(value, address)

    def is_global_address(self, address):
        if address >= self.g_memory.g_int_start and address < (self.g_memory.g_string_start + 1000):
            return True
        else:
            return False

    def is_local_or_temp_address(self, address):
        if address >= self.memories[-1].l_int_start and address < (self.memories[-1].t_string_start + 1000):
            return True
        else:
            return False

    def run(self):
        while self.quad_pointer < len(self.quadruples):
            self.process_quad(self.quadruples[self.quad_pointer])
            self.quad_pointer += 1

    def process_quad(self, quad):
        if quad[0] == Operator.GOTO:
            # Operator.GOTO, None, None, destination.
            self.quad_pointer = quad[3] - 1
            return
        elif quad[0] == Operator.GOTOF:
            # Operator.GOTOF, condition, None, destination.
            condition = get_value_from_address(quad[1])
            if not condition:
                self.quad_pointer = quad[3] - 1
