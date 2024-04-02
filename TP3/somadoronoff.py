import re

texto = "Vamos começar com alguns números simples. Aqui estão alguns exemplos: 123, 456 e  = 789. On Agora, vamos adicionar alguns números maiores, como 1000, 2000 e 3000. OffIsso significa que esses números não serão somados. Mas não se preocupe, ainda temos mais números para adicionar! Vamos incluir agora alguns números decimais, como 3 e 2. OnE vamos adicionar alguns números negativos também, como 15, -10 e -20 = . OffEsses também não serão somados. Vamos continuar! On Aqui estão mais alguns números: off 5000, = 6000 e 7000. OffAgora, vamos desativar o somador por um momento. OffIsso significa que os próximos números não serão somados. Mas não se preocupe, ativaremos novamente em breve. On Agora, alguns números =  adicionais: 8000, 9000 e 10000. OnE para um toque final, vamos adicionar alguns números aleatórios: 42, 99 e  off 777. Off Espero que e45 ste texto seja útil para 67 testar seu programa. Boa sorte!"

def somadoronoff(texto): 
    contador = 0
    result = []
    result = re.findall(r'on(.[^off]*)|(=)',texto,re.IGNORECASE)
    result = ["".join(filter(None, item)) for item in result]
    truelist =[]
    
    for i in result: 
        igual = re.search(r'.+=', i)
        if igual is not None:
            x = re.findall(r'([^=]+)(=)(.+)', i, re.IGNORECASE)
            for a in x:
                truelist.extend(a)
                x = re.findall(r'([^=]+)(=)(.+)', i, re.IGNORECASE)
        else:
            truelist.append(i)
    
    for f in truelist:
        p = re.search(r'=',f)
        if p:
            print(contador)
        else: 
            numeros = re.findall(r'\d+',f)
            contador += sum(map(int,numeros))
    return contador

print(somadoronoff(texto))