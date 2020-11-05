from constants import Type


class Var:
    def __init__(self, name, var_type, address=None):
        self.name = name
        self.var_type = var_type
        self.address = address


class Const:
    def __init__(self, name, const_type, address=None):
        self.name = name
        self.const_type = const_type
        self.address = address


class Func:
    def __init__(self, name, first_quadruple, return_type="void"):
        self.name = name
        self.return_type = return_type
        self.num_params = 0
        self.num_local_vars = 0
        self.num_temp_vars = 0
        self.quad_start = None
        self.vars = {}
        self.return_types = ["void", "int", "float", "string"]
        self.first_quadruple = first_quadruple

    def add_var(self, operand):
        name = operand.str_operand
        if name in self.vars:
            raise NameError(f"Var {name} already defined")
        self.vars[name] = operand

    def get_var(self, name):
        return self.vars[name]

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
        self.constants_addresses = {
            Type.INT: {},
            Type.FLOAT: {},
            Type.STRING: {},
        }
        # This helps us keep track of the function we're defining
        # variables for.

    def add_func(self, name, first_quadruple=None, return_type="void"):
        if name in self.funcs:
            raise NameError(f"Func {name} already defined")
        self.current_func_name = name
        self.funcs[name] = Func(
            name=name, return_type=return_type, first_quadruple=first_quadruple)

    def is_func(self, name):
        return name in self.funcs

    def get_func(self, name):
        return self.funcs[name]

    def del_func(self, name):
        del self.funcs[name]
    
    def add_constant_address(self, constant_value, constant_type, address):
        self.constants_addresses[constant_type][constant_value] = address

    def get_constant_address(self, constant_value, constant_type):
        if constant_value in self.constants_addresses[constant_type]:
            return self.constants_addresses[constant_type][constant_value]
        else:
            return -1  # Constant doesn't exist yet.

    def print_all(self):
        for _, func in self.funcs.items():
            print("******", func.name, "******")
            print("VARIABLES LOCALES:")
            for _, var in func.vars.items():
                print(var.str_operand, var.type, var.address)
        print("CONSTANTES:")
        for key, value in self.constants_addresses[Type.INT].items():
            print(key, value)
        for key, value in self.constants_addresses[Type.FLOAT].items():
            print(key, value)
        for key, value in self.constants_addresses[Type.STRING].items():
            print(key, value)
