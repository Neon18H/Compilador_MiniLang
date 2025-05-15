import ply.yacc as yacc
from lexer.lexer import tokens

def p_program(p):
    '''program : instructions'''
    p[0] = p[1]

def p_instructions(p):
    '''instructions : instructions instruction
                    | instruction'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_instruction_assign(p):
    'instruction : ID EQUALS expression SEMICOLON'
    p[0] = ('assign', p[1], p[3])

def p_instruction_print(p):
    'instruction : PRINT ID SEMICOLON'
    p[0] = ('print', p[2])

def p_expression_binop(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    p[0] = (p[2], p[1], p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_binop(p):
    '''term : term TIMES factor
            | term DIVIDE factor'''
    p[0] = (p[2], p[1], p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = ('num', p[1])

def p_factor_id(p):
    'factor : ID'
    p[0] = ('id', p[1])

def p_error(p):
    raise SyntaxError("Error de sintaxis")

parser = yacc.yacc()
