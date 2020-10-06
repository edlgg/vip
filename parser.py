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
    '''function_header : FUNCTION ID L_PARENS function_header_aux R_PARENS COLON function_type'''

def p_function_header_aux(p):
    '''function_header_aux : function_params
                           | empty'''

def p_function_body(p):
    'function_body : L_KEY_BRACKET function_body_aux function_body_aux_2 R_KEY_BRACKET'

def p_function_body_aux(p):
    '''function_body_aux : var function_body_aux
                         | empty'''

def p_function_body_aux2(p):
    '''function_body_aux_2 : statement function_body_aux_2
                           | statement'''

def p_function_params(p):
    'function_params : type ID function_params_aux function_params_aux_2'

def p_function_params_aux(p):
    '''function_params_aux : array_index
                           | empty'''

def p_function_params_aux_2(p):
    '''function_params_aux_2 : COMMA function_params
                            | empty'''

def p_function_type(p):
    '''function_type : type
                     | VOID'''

def p_var(p):
    'var : type ID var_aux var_aux_2'

def p_var_aux(p):
    '''var_aux : array_dim
               | empty'''

def p_var_aux_2(p):
    '''var_aux_2 : COMMA ID var_aux var_aux_2
                 | empty'''

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
    'assignment : ID assignment_aux EQUALS assignment_aux_2'

def p_assignment_aux(p):
    '''assignment_aux : array_index
                      | empty'''

def p_assigmnent_aux_2(p):
    '''assignment_aux_2 : expression
                        | read'''

def p_function_call(p):
    'function_call : ID params_pass'

def p_return(p):
    'return : RETURN expression'

def p_if(p):
    'if : IF L_PARENS expression R_PARENS block elif else'

def p_elif(p):
    '''elif : ELIF L_PARENS expression R_PARENS block elif
            | empty'''

def p_else(p):
    '''else : ELSE block
            | empty'''

def p_while(p):
    'while : WHILE L_PARENS expression R_PARENS block'

def p_print(p):
    'print : PRINT L_PARENS print_aux R_PARENS'

def p_print_aux(p):
    '''print_aux : CONST_STRING print_aux_2
                 | ID print_aux_2
                 | empty'''

def p_print_aux_2(p):
    '''print_aux_2 : COMMA ID print_aux_2
                   | COMMA CONST_STRING print_aux_2
                   | empty'''

def p_expression(p):
    'expression : exp expression_aux'

def p_expression_aux(p):
    '''expression_aux : AND exp expression_aux
                      | empty'''

def p_read(p):
    'read : READ ID'

def p_params_pass(p):
    'params_pass : L_PARENS params_pass_aux R_PARENS'

def p_params_pass_aux(p):
    '''params_pass_aux : expression params_pass_aux_2
                       | empty'''

def p_params_pass_aux_2(p):
    '''params_pass_aux_2 : COMMA expression params_pass_aux_2
                         | empty'''

def p_block(p):
    'block : L_KEY_BRACKET statement R_KEY_BRACKET'

def p_exp(p):
    'exp : xp exp_aux'

def p_exp_aux(p):
    '''exp_aux : OR xp exp_aux
               | empty'''

def p_xp(p):
    'xp : x xp_aux'

def p_xp_aux(p):
    '''xp_aux : log_op x
            | empty'''

def p_x(p):
    'x : term x_aux'

def p_x_aux(p):
    '''x_aux : PLUS term x_aux
             | MINUS term x_aux
             | empty'''

def p_log_op(p):
    '''log_op : NOT_EQUAL
              | IS_EQUAL
              | GREATER
              | GREATER_EQ
              | LESS
              | LESS_EQ'''

def p_term(p):
    'term : factor term_aux'

def p_term_aux(p):
    '''term_aux : TIMES factor term_aux
                | DIVIDE factor term_aux
                | empty'''

def p_factor(p):
    'factor : factor_aux factor_aux_2'

def p_factor_aux(p):
    '''factor_aux : NOT
                  | empty'''

def p_factor_aux_2(p):
    '''factor_aux_2 : L_PARENS expression R_PARENS
                    | factor_aux_3 const'''


def p_factor_aux_3(p):
    '''factor_aux_3 : PLUS
                    | MINUS
                    | empty'''

def p_const(p):
    '''const : ID
             | CONST_I
             | CONST_F
             | CONST_STRING
             | function_call
             | array_access'''

def p_array_access(p):
    'array_access : ID array_index'


def p_empty(p):
  '''empty :'''


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
