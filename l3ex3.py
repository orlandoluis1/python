n = float(input('digite um numero: '))
m = 0
contp = 0
conti = 0
sp = 0
while n != 0:
    if n%2== 0:
        contp += 1
        sp += n
        m = sp/contp
    else:
        conti += 1
    n = input('digite um numero: ')
print 'qtd pares: ',contp ,'media pares: ', m
print 'qtd impares: ', conti
