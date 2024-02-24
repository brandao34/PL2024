import re

texto = "sadoffjaposdj11asdabonsdl10sadldn=akd34sdaloffdasd=ad4er45adsadawdonedadsdO5nefSDdaoffdadna=dnadadsadonmailDhsadpjAd32opjAdjaSfasf"

def somadoronoff(texto): 
    contador = 0
    result = []
    result = re.findall(r'on(.[^off]*)|(=)',texto,re.IGNORECASE)
    result = ["".join(filter(None, item)) for item in result]
    truelist =[]
    
    for i in result: 
        igual = re.search(r'.+=',i)
        if igual!=None:
            x = re.findall(r'([^=]+)(=)(.+)',i, re.IGNORECASE)
            for a in x:
                truelist.extend(a)
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