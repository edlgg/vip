'''
VIP Parser
Authors: David Souza & Eduardo de la Garza
'''

import ply.yacc as yacc
from scanner import tokens
from Quadruples import Quadruples
from AddressTable import AddressTable
from constants import types

global AT, Q, last_var_type
Q = Quadruples()
AT = AddressTable()


def p_program(p):
    '''program : program_aux main
               | main'''


def p_program_aux(p):
    '''program_aux : program_aux function
                   | function'''


def p_function(p):
    'function : function_header function_body n_end_function'


def p_main(p):
    'main : FUNCTION MAIN n_start_main function_body n_end_function'


def p_function_header(p):
    '''function_header : FUNCTION ID n_add_function_name L_PARENS function_params R_PARENS COLON function_type
                       | FUNCTION ID n_add_function_name L_PARENS R_PARENS COLON function_type'''


def p_function_body(p):
    '''function_body : L_KEY_BRACKET function_body_aux statements R_KEY_BRACKET
                     | L_KEY_BRACKET statements R_KEY_BRACKET'''


def p_function_body_aux(p):
    '''function_body_aux : var function_body_aux
                         | var'''


def p_statements(p):
    '''statements : statement statements
                           | statement'''


def p_function_params(p):
    '''function_params : type ID n_add_var array_index COMMA function_params
                       | type ID n_add_var array_index
                       | type ID n_add_var COMMA function_params
                       | type ID n_add_var'''


def p_function_type(p):
    '''function_type : INT n_add_function_type
                     | FLOAT n_add_function_type
                     | STRING n_add_function_type
                     | VOID n_add_function_type'''


def p_var(p):
    '''var : type_aux ID n_add_var array_dim var_aux SEMICOLON
           | type_aux ID n_add_var array_dim SEMICOLON
           | type_aux ID n_add_var var_aux SEMICOLON
           | type_aux ID n_add_var SEMICOLON'''


def p_type_aux(p):
    '''type_aux : GLOBAL type
                | type'''


def p_var_aux(p):
    '''var_aux : COMMA ID n_add_var array_dim var_aux
               | COMMA ID n_add_var array_dim
               | COMMA ID n_add_var var_aux
               | COMMA ID n_add_var'''


def p_statement(p):
    '''statement : statement_aux SEMICOLON
                 | statement_aux_2'''


def p_statement_aux(p):
    '''statement_aux : assignment
                     | function_call
                     | return
                     | print'''


def p_statement_aux_2(p):
    '''statement_aux_2 : if
                       | while'''


def p_type(p):
    '''type : INT n_record_last_type
            | FLOAT n_record_last_type
            | STRING n_record_last_type'''


def p_array_index(p):
    '''array_index : L_SQUARE_BRACKET expression R_SQUARE_BRACKET L_SQUARE_BRACKET expression R_SQUARE_BRACKET
                   | L_SQUARE_BRACKET expression R_SQUARE_BRACKET'''


def p_array_dim(p):
    '''array_dim : L_SQUARE_BRACKET CONST_I R_SQUARE_BRACKET L_SQUARE_BRACKET CONST_I R_SQUARE_BRACKET
                 | L_SQUARE_BRACKET CONST_I R_SQUARE_BRACKET'''


def p_assignment(p):
    '''assignment : ID array_index ASSIGN n_make_assignment expression
                  | ID array_index ASSIGN n_make_assignment read
                  | ID ASSIGN n_make_assignment expression
                  | ID ASSIGN n_make_assignment read'''


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
    '''expression : exp n_eval_exp AND n_add_operator expression
                  | exp n_eval_exp'''


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
    'block : L_KEY_BRACKET statements R_KEY_BRACKET'


def p_exp(p):
    '''exp : xp n_eval_xp OR n_add_operator exp
           | xp n_eval_xp'''


def p_xp(p):
    '''xp : x n_eval_x log_op n_add_operator x
          | x n_eval_x'''


def p_x(p):
    '''x : term n_eval_term PLUS n_add_operator x
         | term n_eval_term MINUS n_add_operator x
         | term n_eval_term'''


def p_log_op(p):
    '''log_op : NOT_EQUAL
              | EQUALS
              | GREATER
              | GREATER_EQ
              | LESS
              | LESS_EQ'''


def p_term(p):
    '''term : factor n_eval_factor TIMES n_add_operator term
            | factor n_eval_factor DIVIDE n_add_operator term
            | factor n_eval_factor'''


def p_factor(p):
    '''factor : NOT factor_aux
              | factor_aux'''


def p_factor_aux(p):
    '''factor_aux : L_PARENS expression R_PARENS
                  | PLUS const
                  | MINUS const
                  | const'''


def p_const(p):
    '''const : ID n_add_operand
             | CONST_I n_add_operand
             | CONST_F n_add_operand
             | CONST_STRING n_add_operand
             | function_call
             | array_access'''


def p_array_access(p):
    'array_access : ID array_index'

# Where the magic begins.


def p_n_start_main(p):
    'n_start_main : '
    AT.add_func('main')


def p_n_add_function_name(p):
    'n_add_function_name : '
    AT.add_func(p[-1])


def p_n_add_function_type(p):
    'n_add_function_type : '
    func = AT.get_func(AT.current_func_name)
    func.assign_return_type(p[-1])


def p_n_end_function(p):
    'n_end_function : '
    pass


def p_n_add_var(p):
    'n_add_var : '
    func = AT.get_func(AT.current_func_name)
    func.add_var(p[-1], var_type=last_var_type)


def p_n_record_last_type(p):
    'n_record_last_type : '
    global last_var_type
    last_var_type = p[-1]


def p_n_eval_exp(p):
    'n_eval_exp : '
    Q.maybe_solve_operation(['and'])


def p_n_eval_xp(p):
    'n_eval_xp : '
    Q.maybe_solve_operation(['or'])


def p_n_eval_x(p):
    'n_eval_x : '
    Q.maybe_solve_operation(['==', '!=', '<', '>', '<=', '>='])


def p_n_eval_factor(p):
    'n_eval_factor : '
    Q.maybe_solve_operation(['*', '/'])


def p_n_eval_term(p):
    'n_eval_term : '
    Q.maybe_solve_operation(['+', '-'])


def p_n_add_operand(p):
    'n_add_operand : '
    Q.add_type(types[type(p[-1]).__name__])
    Q.add_operand(p[-1])
    # Q.print_all()


def p_n_add_operator(p):
    'n_add_operator : '
    Q.add_operator(p[-1])
    # Q.print_all()

def p_n_make_assignment(p):
    'n_make_assignment : '
    pass


def p_error(p):
    print('There is an error:', p)


def parse(input):
    parser = yacc.yacc(start='program')
    parser.defaulted_states = {}

    # Check the input's syntax
    parser.parse(input)

    Q.print_all()

    return AT
    #result = parser.parse(input, tracking=True)
