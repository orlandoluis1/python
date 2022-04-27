print("Determina o mdc de dois números n > 0 e m > 0\n")
n = int(input("Digite o valor de n (n > 0): "))
m = int(input("Digite o valor de m (m > 0): "))
mdc = 1
for i in range (2 , n+1):
    if n % i == 0 and m % i == 0:
        mdc = i 
print "MDC(",n ,",", m ,')=', mdc
for x in range(-n,n+1):
    for y in range(-m,m+1):
        if mdc == (x*n) + (y*m):
            print x , y
