'''
VIP Parser
Authors: David Souza & Eduardo de la Garza
'''

import ply.yacc as yacc
from scanner import tokens


def p_program(p):
    '''program : program_aux main
               | main'''

def p_program_aux(p):
    '''program_aux : program_aux function
                   | function'''

def p_function(p):
    'function : function_header function_body'

def p_main(p):
    'main : FUNCTION MAIN function_body'

def p_function_header(p):
    '''function_header : FUNCTION ID L_PARENS function_params R_PARENS COLON function_type
                       | FUNCTION ID L_PARENS R_PARENS COLON function_type'''

def p_function_body(p):
    '''function_body : L_KEY_BRACKET function_body_aux function_body_aux_2 R_KEY_BRACKET
                     | L_KEY_BRACKET function_body_aux_2 R_KEY_BRACKET'''

def p_function_body_aux(p):
    '''function_body_aux : var function_body_aux
                         | var'''

def p_function_body_aux2(p):
    '''function_body_aux_2 : statement function_body_aux_2
                           | statement'''

def p_function_params(p):
    '''function_params : type ID array_index COMMA function_params
                       | type ID array_index
                       | type ID COMMA function_params
                       | type ID'''

def p_function_type(p):
    '''function_type : type
                     | VOID'''

def p_var(p):
    '''var : type ID array_dim var_aux
           | type ID array_dim
           | type ID var_aux
           | type ID'''

def p_var_aux(p):
    '''var_aux : COMMA ID array_dim var_aux
               | COMMA ID array_dim
               | COMMA ID var_aux
               | COMMA ID'''

def p_statement(p):
    'statement : statement_aux SEMICOLON'

def p_statement_aux(p):
    '''statement_aux : assignment
                     | function_call
                     | return
                     | if
                     | while
                     | print'''

def p_type(p):
    '''type : INT
            | FLOAT
            | STRING'''

def p_array_index(p):
    '''array_index : L_SQUARE_BRACKET expression R_SQUARE_BRACKET L_SQUARE_BRACKET expression R_SQUARE_BRACKET
                   | L_SQUARE_BRACKET expression R_SQUARE_BRACKET'''

def p_array_dim(p):
    '''array_dim : L_SQUARE_BRACKET CONST_I R_SQUARE_BRACKET L_SQUARE_BRACKET CONST_I R_SQUARE_BRACKET
                 | L_SQUARE_BRACKET CONST_I R_SQUARE_BRACKET'''

def p_assignment(p):
    '''assignment : ID array_index EQUALS expression
                  | ID array_index EQUALS read
                  | ID EQUALS expression
                  | ID EQUALS read'''

def p_function_call(p):
    'function_call : ID params_pass'

def p_return(p):
    'return : RETURN expression'

def p_if(p):
    '''if : IF L_PARENS expression R_PARENS block elif else
          | IF L_PARENS expression R_PARENS block elif
          | IF L_PARENS expression R_PARENS block else
          | IF L_PARENS expression R_PARENS block'''

def p_elif(p):
    '''elif : ELIF L_PARENS expression R_PARENS block elif
            | ELIF L_PARENS expression R_PARENS block'''

def p_else(p):
    'else : ELSE block'

def p_while(p):
    'while : WHILE L_PARENS expression R_PARENS block'

def p_print(p):
    '''print : PRINT L_PARENS print_aux R_PARENS
             | PRINT L_PARENS R_PARENS'''

def p_print_aux(p):
    '''print_aux : CONST_STRING COMMA print_aux
                 | CONST_STRING
                 | ID COMMA print_aux
                 | ID'''

def p_expression(p):
    '''expression : exp AND expression
                  | exp'''

def p_read(p):
    'read : READ ID'

def p_params_pass(p):
    '''params_pass : L_PARENS expression params_pass_aux R_PARENS
                   | L_PARENS expression R_PARENS
                   | L_PARENS R_PARENS'''

def p_params_pass_aux(p):
    '''params_pass_aux : COMMA expression params_pass_aux
                       | COMMA expression'''

def p_block(p):
    'block : L_KEY_BRACKET statement R_KEY_BRACKET'

def p_exp(p):
    '''exp : xp OR exp
           | xp'''

def p_xp(p):
    '''xp : x log_op x
          | x'''

def p_x(p):
    '''x : term x_aux
         | term'''

def p_x_aux(p):
    '''x_aux : PLUS term x_aux
             | PLUS term
             | MINUS term x_aux
             | MINUS term'''

def p_log_op(p):
    '''log_op : NOT_EQUAL
              | IS_EQUAL
              | GREATER
              | GREATER_EQ
              | LESS
              | LESS_EQ'''

def p_term(p):
    '''term : factor term_aux
            | factor'''

def p_term_aux(p):
    '''term_aux : TIMES factor term_aux
                | TIMES factor
                | DIVIDE factor term_aux
                | DIVIDE factor'''

def p_factor(p):
    '''factor : NOT factor_aux
              | factor_aux'''

def p_factor_aux(p):
    '''factor_aux : L_PARENS expression R_PARENS
                  | PLUS const
                  | MINUS const
                  | const'''

def p_const(p):
    '''const : ID
             | CONST_I
             | CONST_F
             | CONST_STRING
             | function_call
             | array_access'''

def p_array_access(p):
    'array_access : ID array_index'

def p_error(p):
  print('There is an error:', p)


# Build parser.
parser = yacc.yacc(start='program')

data = '''
function sum(int a, int b): int {
    int res;
    res = a + b;
    return res;
}

function main {
    int res;
    print("Hello my friends!");
    
    res = sum(4, 4);
    print(res);
}
'''

# Give the lexer some input
# lexer.input(data)
