import pytest
from parser import suma


@pytest.mark.parametrize(
    "a, b, c",
    [
        (1, 6, 7),
        (2, 5, 7),
        (3, 4, 7),
    ],
)
def test_data_consistency(a, b, c):
    assert suma(a, b) == c
