'''
VIP Scanner
Authors: David Souza & Eduardo de la Garza
'''

import ply.lex as lex

# Python's reserved keywords.
reserved = {
    'program': 'PROGRAM',
    'var': 'VAR',
    'int': 'INT',
    'float': 'FLOAT',
    'print': 'PRINT',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'true': 'TRUE',
    'false': 'FALSE',
    'read': 'READ',
    'write': 'WRITE',
    'void': 'VOID',
}

# List of token names.
tokens = [
    'ID',
    'COLON',
    'SEMICOLON',
    'L_BRACKET',
    'R_BRACKET',
    'L_SQUARE_B',
    'R_SQUARE_B',
    'EQUALS',
    'IS_EQUAL',
    'GREATER',
    'GREATER_EQ',
    'LESS',
    'LESS_EQ',
    'NOT_EQUAL',
    'L_PARENTHESIS',
    'R_PARENTHESIS',
    'COMMA',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'CTE_STRING',
    'CTE_I',
    'CTE_F',
] + list(reserved.values())

t_COLON = r':'
t_SEMICOLON = r';'
t_L_BRACKET = r'{'
t_R_BRACKET = r'}'
t_L_SQUARE_B = r'\['
t_R_SQUARE_B = r'\]'
t_EQUALS = r'='
t_IS_EQUAL = r'=='
t_GREATER = r'>'
t_GREATER_EQ = r'>='
t_LESS = r'<'
t_LESS_EQ = r'<='
t_NOT_EQUAL = r'!='
t_L_PARENTHESIS = r'\('
t_R_PARENTHESIS = r'\)'
t_COMMA = r'\,'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_CTE_STRING = r'".*"'


def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  # Check if matched id is a reserved keyword.
  t.type = reserved.get(t.value, 'ID')
  return t


def t_CTE_I(t):
  r'[-+]?(0|[1-9][0-9]*)'
  t.value = int(t.value)
  return t


def t_CTE_F(t):
  r'[-+]?(0|[1-9][0-9]*)(\.[0-9]+)?'
  t.value = float(t.value)
  return t


def t_newline(t):
  r'[\r\n]+'
  t.lexer.lineno += len(t.value)


def t_comment(t):
  r'\#.*\n'
  t.lexer.lineno += 1
  pass


# Ignore space and tab characters.
t_ignore = ' \t'


#Error handling rule for lexer
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


#Build the lexer
lexer = lex.lex()
