from constants import Type


class MemoryManager:
    def __init__(self):
        # Global Variables
        self.g_int_index = 1000
        self.g_int_end = 1999
        self.g_float_index = 2000
        self.g_float_end = 2999
        self.g_string_index = 3000
        self.g_string_end = 3999

        # Local Variables
        self.l_int_index = 4000
        self.l_int_end = 4999
        self.l_float_index = 5000
        self.l_float_end = 5999
        self.l_string_index = 6000
        self.l_string_end = 6999

        # Temporary Variables
        self.t_int_index = 7000
        self.t_int_end = 7999
        self.t_float_index = 8000
        self.t_float_end = 8999
        self.t_string_index = 9000
        self.t_string_end = 9999

        # Constants
        self.c_int_index = 10000
        self.c_int_end = 10999
        self.c_float_index = 11000
        self.c_float_end = 11999
        self.c_string_index = 12000
        self.c_string_end = 12999

    def reset_temp_and_local_vars(self):
        self.l_int_index = self.l_int_index - (self.l_int_index % 1000)
        self.l_float_index = self.l_float_index - (self.l_float_index % 1000)
        self.l_string_index = self.l_string_index - \
            (self.l_string_index % 1000)

        self.t_int_index = self.t_int_index - (self.t_int_index % 1000)
        self.t_float_index = self.t_float_index - (self.t_float_index % 1000)
        self.t_string_index = self.t_string_index - \
            (self.t_string_index % 1000)

    def setAddress(self, scope, var_type, space_required=1):
        assignedAddress = None
        if scope == 'global':
            if var_type == Type.INT:
                if (self.g_int_index + space_required - 1) > self.g_int_end:
                    return -1  # Memory limit exceeded.
                assignedAddress = self.g_int_index
                self.g_int_index += space_required
            elif var_type == Type.FLOAT:
                if (self.g_float_index + space_required - 1) > self.g_float_end:
                    return -1
                assignedAddress = self.g_float_index
                self.g_float_index += space_required
            elif var_type == Type.STRING:
                if (self.g_string_index + space_required - 1) > self.g_string_end:
                    return -1
                assignedAddress = self.g_string_index
                self.g_string_index += space_required
            else:
                return -2  # Invalid var_type given.

        elif scope == 'local':
            if var_type == Type.INT:
                if (self.l_int_index + space_required - 1) > self.l_int_end:
                    return -1  # Memory limit exceeded.
                assignedAddress = self.l_int_index
                self.l_int_index += space_required
            elif var_type == Type.FLOAT:
                if (self.l_float_index + space_required - 1) > self.l_float_end:
                    return -1
                assignedAddress = self.l_float_index
                self.l_float_index += space_required
            elif var_type == Type.STRING:
                if (self.l_string_index + space_required - 1) > self.l_string_end:
                    return -1
                assignedAddress = self.l_string_index
                self.l_string_index += space_required
            else:
                return -2  # Invalid var_type given.

        return assignedAddress

    def setTempAddress(self, var_type):
        assignedAddress = None

        if var_type == Type.INT:
            if self.t_int_index > self.t_int_end:
                return -1  # Memory limit exceeded.
            assignedAddress = self.t_int_index
            self.t_int_index += 1
        elif var_type == Type.FLOAT:
            if self.t_float_index > self.t_float_end:
                return -1
            assignedAddress = self.t_float_index
            self.t_float_index += 1
        elif var_type == Type.STRING:
            if self.t_string_index > self.t_string_end:
                return -1
            assignedAddress = self.t_string_index
            self.t_string_index += 1
        else:
            return -2  # Invalid var_type given.

        return assignedAddress

    def setConstantAddress(self, var_type):
        assignedAddress = None

        if var_type == Type.INT:
            if self.c_int_index > self.c_int_end:
                return -1  # Memory limit exceeded.
            assignedAddress = self.c_int_index
            self.c_int_index += 1
        elif var_type == Type.FLOAT:
            if self.c_float_index > self.c_float_end:
                return -1
            assignedAddress = self.c_float_index
            self.c_float_index += 1
        elif var_type == Type.STRING:
            if self.c_string_index > self.c_string_end:
                return -1
            assignedAddress = self.c_string_index
            self.c_string_index += 1
        else:
            return -2  # Invalid var_type given.

        return assignedAddress
