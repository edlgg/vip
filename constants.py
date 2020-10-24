from enum import Enum


class Type(Enum):
    ERROR = 0
    INT = 1
    FLOAT = 2
    STRING = 3
    VOID = 4


# Map from string type to Enum type.
types = {
    "int": Type.INT,
    "float": Type.FLOAT,
    "string": Type.STRING,
    "void": Type.VOID
}


class Operator(Enum):
    PLUS = 0
    MINUS = 1
    TIMES = 2
    DIVIDE = 3
    ASSIGN = 4
    GREATER = 5
    LESS = 6
    LESS_EQ = 7
    GREATER_EQ = 8
    IS_EQUAL = 9
    NOT_EQUAL = 10
    AND = 11
    OR = 12
