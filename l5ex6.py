def lervet(v):
    v = [0]*40
    for i in range(0,40):
        v[i]= input('n:')
    return v

def contpar(v):
    c = 0
    for i in range(0,40):
        if v[i]%2 == 0:
            c += 1
    return c

vet = []
vet = lervet(vet)

contp = contpar(vet)

print ' a qtd d elem pares no vet: ', contp
