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
    
def ide(m):
    x =input('x: ')
    ach = False
    for i in range(0,4):
        for j in range(0,4):
            if m[i][j] == x:
                print x , 'na pos: i,j: ', i,j
                ach = True
    if not ach:
        print 'erro'


mat = []
matriz(mat)
prt(mat)
ide(mat)
