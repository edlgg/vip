# %%
class Var:
    def __init__(self, name, var_type, address, assigned=False):
        self.name = name
        self.var_type = var_type
        self.address = address
        self.assigned = assigned


class Func:
    def __init__(self, name, return_type, num_params):
        self.name = name
        self.return_type = return_type
        self.num_params = num_params
        self.vars = {}

    def add_var(self, name, var_type, address):
        if name in self.vars:
            raise NameError(f"Var {name} already defined")
        self.vars[name] = Var(
            name=name, var_type=var_type, address=address)

    def delete_var(self, name):
        del self.vars[name]

    def is_var(self, name):
        if name in self.vars:
            return True
        return False

    def is_var_assigned(self, name):
        for _, var in self.vars.items():
            if var.name == name:
                return var.assigned

    def get_var_type(self, name):
        for _, var in self.vars.items():
            if var.name == name:
                return var.var_type

    def get_var_address(self, name):
        for _, var in self.vars.items():
            if var.name == name:
                return var.address


class AddressTable:
    def __init__(self):
        self.funcs = {}

    def add_func(self, name, return_type, num_params):
        if name in self.funcs:
            raise NameError(f"Func {name} already defined")
        self.funcs[name] = Func(
            name=name, return_type=return_type, num_params=num_params)

    def delete_func(self, name):
        del self.funcs[name]
