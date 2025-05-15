import ply.lex as lex

tokens = (
    'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQUALS', 'SEMICOLON', 'PRINT'
)

reserved = {'print': 'PRINT'}

t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_EQUALS    = r'='
t_SEMICOLON = r';'
t_ignore    = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    raise SyntaxError(f"Caracter ilegal: {t.value[0]}")

lexer = lex.lex()
