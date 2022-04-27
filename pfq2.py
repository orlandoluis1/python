# nome: Orlando Luis Xavier Fernandes
# data: 02/06/2021

def cadencaixa(a,b):
    comeco = False
    final = False
    maior =''
    if len(a)>len(b) and b in a:
        for i in range(len(b)):
            if a[i] == b[i]:
                comeco = True
            else:
                if a[-i] == b[-i]:
                    final = True
                    maior = a
    if len(b)>len(a) and a in b:
        for j in range(len(a)):
            if a[j] == b[j]:
                comeco = True
            else:
                if a[-j] == b[-j]:
                    final = True
                    maior = b
    if len(a) == len(b):
        for k in range(len(m)):
            if a[k] == b[k]:
                comeco = True
            else:
                if a[-k] == b[-k]:
                    final = True
                    maior = b
                    
    r = -2
    if comeco == True:
        r = 0
    if final == True:
        r = len(maior)
    if comeco == False and final == False:
        r = -1
    return r
        
a = raw_input('digite uma cadeia: ')
b = raw_input('digite uma cadeia: ')
print
r = cadencaixa(a,b)
print r
