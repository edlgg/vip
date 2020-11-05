'''
VIP Scanner
Authors: David Souza & Eduardo de la Garza
'''

import ply.lex as lex

# Language reserved keywords.
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'string': 'STRING',
    'print': 'PRINT',
    'if': 'IF',
    'elif': 'ELIF',
    'else': 'ELSE',
    'while': 'WHILE',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'read': 'READ',
    'void': 'VOID',
    'function': 'FUNCTION',
    'return': 'RETURN',
    'main': 'MAIN',
    'global': 'GLOBAL',
}

# List of token names.
tokens = [
    'ID',
    'COLON',
    'SEMICOLON',
    'L_KEY_BRACKET',
    'R_KEY_BRACKET',
    'L_SQUARE_BRACKET',
    'R_SQUARE_BRACKET',
    'ASSIGN',
    'EQUALS',
    'GREATER',
    'GREATER_EQ',
    'LESS',
    'LESS_EQ',
    'NOT_EQUAL',
    'L_PARENS',
    'R_PARENS',
    'COMMA',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'CONST_STRING',
    'CONST_I',
    'CONST_F',
] + list(reserved.values())

t_COLON = r':'
t_SEMICOLON = r';'
t_L_KEY_BRACKET = r'{'
t_R_KEY_BRACKET = r'}'
t_L_SQUARE_BRACKET = r'\['
t_R_SQUARE_BRACKET = r'\]'
t_EQUALS = r'=='
t_ASSIGN = r'='
t_GREATER = r'>'
t_GREATER_EQ = r'>='
t_LESS = r'<'
t_LESS_EQ = r'<='
t_NOT_EQUAL = r'!='
t_L_PARENS = r'\('
t_R_PARENS = r'\)'
t_COMMA = r'\,'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'


def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  # Check if matched id is a reserved keyword.
  t.type = reserved.get(t.value, 'ID')
  return t

def t_CONST_F(t):
  r'(\d*)?[.]\d+'
  t.value = float(t.value)
  return t

def t_CONST_I(t):
  r'(0|-?[1-9]\d*)'
  t.value = int(t.value)
  return t

def t_CONST_STRING(t):
   r'".*"'
   t.value = str(t.value)
   return t

def t_newline(t):
  r'[\r\n]+'
  t.lexer.lineno += len(t.value)


def t_comment(t):
  r'\#.*\n'
  t.lexer.lineno += 1
  pass
  # No return value. Token discarded.


# Ignore space and tab characters.
t_ignore = ' \t\r'


#Error handling rule for lexer
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


#Build the lexer
lexer = lex.lex()


#data = '''function main {
#        int a;
#        a = 1;
#        while(i < 5) {
#        if(i < 3) {
#        print("smaller than 3: ", i);}
#        return k;
#        }
#        }'''

# Give the lexer some input
#lexer.input(data)

# Tokenize
#while True:
#    tok = lexer.token()
#    if not tok: 
#        break      # No more input
#    print(tok)
