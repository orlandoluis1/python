def matriz(m):
    for i in range(0,5):
        m.append(0)
        m[i] = []
        for j in range(0,5):
            m[i].append(0)


def ide(m):
    for i in range(0,5):
        for j in range(0,5):
            if i == j:
                m[i][i] = 1

def prt(m):
    for i in range(0,5):
        for j in range(0,5):
            print m[i][j],
        print

mat = []
matriz(mat)
ide(mat)
prt(mat)
