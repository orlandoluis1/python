#nome: orlando luis xavier fernandes
#data: 19/05/2021

def lervet(v):
    for i in range(0,K):
        v[i] = input('num inteiro: ')

def remove0novet(v):
    for i in range(0,K):
        for j in range(i+1,K):
            if v[i] == 0:
                aux = 0
                v[i] = v[j]
                v[j] = aux
    print "[", '',
    for i in range(0,K):
        if v[i] != 0:
            print v[i], '',
    print ']'

K = 20
vet = [0]* K
lervet(vet)
print vet
print
remove0novet(vet)
