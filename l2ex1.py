
vet = [0]*3
for i in range(0,3):
    vet[i] = input('n:')
print vet
for i in range(0,3):
    aux = 0
    for j in range(i,3):
        if vet[i] > vet[j]:
            aux = vet[i]
            vet[i] = vet[j]
            vet[j] = aux
print vet
