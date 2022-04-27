def matriz(m):
    for i in range(0,3):
        m.append(0)
        m[i] = []
        for j in range(0,3):
            m[i].append(int(input('n: ')))

def prt(m):
    for i in range(0,3):
        for j in range(0,3):
            print '%3d'% m[i][j],
        print
    print
def sdpesds(m):
    sdp=0
    for i in range(0,3):
        sdp += m[i][i]
    print 'soma diagonal principal:',sdp
    sds=0
    for i in range(0,3):
        for j in range(0,3):
            if i + j == 2:
                sds += m[i][j]
    print 'soma diagonal secundaria:', sds

mat = []
matriz(mat)
prt(mat)
sdpesds(mat)
