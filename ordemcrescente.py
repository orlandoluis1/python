n1= input('digite um numero: ')
n2= input('digite um numero: ')
n3= input('digite um numero: ')
menor= 9999
meio = 0
maior = 0
if maior < n1:
    maior= n1
if maior < n2:
    maior = n2
if maior < n3:
    maior= n3
if menor >= n1:
    menor= n1
if menor >= n2:
    menor= n2
if menor >= n3:
    menor= n3
if maior == n3 and menor == n1:
    meio= n2
elif maior == n1 and menor == n3:
    meio = n2
elif maior == n2 and menor== n3:
    meio = n1
elif maior == n3 and menor== n2:
    meio = n1
elif maior == n1 and menor == n2:
    meio = n3    
else:
    if maior == n2 and menor == n1:
        meio = n3
print 'ordem crescente: ', menor, meio, maior
