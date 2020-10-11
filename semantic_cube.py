class SemanticCube:
    def __init__(self):
        self.dict_operators = {
            "PLUS" : 0,       # +
            "MINUS" : 1,      # -
            "TIMES" : 2,      # *
            "DIVIDE" : 3,     # /

            "EQUALS" : 4,     # =

            "GREATER" : 5,    # >
            "LESS" : 6,       # <
            "LESS_EQ" : 7,    # <=
            "GREATER_EQ" : 8, # >=

            "IS_EQUAL" : 9,   # ==
            "NOT_EQUAL" : 10, # !=

            "AND" : 11,       # and
            "OR" : 12,        # or
        }

        self.array_types = [
            "error",         # 0
            "int",           # 1
            "float",         # 2
            "string",        # 3
        ] 

        self.semantic_cube = {
            "int": {
                "int":    {
                    "PLUS":       "int",  
                    "MINUS":      "int",     
                    "TIMES":      "int",    
                    "DIVIDE":     "float",  
                    "EQUALS":     "int", 
                    "GREATER":    "int",   
                    "LESS":       "int",    
                    "LESS_EQ":    "int",    
                    "GREATER_EQ": "int", 
                    "IS_EQUAL":   "int",  
                    "NOT_EQUAL":  "int", 
                    "AND":        "int",    
                    "OR":         "int",     
                },
                "float": {
                    "PLUS":       "float",
                    "MINUS":      "float",
                    "TIMES":      "float",
                    "DIVIDE":     "float",
                    "EQUALS":     "int",
                    "GREATER":    "int",
                    "LESS":       "int",
                    "LESS_EQ":    "int",
                    "GREATER_EQ": "int",
                    "IS_EQUAL":   "int",
                    "NOT_EQUAL":  "int",
                    "AND":        "int",
                    "OR":         "int",
                },
                "string": {
                    "PLUS":       "string",
                    "MINUS":      "error",
                    "TIMES":      "string",
                    "DIVIDE":     "error",
                    "EQUALS":     "error",
                    "GREATER":    "error",
                    "LESS":       "error",
                    "LESS_EQ":    "error",
                    "GREATER_EQ": "error",
                    "IS_EQUAL":   "int",
                    "NOT_EQUAL":  "int",
                    "AND":        "error",
                    "OR":         "error",
                }
            },
            "float": {
                "int":    {
                    "PLUS":       "float",
                    "MINUS":      "float",
                    "TIMES":      "float",
                    "DIVIDE":     "float",
                    "EQUALS":     "float",
                    "GREATER":    "int",
                    "LESS":       "int",
                    "LESS_EQ":    "int",
                    "GREATER_EQ": "int",
                    "IS_EQUAL":   "int",
                    "NOT_EQUAL":  "int",
                    "AND":        "int",
                    "OR":         "int",
                },
                "float": {
                    "PLUS":       "float",
                    "MINUS":      "float",
                    "TIMES":      "float",
                    "DIVIDE":     "float",
                    "EQUALS":     "float",
                    "GREATER":    "int",
                    "LESS":       "int",
                    "LESS_EQ":    "int",
                    "GREATER_EQ": "int",
                    "IS_EQUAL":   "int",
                    "NOT_EQUAL":  "int",
                    "AND":        "int",
                    "OR":         "int",
                }
                "string": {
                    "PLUS":       "string",
                    "MINUS":      "error",
                    "TIMES":      "error",
                    "DIVIDE":     "error",
                    "EQUALS":     "error",
                    "GREATER":    "error",
                    "LESS":       "error",
                    "LESS_EQ":    "error",
                    "GREATER_EQ": "error",
                    "IS_EQUAL":   "int",
                    "NOT_EQUAL":  "int",
                    "AND":        "error",
                    "OR":         "error",
                },
            },
            "string": {
                "int":    [3, 0, 3, 0, 3, 0, 0, 0, 0, 1, 1, 0, 0],
                "float":  [3, 0, 0, 0, 3, 0, 0, 0, 0, 1, 1, 0, 0],
                "string": [3, 0, 0, 0, 3, 1, 1, 1, 1, 1, 1, 1, 1],
            },
        }


