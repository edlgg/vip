from constants import Type, allowed_return_types


class Dim:
    """
    A class to create array dimension objects.

    '''
    Attributes
    ----------
    lim_inf : int
        Lower limit of the dimension
    lim_sup : int
        Upper limit of the dimension
    m : int
        Variable needed to calculate array addresses
    has_range : bool
        It indicates if the dimension has a defined range e.g. A[1 .. 4].
        If it doesn't have a range, then the lower limit is always 0.

    Methods
    -------
    None
    """

    def __init__(self):
        """
        Constructs all the necessary attributes with their default values for the dim object

        Parameters
        ----------
        None
        """
        self.lim_inf = 0
        self.lim_sup = 0
        self.m = None
        self.has_range = False

    def set_lim_inf(self, lim_inf):
        self.has_range = True
        self.lim_inf = lim_inf

    def set_lim_sup(self, lim_sup):
        self.lim_sup = lim_sup
        if not self.has_range:
            self.lim_sup -= 1

    def set_m(self, m):
        self.m = m

    def get_lim_inf(self): return self.lim_inf
    def get_lim_sup(self): return self.lim_sup
    def get_m(self): return self.m


class Var:
    """
    A class to create var objects.

    '''
    Attributes
    ----------
    name : str
        Name of the var
    type : Type
        Type of the variable (Type.INT, Type.FLOAT, Type.STRING)
    address : int
        Memory address of the variable
    is_array : bool
        Indicates wheter or not the variable is an array (default is False)
    dims: Dim []
        Contains the Var dims when it is an array (default is None)


    Methods
    -------
    solve_dims(m)
        It iterates through dims to calculate their 'm' attribute
    """

    def __init__(self, name, type, address=None, is_array=False):
        """
        Constructs all the necessary attributes for the var object

        Parameters
        ----------
            name : str
                variable name
            type : Type
                variable type (Type.INT, Type.FLOAT, Type.STRING)
            address: int, optional
                variable assigned address (default is None)
            is_array: bool, optional
                it indicates wheter the var is an array or not (default is False)
        """
        self.name = name
        self.type = type
        self.address = address
        self.is_array = is_array
        self.dims = []

    def __repr__(self):
        return f"{self.name} {self.type} {self.address}"

    def get_type(self):
        return self.type

    def get_address(self):
        return self.address

    def add_dim(self, dim):
        self.dims.append(dim)

    def get_dim(self, index):
        return self.dims[index]

    def get_dim_count(self):
        return len(self.dims)

    def set_address(self, address):
        self.address = address

    def set_type(self, type):
        self.type = type

    def get_name(self):
        return self.name

    def solve_dims(self, m):
        """
        It iterates through dims to calculate their 'm' attribute

        When it reaches the last dim, it calculates -k and stores it in 'm'.

        Parameters
        ----------
        m: int
            It is the first m that serves to calculate the following m's.

        Returns
        -------
        None
        """
        offset = 0
        for dim in self.dims:
            d = dim.get_lim_sup() - dim.get_lim_inf() + 1
            m = int(m/d)
            offset += (dim.get_lim_inf() * m)
            dim.set_m(m)
        # Setting -k in the m field of the last Dim node
        self.dims[len(self.dims) - 1].set_m(-offset)


class Func:
    """
    A class to create function objects.

    '''
    Attributes
    ----------
    name : str
        Name of the function
    return_type : Type
        Return type of the function (Type.VOID, Type.INT, Type.FLOAT, Type.STRING)
    first_quadruple : int
        The first quadruple of the function
    num_params : int
        Indicates the number of parameters the function header has
    vars : Var {}
        Dictionary of local variables
    param_names : str []
        List of parameter names
    current_var_name : str
        auxiliary variable to keep track of the current variable we are definig, used in array declaration


    Methods
    -------
    add_var(operand)
        Adds a local var to the function
    """

    def __init__(self, name, first_quadruple, return_type=Type.VOID):
        """
        Constructs all the necessary attributes for the Func object

        Parameters
        ----------
            name : str
                function name
            first_quadruple : int
                index of the first quadruple of the function
            return_type: Type, optional
                return type of the functino (default is Type.VOID)
        """
        self.name = name
        self.return_type = return_type
        self.first_quadruple = first_quadruple
        self.num_params = 0
        self.vars = {}
        self.param_names = []
        self.current_var_name = None

    def add_var(self, operand):
        """
        Adds a local var to the function

        Parameters
        ----------
        operand : Operand
            Operand object that lives in Quadruples class

        Raises
        ------
        AlreadyDefinedError
            If variable has already been defined before.

        Returns
        -------
        None
        """
        name = operand.name
        if name in self.vars:
            raise NameError(f"Var {name} already defined")
        self.vars[name] = Var(name, operand.type,
                              operand.address, operand.is_array)

    def get_var(self, name):
        if name in self.vars:
            return self.vars[name]
        else:
            return -1

    def delete_var(self, name):
        del self.vars[name]

    def is_var(self, name):
        return name in self.vars

    def assign_return_type(self, return_type):
        if return_type not in allowed_return_types:
            raise NameError(f"Invalid return type: {return_type}")
        self.return_type = return_type

    def get_var_type(self, name):
        return self.vars[name].type

    def get_var_address(self, name):
        return self.vars[name].address

    def get_return_type(self):
        return self.return_type

    def get_name(self):
        return self.name


class AddressTable:
    """
    A class to create Address Table objects.

    '''
    Attributes
    ----------
    funcs : Func {}
        Dictionary of functions for our program
    current_func_name: str
        Helps us to keep track of the name of the current function we are defining
    constant_addresses : Type {{}}
        Dictionary of dictionaries to store our constants addresses
    global_addresses: Type {{}}
        Dictionary of dictionaries to store our global variables addreses


    Methods
    -------
    add_func(operand)
        Adds a function to the address table
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the AddressTable object

        Parameters
        ----------
        None
        """
        self.funcs = {}
        self.current_func_name = None
        self.constants_addresses = {
            Type.INT: {},
            Type.FLOAT: {},
            Type.STRING: {},
        }
        self.global_addresses = {}

    def add_func(self, name, first_quadruple=None, return_type=Type.VOID):
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

    # TODO: Encapsulate these 4 functions into 2.

    def add_constant_address(self, constant_value, constant_type, address):
        # TODO: Check this. Probably it's useful in some cases (WHICH?) but it's generating error at the moment.
        # if constant_type == Type.STRING:
        #     constant_value = constant_value[0] + \
        #         constant_value[2:-2] + constant_value[-1]
        self.constants_addresses[constant_type][constant_value] = address

    def get_constant_address(self, constant_value, constant_type):
        if constant_value in self.constants_addresses[constant_type]:
            return self.constants_addresses[constant_type][constant_value]
        else:
            return -1  # Constant doesn't exist yet.

    def add_global_address(self, operand):
        name = operand.name
        if name in self.global_addresses:
            raise NameError(f"Var {name} already defined")
        self.global_addresses[name] = Var(name, operand.type,
                                          operand.address, operand.is_array)

    def get_global_var(self, global_value):
        if global_value in self.global_addresses:
            return self.global_addresses[global_value]
        else:
            return -1  # Global doesn't exist yet.

    def print_all(self):
        for _, func in self.funcs.items():
            print("******", func.name, "******")
            print("VARIABLES LOCALES:")
            for _, var in func.vars.items():
                print(var.name, var.type, var.address)
        print("CONSTANTES:")
        for key, value in self.constants_addresses[Type.INT].items():
            print(key, value)
        for key, value in self.constants_addresses[Type.FLOAT].items():
            print(key, value)
        for key, value in self.constants_addresses[Type.STRING].items():
            print(key, value)
        print("GLOBALES:")
        for _, var in self.global_addresses.items():
            print(var.name, var.type, var.address)
