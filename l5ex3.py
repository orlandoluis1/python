vet = []
for i in range(0,16):
    vet.append(input('elem: '))

print 'vet original: ', vet
    
aux = 0
for i in range(0,8):
    aux = vet[i]
    vet[i] = vet[i+8]
    vet[i+8] = aux

print 'vet trocado: ', vet
