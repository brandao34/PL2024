import json
import ply.lex as lex
import re
with open('jsoninput.json', 'r') as jsoninput:
    data = json.load(jsoninput)

print(data)
saldo = 0
numero = 0 
somar = 0 
tokens = ("LISTAR", 'MOEDA', 'SELECIONAR','NUMBER', 'MULTIPLICADOR', 'COMA', 'END')

def t_END(t):
    r'\.'
    global saldo
    print("maq: Saldo =", saldo)

def t_LISTAR(t):
    r'LISTAR'
    print("mac:")
    print("cod  |nome   |quant  |preço  |")
    print("---------------------------------")
    stock_item = data['stock'][0]
    print(stock_item['cod'], stock_item['nome'], stock_item['quant'], stock_item['preco'])

def t_MOEDA(t):
    r'MOEDA'
    # Capture the entire line
    line = t.lexer.lexdata.splitlines()[t.lexer.lineno - 1]
    print("Captured line:", line)
    #t.lexer.skip(len(line) - len(t.value))

    #match = re.match(r'(MOEDA) ([(\d+)(\w),\s]*)', line)
#
    #if match:
    #    items = [item.strip() for item in match.group(2).split(',')]
    #    print(items)
    #else:
    #    print("Invalid MOEDA line")
#
    ## Skip the remaining characters in the line
    #t.lexer.skip(len(line) - len(t.value))

def t_VALOR(t):
    r'\d+'
    t.value = int(t.value)  
    global numero
    numero = t.value 
    

def t_MULTIPLICADOR(t):
    r'e|c'
    global numero
    global saldo

    if t.value == 'e': 

        saldo += numero
        numero = 0
    else: 
        saldo +=numero * 0.01
    

def t_SELECIONAR(t):
    r'SELECIONAR'
    print("Sucesso")


def t_COMA(t):
    r','
# Defaults
# Newline
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Spaces
t_ignore = ' \t'

# Errors
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

while True:
    user_input = input("Enter expression (or 'SAIR' to exit): ")
    if user_input == 'SAIR':
        print("Até à próxima")
        break

    lexer.input(user_input)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
