
class Var:
    def __init__(self, name, var_type, address=None):
        self.name = name
        self.var_type = var_type
        self.address = address


class Func:
    def __init__(self, name, return_type="void", num_params=0):
        self.name = name
        self.return_type = return_type
        self.num_params = num_params
        self.vars = {}
        self.return_types = ["void", "int", "float", "string"]

    def add_var(self, operand):
        name = operand.str_operand
        if name in self.vars:
            raise NameError(f"Var {name} already defined")
        self.vars[name] = operand

    def delete_var(self, name):
        del self.vars[name]

    def is_var(self, name):
        return name in self.vars

    def assign_num_params(self, name, num_params):
        self.vars[name].num_params = num_params

    def assign_return_type(self, return_type):
        if return_type not in self.return_types:
            raise NameError(f"Invalid return type: {return_type}")
        self.return_type = return_type

    def get_var_type(self, name):
        return self.vars[name].type

    def get_var_address(self, name):
        return self.vars[name].address


class AddressTable:
    def __init__(self):
        self.funcs = {}
        self.current_func_name = None

        # This helps us keep track of the function we're defining
        # variables for.

    def add_func(self, name, return_type="void", num_params=0):
        if name in self.funcs:
            raise NameError(f"Func {name} already defined")
        self.current_func_name = name
        self.funcs[name] = Func(
            name=name, return_type=return_type, num_params=num_params)

    def is_func(self, name):
        return name in self.funcs

    def get_func(self, name):
        return self.funcs[name]

    def del_func(self, name):
        del self.funcs[name]

    def print_all(self):
        for _, func in self.funcs.items():
            print(func.name)
            for _, var in func.vars.items():
                print(var.str_operand, var.type, var.address)
                