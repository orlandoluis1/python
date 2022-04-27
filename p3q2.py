#nome: orlando luis xavier fernandes
#data: 19/05/2021

def lermat(m):
    for i in range(0,N):
        m.append(0)
        m[i]=[]
        for j in range(0,N):
            m[i].append(input('elem: '))
    print

def quadradomagico(m):
    q = False
    sdp = 0
    sds = 0
    for i in range(0,N):
        sl = 0
        sc = 0
        sdp += m[i][i]
        sds += m[N-i-1][i]
        for j in range(0,N):
            sl += m[i][j]
            sc += m[j][i]
    if sl == sc and sdp == sds and sl == sdp:
        q = True
    return q

N = input('Matriz N x N :')
mat = []
lermat(mat)
qm = quadradomagico(mat)
print 'a matriz N x N : ',
if qm:
    print 'quadradro magico'
else:
    print 'nao e um quadradro magico'

