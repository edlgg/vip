from constants import Type

# TODO: Consider deleting this class. I'm not sure if the new implementation of var makes this useless.

class Operand:

    def __init__(self, name=None, op_type=None, address=None, is_array=False, is_function_call=False):
        self.name = name

        self.type = op_type

        self.address = address

        self.is_array = is_array

        self.is_function_call = is_function_call

    def __repr__(self):
        return f"Operand({self.name}, {self.type}, {self.address})"

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def set_dims(self, dims):
        self.dims = dims

    def append_dim(self, dim):
        self.dims.append(dim)

    def get_dims(self):
        return self.dims
