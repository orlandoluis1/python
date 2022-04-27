cont=0
soma=0
n=raw_input('digite seu nome: ')
while n!= 'FIM':
    s=raw_input('digite seu sexo: ')
    n1=input('digite nota1: ')
    n2=input('digite nota2: ')
    m= (n1+n2)/float(2)
    if s == 'F': 
        m= (n1+n2)/float(2)
        print 'media mulheres', m
    else:
        cont=cont+1
        soma=soma+m
    n=raw_input('digite seu nome: ')
print 'media homens', float(soma)/cont
