s=0
vet=[]
for i in range(0,5):
    vet.append(input('n: '))
print 'vet: ', vet

for i in range (0,4):
    for j in range(i+1,5):
        if vet[i] > vet[j]:
            aux = vet[i]
            vet[i]= vet[j]
            vet[j]= aux
print 'vet ordenado: ', vet
