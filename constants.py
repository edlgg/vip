from enum import Enum
class Type(Enum):
     ERROR = 0
     INT = 1
     FLOAT = 2
     STRING = 3
     VOID = 4

types = {
    "int" : Type.INT,
    "float" : Type.FLOAT,
    "string" : Type.STRING,
    "void" : Type.VOID
}