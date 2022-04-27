#nome: Orlando Luis Xavier Fernandes
#data: 19/05/2021

def matriz(m):
    for i in range(0,I):
        m.append(0)
        m[i]=[]
        for j in range(0,J):
            m[i].append(input('lado: '))
    print
def prt(m):
    for i in range(0,I):
        for j in range(0,J):
            print '%3d'% m[i][j],
        print
    print

def perimetro(m):
    v = [0]* I
    for i in range(0,I):
        p2 = 0
        for j in range(0,J):
            p2 += m[i][j]
        v[i] = p2
    return v

def somacolunas(m):
    v2 = [0] * J 
    for j in range(0,J):
        sc = 0
        for i in range(0,I):
            sc += m[i][j]
        v2[j] = sc
    return v2


I = 5
J = 4
mat = []
matriz(mat)
prt(mat)
vet = []
vet = perimetro(mat)
vet2 = []
vet2 = somacolunas(mat)
print 'perimetro dos quadrados: ',vet
print
print 'soma das colunas: ',vet2
