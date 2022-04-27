def matriz(m):
    for i in range(0,4):
        m.append(0)
        m[i] = []
        for j in range(0,4):
            m[i].append(int(input('n: ')))

def prt(m):
    for i in range(0,4):
        for j in range(0,4):
            print '%3d'% m[i][j],
        print
    print
def sdptsds(m):
    aux = 0
    for i in range(0,4):
            aux = m[i][i]
            m[i][i] = m[4-i-1][i]
            m[4-i-1][i] = aux


mat = []
matriz(mat)
prt(mat)
sdptsds(mat)
prt(mat)
