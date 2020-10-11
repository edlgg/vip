# %%
class Var:
    def __init__(self, name, var_type, address, assigned=False):
        self.name = name
        self.var_type = var_type
        self.address = address
        self.assigned = assigned


class Func:
    def __init__(self, name, func_type, num_params):
        self.name = name
        self.func_type = func_type
        self.num_params = num_params
        self.vars = {}

    def add_var(self, name, var_type, address):
        if name in self.vars:
            raise NameError(f"Var {name} already defined")
        self.vars[name] = Var(
            name=name, var_type=var_type, address=address)

    def delete_var(self, name):
        del self.vars[name]


class AddressTable:
    def __init__(self):
        self.funcs = {}

    def add_func(self, name, func_type, num_params):
        if name in self.funcs:
            raise NameError(f"Func {name} already defined")
        self.funcs[name] = Func(
            name=name, func_type=func_type, num_params=num_params)

    def delete_func(self, name):
        del self.funcs[name]
