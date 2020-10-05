
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programAND COLON COMMA CONST_F CONST_I CONST_STRING DIVIDE ELIF ELSE EQUALS FLOAT FUNCTION GREATER GREATER_EQ ID IF INT IS_EQUAL LESS LESS_EQ L_KEY_BRACKET L_PARENS L_SQUARE_BRACKET MAIN MINUS NOT NOT_EQUAL OR PLUS PRINT READ RETURN R_KEY_BRACKET R_PARENS R_SQUARE_BRACKET SEMICOLON STRING TIMES VOID WHILEprogram : program_aux mainprogram_aux : function\n                   | program_aux function\n                   | empty function : function_header function_bodymain : FUNCTION MAIN function_bodyfunction_header : FUNCTION ID L_PARENS function_header_aux R_PARENS COLON function_typefunction_header_aux : function_params\n                           | emptyfunction_body : L_KEY_BRACKET function_body_aux function_body_aux_2 R_KEY_BRACKETfunction_body_aux : function_body_aux var\n                         | emptyfunction_body_aux_2 : function_body_aux_2 statement\n                          | statementfunction_params : type ID function_params_aux function_params_aux_2function_params_aux : array_index\n                           | emptyfunction_params_aux_2 : COMMA function_params\n                            | emptyfunction_type : type\n                     | VOIDvar : type ID var_aux var_aux_2var_aux : array_dim\n               | emptyvar_aux_2 : var_aux_2 COMMA ID var_aux\n                 | emptystatement : statement_aux SEMICOLONstatement_aux : assignment\n                     | function_call\n                     | return\n                     | if\n                     | while\n                     | printtype : INT\n            | FLOAT\n            | STRINGarray_index : L_SQUARE_BRACKET expression R_SQUARE_BRACKET L_SQUARE_BRACKET expression R_SQUARE_BRACKET\n                   | L_SQUARE_BRACKET expression R_SQUARE_BRACKETarray_dim : L_SQUARE_BRACKET CONST_I R_SQUARE_BRACKET L_SQUARE_BRACKET CONST_I R_SQUARE_BRACKET\n                 | L_SQUARE_BRACKET CONST_I R_SQUARE_BRACKETassignment : ID assignment_aux EQUALS assignment_aux_2assignment_aux : array_index\n                      | emptyassignment_aux_2 : expression\n                        | readfunction_call : ID params_passreturn : RETURN expressionif : IF L_PARENS expression R_PARENS block elif elseelif : ELIF L_PARENS expression R_PARENS block elif\n            | emptyelse : ELSE block\n            | emptywhile : WHILE L_PARENS expression R_PARENS blockprint : PRINT L_PARENS print_aux R_PARENSprint_aux : CONST_STRING print_aux_2\n                 | ID print_aux_2\n                 | emptyprint_aux_2 : COMMA ID print_aux_2\n                   | COMMA CONST_STRING print_aux_2\n                   | emptyexpression : exp expression_auxexpression_aux : AND exp expression_aux\n                      | emptyread : READ IDparams_pass : L_PARENS params_pass_aux R_PARENSparams_pass_aux : expression params_pass_aux_2\n                       | emptyparams_pass_aux_2 : COMMA expression params_pass_aux_2\n                         | emptyblock : L_KEY_BRACKET statement R_KEY_BRACKETexp : xp exp_auxexp_aux : OR xp exp_aux\n               | emptyxp : x xp_auxxp_aux : log_op x\n            | emptyx : term x_auxx_aux : PLUS term x_aux\n             | MINUS term x_aux\n             | emptylog_op : NOT_EQUAL\n              | IS_EQUAL\n              | GREATER\n              | GREATER_EQ\n              | LESS\n              | LESS_EQterm : factor term_auxterm_aux : TIMES factor term_aux\n                | DIVIDE factor term_aux\n                | emptyfactor : factor_aux factor_aux_2factor_aux : NOT\n                  | emptyfactor_aux_2 : L_PARENS expression R_PARENS\n                    | factor_aux_3 constfactor_aux_3 : PLUS\n                    | MINUS\n                    | emptyconst : ID\n             | CONST_I\n             | CONST_F\n             | CONST_STRING\n             | function_call\n             | array_accessarray_access : ID array_indexempty :'
    
_lr_action_items = {'FUNCTION':([0,2,3,4,8,10,41,],[6,9,-2,-4,-3,-5,-10,]),'$end':([1,7,17,41,],[0,-1,-6,-10,]),'L_KEY_BRACKET':([5,13,24,25,26,140,141,147,148,149,186,193,],[11,11,-34,-35,-36,167,167,-7,-20,-21,167,167,]),'ID':([6,9,11,14,15,18,19,20,21,24,25,26,33,40,42,43,48,49,50,57,58,59,60,61,62,65,66,67,69,72,75,78,81,83,84,85,86,87,88,90,91,94,95,98,99,100,101,102,113,114,119,122,144,153,154,157,167,172,182,188,190,],[12,12,-106,22,-12,22,-11,-14,43,-34,-35,-36,-106,64,-13,-106,-106,-106,-27,-106,-92,-93,-106,-106,107,-106,-23,-24,-106,-93,-106,-106,-106,-81,-82,-83,-84,-85,-86,-106,-106,-106,-106,-106,134,-96,-97,-98,-22,-26,155,-106,169,172,-40,-106,22,-106,-25,-106,-39,]),'MAIN':([9,],[13,]),'INT':([11,14,15,16,19,43,65,66,67,109,113,114,151,154,172,182,190,],[-106,24,-12,24,-11,-106,-106,-23,-24,24,-22,-26,24,-40,-106,-25,-39,]),'FLOAT':([11,14,15,16,19,43,65,66,67,109,113,114,151,154,172,182,190,],[-106,25,-12,25,-11,-106,-106,-23,-24,25,-22,-26,25,-40,-106,-25,-39,]),'STRING':([11,14,15,16,19,43,65,66,67,109,113,114,151,154,172,182,190,],[-106,26,-12,26,-11,-106,-106,-23,-24,26,-22,-26,26,-40,-106,-25,-39,]),'RETURN':([11,14,15,18,19,20,42,43,50,65,66,67,113,114,154,167,172,182,190,],[-106,33,-12,33,-11,-14,-13,-106,-27,-106,-23,-24,-22,-26,-40,33,-106,-25,-39,]),'IF':([11,14,15,18,19,20,42,43,50,65,66,67,113,114,154,167,172,182,190,],[-106,34,-12,34,-11,-14,-13,-106,-27,-106,-23,-24,-22,-26,-40,34,-106,-25,-39,]),'WHILE':([11,14,15,18,19,20,42,43,50,65,66,67,113,114,154,167,172,182,190,],[-106,35,-12,35,-11,-14,-13,-106,-27,-106,-23,-24,-22,-26,-40,35,-106,-25,-39,]),'PRINT':([11,14,15,18,19,20,42,43,50,65,66,67,113,114,154,167,172,182,190,],[-106,36,-12,36,-11,-14,-13,-106,-27,-106,-23,-24,-22,-26,-40,36,-106,-25,-39,]),'L_PARENS':([12,22,33,34,35,36,48,49,57,58,59,60,61,69,72,75,78,81,83,84,85,86,87,88,90,91,94,95,98,122,134,157,177,188,],[16,48,-106,60,61,62,-106,-106,98,-92,-93,-106,-106,-106,-93,-106,-106,-106,-81,-82,-83,-84,-85,-86,-106,-106,-106,-106,-106,-106,48,-106,188,-106,]),'R_PARENS':([16,37,38,39,45,48,52,53,54,55,56,62,64,70,71,72,74,76,77,79,80,82,89,92,93,96,97,103,104,105,106,107,108,110,111,112,120,121,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,143,145,146,150,152,156,158,159,160,161,162,163,164,165,169,170,171,174,180,181,184,192,],[-106,63,-8,-9,-46,-106,-106,-106,-106,-106,-106,-106,-106,120,-106,-67,-61,-63,-71,-73,-74,-76,-77,-80,-87,-90,-91,140,141,142,-106,-106,-57,-106,-16,-17,-65,-66,-69,-38,-106,-106,-75,-106,-106,-106,-106,164,-95,-99,-100,-101,-102,-103,-104,-55,-60,-56,-15,-19,-106,-62,-72,-78,-79,-88,-89,-94,-105,-106,-106,-18,-68,-58,-59,-37,193,]),'R_KEY_BRACKET':([18,20,42,50,179,],[41,-14,-13,-27,189,]),'L_SQUARE_BRACKET':([22,43,64,124,134,154,172,],[49,68,49,157,49,173,68,]),'EQUALS':([22,44,46,47,124,184,],[-106,69,-42,-43,-38,-37,]),'SEMICOLON':([23,27,28,29,30,31,32,45,51,52,53,54,55,56,74,76,77,79,80,82,89,92,93,96,97,116,117,118,120,124,125,126,127,128,129,130,131,133,134,135,136,137,138,139,142,155,158,159,160,161,162,163,164,165,166,168,176,178,184,185,187,189,191,194,195,],[50,-28,-29,-30,-31,-32,-33,-46,-47,-106,-106,-106,-106,-106,-61,-63,-71,-73,-74,-76,-77,-80,-87,-90,-91,-41,-44,-45,-65,-38,-106,-106,-75,-106,-106,-106,-106,-95,-99,-100,-101,-102,-103,-104,-54,-64,-62,-72,-78,-79,-88,-89,-94,-105,-106,-53,-106,-50,-37,-48,-52,-70,-51,-106,-49,]),'NOT':([33,48,49,60,61,69,75,78,81,83,84,85,86,87,88,90,91,94,95,98,122,157,188,],[58,58,58,58,58,58,58,58,58,-81,-82,-83,-84,-85,-86,58,58,58,58,58,58,58,58,]),'PLUS':([33,45,48,49,55,56,57,58,59,60,61,69,72,75,78,81,83,84,85,86,87,88,90,91,93,94,95,96,97,98,120,122,124,128,129,130,131,133,134,135,136,137,138,139,157,162,163,164,165,184,188,],[-106,-46,-106,-106,90,-106,100,-92,-93,-106,-106,-106,-93,-106,-106,-106,-81,-82,-83,-84,-85,-86,-106,-106,-87,-106,-106,-90,-91,-106,-65,-106,-38,90,90,-106,-106,-95,-99,-100,-101,-102,-103,-104,-106,-88,-89,-94,-105,-37,-106,]),'MINUS':([33,45,48,49,55,56,57,58,59,60,61,69,72,75,78,81,83,84,85,86,87,88,90,91,93,94,95,96,97,98,120,122,124,128,129,130,131,133,134,135,136,137,138,139,157,162,163,164,165,184,188,],[-106,-46,-106,-106,91,-106,101,-92,-93,-106,-106,-106,-93,-106,-106,-106,-81,-82,-83,-84,-85,-86,-106,-106,-87,-106,-106,-90,-91,-106,-65,-106,-38,91,91,-106,-106,-95,-99,-100,-101,-102,-103,-104,-106,-88,-89,-94,-105,-37,-106,]),'CONST_I':([33,48,49,57,58,59,60,61,68,69,72,75,78,81,83,84,85,86,87,88,90,91,94,95,98,99,100,101,102,122,157,173,188,],[-106,-106,-106,-106,-92,-93,-106,-106,115,-106,-93,-106,-106,-106,-81,-82,-83,-84,-85,-86,-106,-106,-106,-106,-106,135,-96,-97,-98,-106,-106,183,-106,]),'CONST_F':([33,48,49,57,58,59,60,61,69,72,75,78,81,83,84,85,86,87,88,90,91,94,95,98,99,100,101,102,122,157,188,],[-106,-106,-106,-106,-92,-93,-106,-106,-106,-93,-106,-106,-106,-81,-82,-83,-84,-85,-86,-106,-106,-106,-106,-106,136,-96,-97,-98,-106,-106,-106,]),'CONST_STRING':([33,48,49,57,58,59,60,61,62,69,72,75,78,81,83,84,85,86,87,88,90,91,94,95,98,99,100,101,102,122,144,157,188,],[-106,-106,-106,-106,-92,-93,-106,-106,106,-106,-93,-106,-106,-106,-81,-82,-83,-84,-85,-86,-106,-106,-106,-106,-106,137,-96,-97,-98,-106,170,-106,-106,]),'COMMA':([43,45,52,53,54,55,56,64,65,66,67,71,74,76,77,79,80,82,89,92,93,96,97,106,107,110,111,112,113,114,120,124,125,126,127,128,129,130,131,133,134,135,136,137,138,139,154,156,158,159,160,161,162,163,164,165,169,170,172,182,184,190,],[-106,-46,-106,-106,-106,-106,-106,-106,-106,-23,-24,122,-61,-63,-71,-73,-74,-76,-77,-80,-87,-90,-91,144,144,151,-16,-17,153,-26,-65,-38,-106,-106,-75,-106,-106,-106,-106,-95,-99,-100,-101,-102,-103,-104,-40,122,-62,-72,-78,-79,-88,-89,-94,-105,144,144,-106,-25,-37,-39,]),'TIMES':([45,56,97,120,124,130,131,133,134,135,136,137,138,139,164,165,184,],[-46,94,-91,-65,-38,94,94,-95,-99,-100,-101,-102,-103,-104,-94,-105,-37,]),'DIVIDE':([45,56,97,120,124,130,131,133,134,135,136,137,138,139,164,165,184,],[-46,95,-91,-65,-38,95,95,-95,-99,-100,-101,-102,-103,-104,-94,-105,-37,]),'NOT_EQUAL':([45,54,55,56,89,92,93,96,97,120,124,128,129,130,131,133,134,135,136,137,138,139,160,161,162,163,164,165,184,],[-46,83,-106,-106,-77,-80,-87,-90,-91,-65,-38,-106,-106,-106,-106,-95,-99,-100,-101,-102,-103,-104,-78,-79,-88,-89,-94,-105,-37,]),'IS_EQUAL':([45,54,55,56,89,92,93,96,97,120,124,128,129,130,131,133,134,135,136,137,138,139,160,161,162,163,164,165,184,],[-46,84,-106,-106,-77,-80,-87,-90,-91,-65,-38,-106,-106,-106,-106,-95,-99,-100,-101,-102,-103,-104,-78,-79,-88,-89,-94,-105,-37,]),'GREATER':([45,54,55,56,89,92,93,96,97,120,124,128,129,130,131,133,134,135,136,137,138,139,160,161,162,163,164,165,184,],[-46,85,-106,-106,-77,-80,-87,-90,-91,-65,-38,-106,-106,-106,-106,-95,-99,-100,-101,-102,-103,-104,-78,-79,-88,-89,-94,-105,-37,]),'GREATER_EQ':([45,54,55,56,89,92,93,96,97,120,124,128,129,130,131,133,134,135,136,137,138,139,160,161,162,163,164,165,184,],[-46,86,-106,-106,-77,-80,-87,-90,-91,-65,-38,-106,-106,-106,-106,-95,-99,-100,-101,-102,-103,-104,-78,-79,-88,-89,-94,-105,-37,]),'LESS':([45,54,55,56,89,92,93,96,97,120,124,128,129,130,131,133,134,135,136,137,138,139,160,161,162,163,164,165,184,],[-46,87,-106,-106,-77,-80,-87,-90,-91,-65,-38,-106,-106,-106,-106,-95,-99,-100,-101,-102,-103,-104,-78,-79,-88,-89,-94,-105,-37,]),'LESS_EQ':([45,54,55,56,89,92,93,96,97,120,124,128,129,130,131,133,134,135,136,137,138,139,160,161,162,163,164,165,184,],[-46,88,-106,-106,-77,-80,-87,-90,-91,-65,-38,-106,-106,-106,-106,-95,-99,-100,-101,-102,-103,-104,-78,-79,-88,-89,-94,-105,-37,]),'OR':([45,53,54,55,56,80,82,89,92,93,96,97,120,124,126,127,128,129,130,131,133,134,135,136,137,138,139,160,161,162,163,164,165,184,],[-46,78,-106,-106,-106,-74,-76,-77,-80,-87,-90,-91,-65,-38,78,-75,-106,-106,-106,-106,-95,-99,-100,-101,-102,-103,-104,-78,-79,-88,-89,-94,-105,-37,]),'AND':([45,52,53,54,55,56,77,79,80,82,89,92,93,96,97,120,124,125,126,127,128,129,130,131,133,134,135,136,137,138,139,159,160,161,162,163,164,165,184,],[-46,75,-106,-106,-106,-106,-71,-73,-74,-76,-77,-80,-87,-90,-91,-65,-38,75,-106,-75,-106,-106,-106,-106,-95,-99,-100,-101,-102,-103,-104,-72,-78,-79,-88,-89,-94,-105,-37,]),'R_SQUARE_BRACKET':([45,52,53,54,55,56,73,74,76,77,79,80,82,89,92,93,96,97,115,120,124,125,126,127,128,129,130,131,133,134,135,136,137,138,139,158,159,160,161,162,163,164,165,175,183,184,],[-46,-106,-106,-106,-106,-106,124,-61,-63,-71,-73,-74,-76,-77,-80,-87,-90,-91,154,-65,-38,-106,-106,-75,-106,-106,-106,-106,-95,-99,-100,-101,-102,-103,-104,-62,-72,-78,-79,-88,-89,-94,-105,184,190,-37,]),'COLON':([63,],[109,]),'READ':([69,],[119,]),'VOID':([109,],[149,]),'ELIF':([166,189,194,],[177,-70,177,]),'ELSE':([166,176,178,189,194,195,],[-106,186,-50,-70,-106,-49,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'program_aux':([0,],[2,]),'function':([0,2,],[3,8,]),'empty':([0,11,16,22,33,43,48,49,52,53,54,55,56,57,60,61,62,64,65,69,71,75,78,81,90,91,94,95,98,106,107,110,122,125,126,128,129,130,131,156,157,166,169,170,172,176,188,194,],[4,15,39,47,59,67,72,59,76,79,82,92,96,102,59,59,108,112,114,59,123,59,59,59,59,59,59,59,59,145,145,152,59,76,79,92,92,96,96,123,59,178,145,145,67,187,59,178,]),'function_header':([0,2,],[5,5,]),'main':([2,],[7,]),'function_body':([5,13,],[10,17,]),'function_body_aux':([11,],[14,]),'function_body_aux_2':([14,],[18,]),'var':([14,],[19,]),'statement':([14,18,167,],[20,42,179,]),'type':([14,16,109,151,],[21,40,148,40,]),'statement_aux':([14,18,167,],[23,23,23,]),'assignment':([14,18,167,],[27,27,27,]),'function_call':([14,18,99,167,],[28,28,138,28,]),'return':([14,18,167,],[29,29,29,]),'if':([14,18,167,],[30,30,30,]),'while':([14,18,167,],[31,31,31,]),'print':([14,18,167,],[32,32,32,]),'function_header_aux':([16,],[37,]),'function_params':([16,151,],[38,171,]),'assignment_aux':([22,],[44,]),'params_pass':([22,134,],[45,45,]),'array_index':([22,64,134,],[46,111,165,]),'expression':([33,48,49,60,61,69,98,122,157,188,],[51,71,73,103,104,117,132,156,175,192,]),'exp':([33,48,49,60,61,69,75,98,122,157,188,],[52,52,52,52,52,52,125,52,52,52,52,]),'xp':([33,48,49,60,61,69,75,78,98,122,157,188,],[53,53,53,53,53,53,53,126,53,53,53,53,]),'x':([33,48,49,60,61,69,75,78,81,98,122,157,188,],[54,54,54,54,54,54,54,54,127,54,54,54,54,]),'term':([33,48,49,60,61,69,75,78,81,90,91,98,122,157,188,],[55,55,55,55,55,55,55,55,55,128,129,55,55,55,55,]),'factor':([33,48,49,60,61,69,75,78,81,90,91,94,95,98,122,157,188,],[56,56,56,56,56,56,56,56,56,56,56,130,131,56,56,56,56,]),'factor_aux':([33,48,49,60,61,69,75,78,81,90,91,94,95,98,122,157,188,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'var_aux':([43,172,],[65,182,]),'array_dim':([43,172,],[66,66,]),'params_pass_aux':([48,],[70,]),'expression_aux':([52,125,],[74,158,]),'exp_aux':([53,126,],[77,159,]),'xp_aux':([54,],[80,]),'log_op':([54,],[81,]),'x_aux':([55,128,129,],[89,160,161,]),'term_aux':([56,130,131,],[93,162,163,]),'factor_aux_2':([57,],[97,]),'factor_aux_3':([57,],[99,]),'print_aux':([62,],[105,]),'function_params_aux':([64,],[110,]),'var_aux_2':([65,],[113,]),'assignment_aux_2':([69,],[116,]),'read':([69,],[118,]),'params_pass_aux_2':([71,156,],[121,174,]),'const':([99,],[133,]),'array_access':([99,],[139,]),'print_aux_2':([106,107,169,170,],[143,146,180,181,]),'function_type':([109,],[147,]),'function_params_aux_2':([110,],[150,]),'block':([140,141,186,193,],[166,168,191,194,]),'elif':([166,194,],[176,195,]),'else':([176,],[185,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program_aux main','program',2,'p_program','parser.py',11),
  ('program_aux -> function','program_aux',1,'p_program_aux','parser.py',15),
  ('program_aux -> program_aux function','program_aux',2,'p_program_aux','parser.py',16),
  ('program_aux -> empty','program_aux',1,'p_program_aux','parser.py',17),
  ('function -> function_header function_body','function',2,'p_function','parser.py',21),
  ('main -> FUNCTION MAIN function_body','main',3,'p_main','parser.py',25),
  ('function_header -> FUNCTION ID L_PARENS function_header_aux R_PARENS COLON function_type','function_header',7,'p_function_header','parser.py',29),
  ('function_header_aux -> function_params','function_header_aux',1,'p_function_header_aux','parser.py',33),
  ('function_header_aux -> empty','function_header_aux',1,'p_function_header_aux','parser.py',34),
  ('function_body -> L_KEY_BRACKET function_body_aux function_body_aux_2 R_KEY_BRACKET','function_body',4,'p_function_body','parser.py',38),
  ('function_body_aux -> function_body_aux var','function_body_aux',2,'p_function_body_aux','parser.py',42),
  ('function_body_aux -> empty','function_body_aux',1,'p_function_body_aux','parser.py',43),
  ('function_body_aux_2 -> function_body_aux_2 statement','function_body_aux_2',2,'p_function_body_aux2','parser.py',47),
  ('function_body_aux_2 -> statement','function_body_aux_2',1,'p_function_body_aux2','parser.py',48),
  ('function_params -> type ID function_params_aux function_params_aux_2','function_params',4,'p_function_params','parser.py',52),
  ('function_params_aux -> array_index','function_params_aux',1,'p_function_params_aux','parser.py',56),
  ('function_params_aux -> empty','function_params_aux',1,'p_function_params_aux','parser.py',57),
  ('function_params_aux_2 -> COMMA function_params','function_params_aux_2',2,'p_function_params_aux_2','parser.py',61),
  ('function_params_aux_2 -> empty','function_params_aux_2',1,'p_function_params_aux_2','parser.py',62),
  ('function_type -> type','function_type',1,'p_function_type','parser.py',66),
  ('function_type -> VOID','function_type',1,'p_function_type','parser.py',67),
  ('var -> type ID var_aux var_aux_2','var',4,'p_var','parser.py',70),
  ('var_aux -> array_dim','var_aux',1,'p_var_aux','parser.py',74),
  ('var_aux -> empty','var_aux',1,'p_var_aux','parser.py',75),
  ('var_aux_2 -> var_aux_2 COMMA ID var_aux','var_aux_2',4,'p_var_aux_2','parser.py',79),
  ('var_aux_2 -> empty','var_aux_2',1,'p_var_aux_2','parser.py',80),
  ('statement -> statement_aux SEMICOLON','statement',2,'p_statement','parser.py',83),
  ('statement_aux -> assignment','statement_aux',1,'p_statement_aux','parser.py',87),
  ('statement_aux -> function_call','statement_aux',1,'p_statement_aux','parser.py',88),
  ('statement_aux -> return','statement_aux',1,'p_statement_aux','parser.py',89),
  ('statement_aux -> if','statement_aux',1,'p_statement_aux','parser.py',90),
  ('statement_aux -> while','statement_aux',1,'p_statement_aux','parser.py',91),
  ('statement_aux -> print','statement_aux',1,'p_statement_aux','parser.py',92),
  ('type -> INT','type',1,'p_type','parser.py',96),
  ('type -> FLOAT','type',1,'p_type','parser.py',97),
  ('type -> STRING','type',1,'p_type','parser.py',98),
  ('array_index -> L_SQUARE_BRACKET expression R_SQUARE_BRACKET L_SQUARE_BRACKET expression R_SQUARE_BRACKET','array_index',6,'p_array_index','parser.py',102),
  ('array_index -> L_SQUARE_BRACKET expression R_SQUARE_BRACKET','array_index',3,'p_array_index','parser.py',103),
  ('array_dim -> L_SQUARE_BRACKET CONST_I R_SQUARE_BRACKET L_SQUARE_BRACKET CONST_I R_SQUARE_BRACKET','array_dim',6,'p_array_dim','parser.py',107),
  ('array_dim -> L_SQUARE_BRACKET CONST_I R_SQUARE_BRACKET','array_dim',3,'p_array_dim','parser.py',108),
  ('assignment -> ID assignment_aux EQUALS assignment_aux_2','assignment',4,'p_assignment','parser.py',112),
  ('assignment_aux -> array_index','assignment_aux',1,'p_assignment_aux','parser.py',116),
  ('assignment_aux -> empty','assignment_aux',1,'p_assignment_aux','parser.py',117),
  ('assignment_aux_2 -> expression','assignment_aux_2',1,'p_assigmnent_aux_2','parser.py',121),
  ('assignment_aux_2 -> read','assignment_aux_2',1,'p_assigmnent_aux_2','parser.py',122),
  ('function_call -> ID params_pass','function_call',2,'p_function_call','parser.py',126),
  ('return -> RETURN expression','return',2,'p_return','parser.py',130),
  ('if -> IF L_PARENS expression R_PARENS block elif else','if',7,'p_if','parser.py',134),
  ('elif -> ELIF L_PARENS expression R_PARENS block elif','elif',6,'p_elif','parser.py',138),
  ('elif -> empty','elif',1,'p_elif','parser.py',139),
  ('else -> ELSE block','else',2,'p_else','parser.py',143),
  ('else -> empty','else',1,'p_else','parser.py',144),
  ('while -> WHILE L_PARENS expression R_PARENS block','while',5,'p_while','parser.py',148),
  ('print -> PRINT L_PARENS print_aux R_PARENS','print',4,'p_print','parser.py',152),
  ('print_aux -> CONST_STRING print_aux_2','print_aux',2,'p_print_aux','parser.py',156),
  ('print_aux -> ID print_aux_2','print_aux',2,'p_print_aux','parser.py',157),
  ('print_aux -> empty','print_aux',1,'p_print_aux','parser.py',158),
  ('print_aux_2 -> COMMA ID print_aux_2','print_aux_2',3,'p_print_aux_2','parser.py',162),
  ('print_aux_2 -> COMMA CONST_STRING print_aux_2','print_aux_2',3,'p_print_aux_2','parser.py',163),
  ('print_aux_2 -> empty','print_aux_2',1,'p_print_aux_2','parser.py',164),
  ('expression -> exp expression_aux','expression',2,'p_expression','parser.py',168),
  ('expression_aux -> AND exp expression_aux','expression_aux',3,'p_expression_aux','parser.py',172),
  ('expression_aux -> empty','expression_aux',1,'p_expression_aux','parser.py',173),
  ('read -> READ ID','read',2,'p_read','parser.py',177),
  ('params_pass -> L_PARENS params_pass_aux R_PARENS','params_pass',3,'p_params_pass','parser.py',181),
  ('params_pass_aux -> expression params_pass_aux_2','params_pass_aux',2,'p_params_pass_aux','parser.py',185),
  ('params_pass_aux -> empty','params_pass_aux',1,'p_params_pass_aux','parser.py',186),
  ('params_pass_aux_2 -> COMMA expression params_pass_aux_2','params_pass_aux_2',3,'p_params_pass_aux_2','parser.py',190),
  ('params_pass_aux_2 -> empty','params_pass_aux_2',1,'p_params_pass_aux_2','parser.py',191),
  ('block -> L_KEY_BRACKET statement R_KEY_BRACKET','block',3,'p_block','parser.py',195),
  ('exp -> xp exp_aux','exp',2,'p_exp','parser.py',199),
  ('exp_aux -> OR xp exp_aux','exp_aux',3,'p_exp_aux','parser.py',203),
  ('exp_aux -> empty','exp_aux',1,'p_exp_aux','parser.py',204),
  ('xp -> x xp_aux','xp',2,'p_xp','parser.py',208),
  ('xp_aux -> log_op x','xp_aux',2,'p_xp_aux','parser.py',212),
  ('xp_aux -> empty','xp_aux',1,'p_xp_aux','parser.py',213),
  ('x -> term x_aux','x',2,'p_x','parser.py',217),
  ('x_aux -> PLUS term x_aux','x_aux',3,'p_x_aux','parser.py',221),
  ('x_aux -> MINUS term x_aux','x_aux',3,'p_x_aux','parser.py',222),
  ('x_aux -> empty','x_aux',1,'p_x_aux','parser.py',223),
  ('log_op -> NOT_EQUAL','log_op',1,'p_log_op','parser.py',227),
  ('log_op -> IS_EQUAL','log_op',1,'p_log_op','parser.py',228),
  ('log_op -> GREATER','log_op',1,'p_log_op','parser.py',229),
  ('log_op -> GREATER_EQ','log_op',1,'p_log_op','parser.py',230),
  ('log_op -> LESS','log_op',1,'p_log_op','parser.py',231),
  ('log_op -> LESS_EQ','log_op',1,'p_log_op','parser.py',232),
  ('term -> factor term_aux','term',2,'p_term','parser.py',236),
  ('term_aux -> TIMES factor term_aux','term_aux',3,'p_term_aux','parser.py',240),
  ('term_aux -> DIVIDE factor term_aux','term_aux',3,'p_term_aux','parser.py',241),
  ('term_aux -> empty','term_aux',1,'p_term_aux','parser.py',242),
  ('factor -> factor_aux factor_aux_2','factor',2,'p_factor','parser.py',246),
  ('factor_aux -> NOT','factor_aux',1,'p_factor_aux','parser.py',250),
  ('factor_aux -> empty','factor_aux',1,'p_factor_aux','parser.py',251),
  ('factor_aux_2 -> L_PARENS expression R_PARENS','factor_aux_2',3,'p_factor_aux_2','parser.py',255),
  ('factor_aux_2 -> factor_aux_3 const','factor_aux_2',2,'p_factor_aux_2','parser.py',256),
  ('factor_aux_3 -> PLUS','factor_aux_3',1,'p_factor_aux_3','parser.py',261),
  ('factor_aux_3 -> MINUS','factor_aux_3',1,'p_factor_aux_3','parser.py',262),
  ('factor_aux_3 -> empty','factor_aux_3',1,'p_factor_aux_3','parser.py',263),
  ('const -> ID','const',1,'p_const','parser.py',267),
  ('const -> CONST_I','const',1,'p_const','parser.py',268),
  ('const -> CONST_F','const',1,'p_const','parser.py',269),
  ('const -> CONST_STRING','const',1,'p_const','parser.py',270),
  ('const -> function_call','const',1,'p_const','parser.py',271),
  ('const -> array_access','const',1,'p_const','parser.py',272),
  ('array_access -> ID array_index','array_access',2,'p_array_access','parser.py',276),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',281),
]
