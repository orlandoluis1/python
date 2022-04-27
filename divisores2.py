n=input('digite um numero: ')
divisores=0
for i in range(1,n+1):
    if n%i==0:
        divisores+=1
        print i,
print
print 'o numero de divisores de ', n, ' e: ', divisores

