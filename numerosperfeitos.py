n= 2
for j in range(1,10000):
    soma = 0
    for i in range (1,(n//2)+1):
        if n % i == 0:
            soma = soma + i
    if soma == n:
        print n
    n = n + 1
