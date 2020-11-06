class RuntimeMemory():
    def __init__(self, scope, reSturn_quad):
        self.scope = scope
        self.return_quad = return_quad

        # Global variables
        self.g_int_start = 1000
        self.g_float_start = 2000
        self.g_string = 3000

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

    def get_value_from_address_helper():
        pass
