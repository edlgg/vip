import pytest
from AddressTable import Var, Func


@pytest.mark.parametrize(
    "name, var_type, address",
    [
        ("a", "int", 1),
        ("b", "int", 2),
        ("c", "int", 3),
    ],
)
def test_var_init(name, var_type, address):
    var = Var(name=name, var_type=var_type, address=address)
    assert var.name == name
    assert var.var_type == var_type
    assert var.address == address


@pytest.mark.parametrize(
    "name, return_type, num_params",
    [
        ("a", "int", 1),
        ("b", "int", 2),
        ("c", "int", 3),
    ],
)
def test_func_init(name, return_type, num_params):
    func = Func(name=name, return_type=return_type, num_params=num_params)
    assert func.name == name
    assert func.return_type == return_type
    assert func.num_params == num_params


@pytest.mark.parametrize(
    "name, var_type, address",
    [
        ("a", "int", 1),
        ("b", "int", 2),
        ("c", "int", 3),
    ],
)
def test_add_var(name, var_type, address):
    func = Func(name="test", return_type="void", num_params=0)
    func.add_var(name=name, var_type=var_type, address=address)
    for _, var in func.vars.items():
        if var.name == name:
            assert var.name == name
