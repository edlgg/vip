import pytest

from SemanticCube import SemanticCube

class TestFunc:

    @pytest.mark.parametrize(
        "var_type_1, var_type_2, operator, var_type_output",
        [
            ("int", "int", "PLUS", "int"),
            ("float", "int", "TIMES", "float"),
            ("string", "float", "DIVIDE", "error")
        ],
    )
    def test_check_type_compatibility(self, var_type_1, var_type_2, operator, var_type_output):
        semanticCube = SemanticCube()
        assert semanticCube.type_rules[var_type_1][var_type_2][operator] == var_type_output