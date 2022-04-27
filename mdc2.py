n = int(input("Digite o valor de n (n > 0): "))
m = int(input("Digite o valor de m (m > 0): "))
mdc = int(input('digite o mdc: '))
for x in range(-mdc,mdc):
    for y in range(-mdc,mdc):
        if mdc == (x*n) + (y*m):
            print x , y
else:
    print 'nao achou'
