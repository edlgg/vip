import pytest
from AddressTable import Var, Func, AddressTable
from constants import Type


class TestFunc:
    @pytest.mark.parametrize(
        "name, var_type, address",
        [
            ("a", Type.INT, 1),
            ("b", Type.INT, 2),
            ("c", Type.INT, 3),
        ],
    )
    def test_var_init(self, name, type, address):
        var = Var(name=name, type=type, address=address)
        assert var.name == name
        assert var.type == type
        assert var.address == address

    @pytest.mark.parametrize(
        "name, return_type, first_quadruple",
        [
            ("a", Type.INT, 29),
            ("b", Type.INT, 50),
            ("c", Type.INT, 3),
        ],
    )
    def test_func_init(self, name, return_type, first_quadruple):
        func = Func(name=name, return_type=return_type, first_quadruple=first_quadruple)
        assert func.name == name
        assert func.return_type == return_type
        assert func.first_quadruple == first_quadruple

    @pytest.mark.parametrize(
        "name, var_type, address",
        [
            ("a", "int", 1),
            ("b", "int", 2),
            ("c", "int", 3),
        ],
    )
    def test_add_var(self, name, var_type, address):
        func = Func(name="test", return_type=Type.VOID, first_quadruple=15)
        func.add_var(name=name, type=var_type, address=address)
        assert name in func.vars

    @pytest.mark.parametrize(
        "name, var_type, address",
        [
            ("a", "int", 1),
            ("b", "int", 2),
            ("c", "int", 3),
        ],
    )
    def test_delete_var(self, name, var_type, address):
        func = Func(name="test", return_type="void")
        func.add_var(name=name, var_type=var_type, address=address)
        assert name in func.vars
        func.delete_var(name)
        assert name not in func.vars

    @pytest.mark.parametrize(
        "name, search, result",
        [
            ("a", "a", True),
            ("a", "b", False),
        ],
    )
    def test_is_var(self, name, search, result):
        func = Func(name="test", return_type=Type.VOID)
        func.add_var(name=name, var_type="int", address=1)
        assert func.is_var(search) == result

   
    @pytest.mark.parametrize(
        "name, assign",
        [
            ("a", True),
            ("a", False)
        ],
    )
    def test_is_var_assigned(self, name, assign):
        func = Func(name="test", return_type="void")
        func.add_var(name=name, var_type="int", address=1)

        if assign:
            func.assign_var(name=name)

        assert func.is_var_assigned(name) == assign

    @pytest.mark.parametrize(
        "var_type",
        [
            ("int"),
            ("double")
        ],
    )
    def test_get_var_type(self, var_type):
        func = Func(name="test", return_type="void")
        func.add_var(name="a", var_type=var_type, address=1)
        assert func.vars["a"].var_type == var_type

    @pytest.mark.parametrize(
        "address",
        [
            (1),
            (2)
        ],
    )
    def test_get_var_address(self, address):
        func = Func(name="test", return_type="void")
        func.add_var(name="a", var_type="int", address=address)
        assert func.vars["a"].address == address


class TestAddressTable:
    @pytest.mark.parametrize(
        "name, return_type",
        [
            ("func1", "int"),
            ("func2", "float")
        ],
    )
    def test_add_func(self, name, return_type):
        table = AddressTable()
        table.add_func(name=name, return_type=return_type)
        assert name in table.funcs
        assert table.funcs[name].return_type == return_type

    @pytest.mark.parametrize(
        "name, assign",
        [
            ("func1", True),
            ("func2", False)
        ],
    )
    def test_is_func(self, name, assign):
        table = AddressTable()
        if assign:
            table.add_func(name=name, return_type="void")
        assert table.is_func(name) == assign

    @pytest.mark.parametrize(
        "name",
        [
            ("func1"),
            ("func2")
        ],
    )
    def test_get_func(self, name):
        table = AddressTable()
        table.add_func(name=name, return_type="void")
        assert table.get_func(name).name == name

    @pytest.mark.parametrize(
        "name",
        [
            ("func1"),
            ("func2")
        ],
    )
    def test_del_func(self, name):
        table = AddressTable()
        table.add_func(name=name, return_type="void")
        assert table.is_func(name)
        table.del_func(name)
        assert not table.is_func(name)
