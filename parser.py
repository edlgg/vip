'''
VIP Parser
Authors: David Souza & Eduardo de la Garza
'''

import ply.yacc as yacc
from scanner import tokens
from Quadruples import Quadruples
from constants import Operator, operators

Q = Quadruples()


def p_program(p):  # YA ESTA
    '''program : vars functions main
               | vars main
               | functions main
               | main'''


def p_functions(p):  # YA ESTA
    '''functions : functions function
                 | function'''


def p_function(p):  # YA ESTA
    'function : function_header function_body n_end_function'


def p_main(p):  # YA ESTA
    'main : FUNCTION MAIN L_PARENS R_PARENS n_start_main function_body n_end_main'


def p_function_header(p):  # YA ESTA
    '''function_header : FUNCTION ID n_add_function_name L_PARENS function_params R_PARENS COLON function_type
                       | FUNCTION ID n_add_function_name L_PARENS R_PARENS COLON function_type'''


def p_function_body(p):  # YA ESTA
    '''function_body : L_KEY_BRACKET vars statements R_KEY_BRACKET
                     | L_KEY_BRACKET statements R_KEY_BRACKET'''


def p_vars(p):  # YA ESTA
    '''vars : var vars
            | var'''


def p_statements(p):  # YA ESTA
    '''statements : statement statements
                  | statement'''


def p_function_params(p):  # YA ESTA
    '''function_params : type ID n_add_param array_index COMMA function_params
                       | type ID n_add_param array_index
                       | type ID n_add_param COMMA function_params
                       | type ID n_add_param'''


def p_function_type(p):  # YA ESTA
    '''function_type : INT n_add_function_type
                     | FLOAT n_add_function_type
                     | STRING n_add_function_type
                     | VOID n_add_function_type'''


def p_var(p):  # YA ESTA
    '''var : type_aux var_aux n_reset_is_global SEMICOLON'''


def p_type_aux(p):  # YA ESTA
    '''type_aux : GLOBAL n_is_global type
                | type'''


def p_var_aux(p):  # YA ESTA
    '''var_aux : ID n_add_var_arr array_dim COMMA var_aux
               | ID n_add_var_arr array_dim
               | ID n_add_var COMMA var_aux
               | ID n_add_var'''


def p_statement(p):  # YA ESTA
    '''statement : statement_aux SEMICOLON
                 | statement_aux_2'''


def p_statement_aux(p):  # YA ESTA
    '''statement_aux : assignment
                     | function_call
                     | return
                     | print
                     | read'''


def p_statement_aux_2(p):  # YA ESTA
    '''statement_aux_2 : if
                       | while'''


def p_type(p):  # YA ESTA
    '''type : INT n_record_last_type
            | FLOAT n_record_last_type
            | STRING n_record_last_type'''


def p_array_dim(p):  # YA ESTA
    '''array_dim : L_SQUARE_BRACKET array_dim_aux R_SQUARE_BRACKET array_dim_2 n_array_dim_done
                 | L_SQUARE_BRACKET array_dim_aux R_SQUARE_BRACKET n_array_dim_done'''


def p_array_dim_2(p):  # YA ESTA
    '''array_dim_2 : L_SQUARE_BRACKET array_dim_aux R_SQUARE_BRACKET array_dim_2
                   | L_SQUARE_BRACKET array_dim_aux R_SQUARE_BRACKET'''


def p_array_dim_aux(p):  # YA ESTA
    '''array_dim_aux : n_create_dim_node CONST_I n_array_dim_inf_with_interval DOT DOT CONST_I n_array_dim_sup
                     | n_create_dim_node n_array_dim_inf CONST_I n_array_dim_sup'''


def p_assignment(p):  # YA ESTA
    '''assignment : ID n_start_assignment ASSIGN expression
                  | ID n_start_assignment ASSIGN read
                  | array_access ASSIGN  expression
                  | array_access ASSIGN  read'''
    Q.assign()


def p_function_call(p):  # YA ESTA
    'function_call : ID n_calling_func params_pass n_validate_function_call'


def p_return(p):  # YA ESTA
    'return : RETURN expression n_return'


def p_if(p):  # YA ESTA
    '''if : IF if_condition'''


def p_if_condition(p):  # YA ESTA
    '''if_condition : L_PARENS expression R_PARENS n_end_condition block ELIF n_start_else if_condition n_end_if
                    | L_PARENS expression R_PARENS n_end_condition block ELSE n_start_else block n_end_if
                    | L_PARENS expression R_PARENS n_end_condition block n_end_if'''


def p_while(p):  # YA ESTA
    'while : WHILE n_start_while L_PARENS expression R_PARENS n_end_condition block n_end_while'


def p_print(p):  # YA ESTA
    '''print : PRINT L_PARENS print_aux R_PARENS n_end_print
             | PRINT L_PARENS R_PARENS'''


def p_print_aux(p):  # YA ESTA
    '''print_aux : expression n_print COMMA print_aux
                 | expression n_print'''


def p_expression(p):  # YA ESTA
    '''expression : exp n_eval_exp AND n_add_operator expression
                  | exp n_eval_exp'''


def p_read(p):  # YA ESTA
    'read : READ L_PARENS ID n_register_read R_PARENS'


def p_params_pass(p):  # YA ESTA
    '''params_pass : L_PARENS expression n_validate_param params_pass_aux R_PARENS
                   | L_PARENS expression n_validate_param R_PARENS
                   | L_PARENS R_PARENS'''


def p_params_pass_aux(p):  # YA ESTA
    '''params_pass_aux : COMMA expression n_validate_param params_pass_aux
                       | COMMA expression n_validate_param'''


def p_block(p):  # YA ESTA
    'block : L_KEY_BRACKET statements R_KEY_BRACKET'


def p_exp(p):  # Ya ESTA
    '''exp : xp n_eval_xp OR n_add_operator exp
           | xp n_eval_xp'''


def p_xp(p):  # YA ESTA
    '''xp : x n_eval_x NOT_EQUAL n_add_operator xp
          | x n_eval_x EQUALS n_add_operator xp
          | x n_eval_x GREATER n_add_operator xp
          | x n_eval_x GREATER_EQ n_add_operator xp
          | x n_eval_x LESS n_add_operator xp
          | x n_eval_x LESS_EQ n_add_operator xp
          | x n_eval_x'''


def p_x(p):  # YA ESTA
    '''x : term n_eval_term PLUS n_add_operator x
         | term n_eval_term MINUS n_add_operator x
         | term n_eval_term'''


def p_term(p):  # YA ESTA
    '''term : factor n_eval_factor TIMES  n_add_operator term
            | factor n_eval_factor DIVIDE n_add_operator term
            | factor n_eval_factor'''


def p_factor(p):  # YA ESTA
    '''factor : NOT factor_aux
              | factor_aux'''


def p_factor_aux(p):  # YA ESTA
    '''factor_aux : L_PARENS n_add_operator expression n_pop_fake_bottom R_PARENS
                  | PLUS const
                  | MINUS const
                  | const'''


def p_const(p):  # YA ESTA
    '''const : ID n_add_operand
             | CONST_F n_add_operand
             | CONST_I n_add_operand
             | CONST_STRING n_add_operand
             | function_call
             | array_access'''


def p_array_access(p):  # YA ESTA
    'array_access : ID n_add_operand n_validate_is_array array_index n_pop_fake_bottom'


def p_array_index(p):  # YA ESTA
    '''array_index : L_SQUARE_BRACKET expression n_ver_index R_SQUARE_BRACKET array_index_aux'''


def p_array_index_aux(p):  # YA ESTA
    '''array_index_aux : array_index
                       | n_get_array_dir'''


############################################################################################################################
''' LADIES AND GENTLEMENT, MAKE SOME POPCORN, ORDER SOME TACOS AND BUCKLE YOUR SEATBELTS, THIS IS WHERE THE MAGIC BEGINS '''
############################################################################################################################


###
def p_n_start_main(p):
    'n_start_main : '
    Q.start_main()


def p_n_add_function_name(p):
    'n_add_function_name : '
    Q.register_func(p[-1])


def p_n_add_function_type(p):
    'n_add_function_type : '
    Q.register_func_type(p[-1])


def p_n_end_function(p):
    'n_end_function : '
    Q.end_function()


def p_n_end_main(p):
    'n_end_main : '
    Q.end_function(is_main=True)


def p_n_add_var(p):
    'n_add_var : '
    Q.add_var(p[-1])


def p_n_add_var_arr(p):
    'n_add_var_arr : '
    Q.add_var(p[-1], is_array=True)


def p_n_add_param(p):
    'n_add_param : '
    Q.add_var(p[-1], is_param=True)


def p_n_record_last_type(p):
    'n_record_last_type : '
    Q.last_var_type = p[-1]


def p_n_eval_exp(p):
    'n_eval_exp : '
    Q.maybe_solve_operation([Operator.AND])


def p_n_eval_xp(p):
    'n_eval_xp : '
    Q.maybe_solve_operation([Operator.OR])


def p_n_eval_x(p):
    'n_eval_x : '
    Q.maybe_solve_operation([Operator.EQUALS, Operator.NOT_EQUAL, Operator.LESS,
                             Operator.GREATER, Operator.LESS_EQ, Operator.GREATER_EQ])


def p_n_eval_factor(p):
    'n_eval_factor : '
    Q.maybe_solve_operation([Operator.TIMES, Operator.DIVIDE])


def p_n_eval_term(p):
    'n_eval_term : '
    Q.maybe_solve_operation([Operator.PLUS, Operator.MINUS])


def p_n_end_condition(p):
    'n_end_condition : '
    Q.register_condition()


def p_n_start_else(p):
    'n_start_else : '
    Q.register_else()


def p_n_end_if(p):
    'n_end_if : '
    Q.register_end_if()


def p_n_start_while(p):
    'n_start_while : '
    Q.register_start_while()


def p_n_end_while(p):
    'n_end_while : '
    Q.register_end_while()


def p_n_is_global(p):
    'n_is_global : '
    Q.set_is_global(True)


def p_n_reset_is_global(p):
    'n_reset_is_global : '
    Q.set_is_global(False)


def p_n_add_operand(p):
    'n_add_operand : '
    Q.add_operand(p[-1])


def p_n_add_operator(p):
    'n_add_operator : '
    Q.add_operator(operators[p[-1]])


def p_n_pop_fake_bottom(p):
    'n_pop_fake_bottom : '
    Q.pop_fake_bottom()


def p_n_start_assignment(p):
    'n_start_assignment : '
    Q.init_assignment(p[-1])


def p_n_create_dim_node(p):
    'n_create_dim_node : '
    Q.create_dim_node()


def p_n_array_dim_done(p):
    'n_array_dim_done : '
    Q.end_array_dim()


def p_n_array_dim_inf(p):
    'n_array_dim_inf : '
    Q.register_array_dim_lim_inf()


def p_n_array_dim_inf_with_interval(p):
    'n_array_dim_inf_with_interval : '
    Q.register_array_dim_lim_inf(lim_inf=p[-1])


def p_n_array_dim_sup(p):
    'n_array_dim_sup : '
    Q.register_array_dim_lim_sup(p[-1])


def p_n_get_array_dir(p):
    'n_get_array_dir : '
    Q.get_array_dir()


def p_n_ver_index(p):
    'n_ver_index : '
    Q.ver_index()


def p_n_print(p):
    'n_print : '
    Q.do_print()


def p_n_end_print(p):
    'n_end_print : '
    Q.end_print()


def p_n_return(p):
    'n_return : '
    Q.add_return()


def p_n_calling_func(p):
    'n_calling_func : '
    Q.calling_func(p[-1])


def p_n_validate_param(p):
    'n_validate_param : '
    Q.validate_param(p[-1])


def p_n_validate_function_call(p):
    'n_validate_function_call : '
    Q.validate_function_call()


def p_n_register_read(p):
    'n_register_read : '
    Q.register_read(p[-1])


def p_n_validate_is_array(p):
    'n_validate_is_array : '
    Q.validate_is_array()


def p_error(p):
    print('There is an error:', p)


def parse(input):
    parser = yacc.yacc(start='program')
    parser.defaulted_states = {}

    # Check the input's syntax
    parser.parse(input)

    Q.print_all()

    obj_code = Q.generate_obj_code()

    return obj_code
