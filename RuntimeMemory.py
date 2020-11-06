from constants import Type, Scope

class RuntimeMemory():
    def __init__(self, scope, return_quad):
        self.scope = scope
        self.return_quad = return_quad

        # Global variables
        self.g_int_start = 1000
        self.g_float_start = 2000
        self.g_string_start = 3000

        # Local variables
        self.l_int_start = 4000
        self.l_float_start = 5000
        self.l_string_start = 6000

        # Temp variables
        self.t_int_start = 7000
        self.t_float_start = 8000
        self.t_string_start = 9000

        # Memory structures
        self.int_memory = {}
        self.float_memory = {}
        self.string_memory = {}
        self.temp_memory = {}

    def get_value_from_address_helper(self, address):
        if self.address_of_type(address, Type.INT):
            return self.int_memory[address]
        elif self.address_of_type(address, Type.FLOAT):
            return self.float_memory[address]
        elif self.address_of_type(address, Type.STRING):
            return self.string_memory[address]
        else:
            return self.temp_memory[address]

    def set_value_to_address_helper(self, value, address):
        if self.address_of_type(address, Type.INT):
            self.int_memory[address] = value
        elif self.address_of_type(address, Type.FLOAT):
            self.float_memory[address] = value
        elif self.address_of_type(address, Type.STRING):
            self.string_memory[address] = value
        else:
            self.temp_memory[address] = value

    def address_of_type(self, address, var_type):
        start, end = self.get_memory_range(self.scope, var_type)
        return self.validate_range(address, start, end)

    def validate_range(self, address, range_start, range_end):
        return address >= range_start and address <= range_end

    def get_memory_range(self, scope, var_type):
        start = 1000
        if scope == Scope.LOCAL:
            start = 4000
        elif scope == Scope.TEMP:
            start = 7000
        
        if var_type == Type.FLOAT:
            start += 1000
        elif var_type == Type.STRING:
            start += 2000

        return start, start + 999
        
            

