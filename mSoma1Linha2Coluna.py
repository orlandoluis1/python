def matriz(m):
    m = []
    for i in range(0,lin):
        m.append(0)
        m[i]=[]
        for j in range(0,col):
            m[i].append(input('elem:'))
    return m

def somalc(m1,m2):
    aux = [0] * lin
    for i in range(0,lin):
        s = 0
        for j in range(0,col):
            s += m1[i][j] - m2[j][i]  
        aux[i] = s
    return aux

lin=5
col=5
mat1=[]
mat2=[]
mat1 = matriz(mat1)
mat2 = matriz(mat2)
print 'vetor 1 linha + 2 coluna: ', somalc(mat1,mat2)
