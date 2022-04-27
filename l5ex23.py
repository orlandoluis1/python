def matriz(m):
    for i in range(0,I):
        m.append(0)
        m[i]=[]
        for j in range(0,J):
            m[i].append(input('n: '))
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

I = 10
J = 3
mat = []
matriz(mat)
prt(mat)
vet = []
vet = perimetro(mat)
print vet
