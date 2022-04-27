vet = [0]*12
for i in range(0,12):
    vet[i] = input('n: ')
print '-----'
x = input('x de 1 a 12: ')
y = input('y de 1 a 12: ')
print '-----'
s = vet[x-1] + vet[y-1]
print 'soma da posicoes x e y : ', s
