import ply.lex as lex
import ply.yacc as yacc

tokens = ['ID', 
          'ASSIGN', 
          'NUM', 
          'PLUS',
          'MINUS', 
          'TIMES', 
          'DIVIDE',
          'LPAREN', 
          'RPAREN', 
          'NEGATION', 
          'INTERROG',
          'NEWLINE']

t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NEGATION = r'\!'
t_INTERROG = r'\?'

def t_ID(t):
    r'[a-zA-Z]+'
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Caractere ilegal: '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_expression(p):
    '''expression : 
                  | expression NEWLINE
                  | expression expression_body
                  | expression_body'''
    if len(p) > 1:
        p[0] = ' '.join(str(x) for x in p[1:] if isinstance(x, str))

def p_expression_body(p):
    '''expression_body : ID
                       | NUM
                       | INTERROG expression
                       | NEGATION expression
                       | MINUS expression
                       | ASSIGN expression 
                       | TIMES expression 
                       | PLUS expression 
                       | DIVIDE expression
                       | LPAREN expression RPAREN'''
    if len(p) > 1:
        p[0] = ' '.join(str(x) for x in p[1:] if isinstance(x, str))

def p_error(p):
    if p:
        print("Erro de sintaxe em '%s'" % p.value)
    else:
        print("Erro de sintaxe no final da entrada")

parser = yacc.yacc()

entrada = '''
        ?a
        b=a*2/(27-3)
        !a+b
        c=a*b/'''

resultado = parser.parse(entrada)
if resultado is None:
    print("Nenhuma expressão válida encontrada na entrada.")
else:
    print(resultado)