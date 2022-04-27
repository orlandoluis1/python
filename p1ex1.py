# nome: Orlando Luis Xavier Fernandes
# data: 14/04/2021
xy= 0
zw = 0
for b in range(1000,10000):
    xy= b // 100
    zw= b % 100
    if b == (xy+zw)**2:
        print 'numero igual a soma ao quadrado: ', b
for j in range(1000,10000):
        soma = 0
        for h in range (1,(j//2)+1):
            if j % h == 0:
                soma = soma + h
        if soma == j:
            print 'numeros perfeitos: ' , j
for i in range (1000,10000):
    for x in range(1,10000):
        if i== x*(x+1)*(x+2):
            print 'numeros triangulares: ',(i),' = ', (x) , ' * ', (x+1), ' * ', (x+2)
    
