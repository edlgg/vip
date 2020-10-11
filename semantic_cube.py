class SemanticCube:
    def __init__(self):
        self.type_rules = {
            'int': {
                'int': {},
                'float': {},
                'string': {},
                'list_int': {},
                'list_float': {},
                'list_string': {},
            },
            'float': {},
            'string': {},
            'list_int': {},
            'list_float': {},
            'list_string': {},
        }
    "+": 0,
    "-": 1,
    "*": 2,
    "/": 3,

    # Asignación
    "=": 4,

    # Relacionales
    ">": 5,
    "<": 6,
    "<=": 7,
    ">=": 8,

    # Lógicos
    "==": 9,
    "!=": 10,
    "&&": 11,
    "||": 12,
    "!": 13
