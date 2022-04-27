def lervet(v):
    v = [0]*10
    for i in range(0,10):
        v[i]= input('n:')
    return v

def juntar(v,v1):
    v2 = [0]*20
    for i in range(0,10):
        v2[i] = v[i]
        v2[i+10]= v1[i]
    return v2

vet1 = []
vet2 = []
vet = []

vet1 = lervet(vet1)
vet2 = lervet(vet2)
vet = juntar(vet1,vet2)

print 'vet1: ',vet1
print 'vet2: ',vet2
print 'vet1 + vet2: ',vet
