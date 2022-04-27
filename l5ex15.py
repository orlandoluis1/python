def matriz(m):
    for i in range(0,5):
        m.append(0)
        m[i]=[]
        for j in range(0,5):
            m[i].append(input('elem: '))

def maiorelem(m):
    maior = -1
    for i in range(0,5):
        for j in range(0,5):
            if maior < m[i][j]:
                maior = m[i][j]
    return maior

def lcm(m,maior):
    for i in range(0,5):
        for j in range(0,5):
            if maior == m[i][j]:
                print 'm[i][j]', i,'',j,'', 'maior elem',maior

mat = []
matriz(mat)
print
m = maiorelem(mat)
lcm(mat,m)

    
