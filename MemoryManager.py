'''
VIP Memory Manager
Authors: David Souza & Eduardo de la Garza
'''
from constants import Type, Scope


class MemoryManager:
    """
    A class to manage the assignment of memory addresses.

    '''
    Attributes
    ----------
    None

    Methods
    -------
    reset_temp_and_local_vars():
        Resets the temporary and local variable indexes
    """
    def __init__(self):
        """
        Initializes all the memory limits and indexes for the MemoryManager object.
        """
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

    '''
    '''
    def reset_temp_and_local_vars(self):
        """
        This method resets the temporary and local variable indexes.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.l_int_index = self.l_int_index - (self.l_int_index % 1000)
        self.l_float_index = self.l_float_index - (self.l_float_index % 1000)
        self.l_string_index = self.l_string_index - \
            (self.l_string_index % 1000)

        self.t_int_index = self.t_int_index - (self.t_int_index % 1000)
        self.t_float_index = self.t_float_index - (self.t_float_index % 1000)
        self.t_string_index = self.t_string_index - \
            (self.t_string_index % 1000)

    def set_address(self, scope, var_type, space_required=1):
        """
        Returns the next available address for a variable.

        Parameters
        ----------
            scope: Scope
                The scope of the variable (Scope.GLOBAL or Scope.LOCAL)
            var_type: Type
                The type of the variable (Type.INT, Type.FLOAT, Type.STRING)
            space_required: int, optional
                Memory space required for that particular variable (default is 1)

        Returns
        -------
            assigned_address (int): Memory address that is going to be assigned to the variable.
        """
        assigned_address = None
        if scope == Scope.GLOBAL:
            if var_type == Type.INT:
                if (self.g_int_index + space_required - 1) > self.g_int_end:
                    return -1  # Memory limit exceeded.
                assigned_address = self.g_int_index
                self.g_int_index += space_required
            elif var_type == Type.FLOAT:
                if (self.g_float_index + space_required - 1) > self.g_float_end:
                    return -1
                assigned_address = self.g_float_index
                self.g_float_index += space_required
            elif var_type == Type.STRING:
                if (self.g_string_index + space_required - 1) > self.g_string_end:
                    return -1
                assigned_address = self.g_string_index
                self.g_string_index += space_required
            else:
                return -2  # Invalid var_type given.

        elif scope == Scope.LOCAL:
            if var_type == Type.INT:
                if (self.l_int_index + space_required - 1) > self.l_int_end:
                    return -1  # Memory limit exceeded.
                assigned_address = self.l_int_index
                self.l_int_index += space_required
            elif var_type == Type.FLOAT:
                if (self.l_float_index + space_required - 1) > self.l_float_end:
                    return -1
                assigned_address = self.l_float_index
                self.l_float_index += space_required
            elif var_type == Type.STRING:
                if (self.l_string_index + space_required - 1) > self.l_string_end:
                    return -1
                assigned_address = self.l_string_index
                self.l_string_index += space_required
            else:
                return -2  # Invalid var_type given.

        return assigned_address

    def set_temp_address(self, var_type):
        """
        Returns the next available address for a temp variable.

        Parameters
        ----------
            var_type: Type
                The type of the variable (Type.INT, Type.FLOAT, Type.STRING)

        Returns
        -------
            assigned_address (int): Memory address that is going to be assigned to the temporary variable.
        """
        assigned_address = None

        if var_type == Type.INT:
            if self.t_int_index > self.t_int_end:
                return -1  # Memory limit exceeded.
            assigned_address = self.t_int_index
            self.t_int_index += 1
        elif var_type == Type.FLOAT:
            if self.t_float_index > self.t_float_end:
                return -1
            assigned_address = self.t_float_index
            self.t_float_index += 1
        elif var_type == Type.STRING:
            if self.t_string_index > self.t_string_end:
                return -1
            assigned_address = self.t_string_index
            self.t_string_index += 1
        else:
            return -2  # Invalid var_type given.

        return assigned_address

    def set_constant_address(self, constant_type):
        """
        Returns the next available address for a constant.

        Parameters
        ----------
            constant_type: Type
                The type of the variable (Type.INT, Type.FLOAT, Type.STRING)

        Returns
        -------
            assigned_address (int): Memory address that is going to be assigned to the constant.
        """
        assigned_address = None

        if constant_type == Type.INT:
            if self.c_int_index > self.c_int_end:
                return -1  # Memory limit exceeded.
            assigned_address = self.c_int_index
            self.c_int_index += 1
        elif constant_type == Type.FLOAT:
            if self.c_float_index > self.c_float_end:
                return -1
            assigned_address = self.c_float_index
            self.c_float_index += 1
        elif constant_type == Type.STRING:
            if self.c_string_index > self.c_string_end:
                return -1
            assigned_address = self.c_string_index
            self.c_string_index += 1
        else:
            return -2  # Invalid type given.

        return assigned_address
