def matriz(m):
    c = 0
    for i in range(0,4):
        m.append(0)
        m[i] = []
        for j in range(0,4):
            m[i].append(c)
            c += 1

def prt(m):
    for i in range(0,4):
        for j in range(0,4):
            print '%3d'% m[i][j],
        print
    print

def troca(m):
    for i in range(0,4):
        for j in range(0,4):
            if i == 1:
                m[i][j] = m[j] [3]
mat = []
matriz(mat)
prt(mat)
troca(mat)
prt (mat)
