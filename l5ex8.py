def lervet(v):
    v = [0]*15
    for i in range(0,15):
        v[i]= input('n:')
    return v

def somaedif(v,v1):
    v2 = [0]*2
    for i in range(0,15):
        v2[0] += v[i] + v1[i]
        v2[1] += v[i] - v1[i]
    return v2

vet1 = []
vet2 = []
vet = []

vet1 = lervet(vet1)
vet2 = lervet(vet2)
vet = somaedif(vet1,vet2)

print 'vet1: ',vet1
print 'vet2: ',vet2
print
print 'soma dos elementos e diferenca dos elementos: ', vet
