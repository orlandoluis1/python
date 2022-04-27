# nome: Orlando Luis Xavier Fernandes
# data: 02/06/2021

def lermat(m):
    for i in range(0,N):
        m.append(0)
        m[i]=[]
        for j in range(0,N):
            m[i].append(int(input('elem: ')))

def Vizinho1(m):
    c = 0
    for i in range(0,N-2):
        for j in range(0,N-2):
            if m[i][j] == m[i+1][j] == m[i+2][j] == m[i][j+1] == m[i][j+2] == m[i+1][j+2] == m[i+2][j+1] == m[i+2][j+2] == 1: 
                c += 1
    return c

def prtmat(m):
    print 'matriz ', N ,'x',N,':'
    for i in range(0,N):
        for j in range(0,N):
            print m[i][j],
        print

N = input('digite a matriz NxN: ')
m = []
lermat(m)
c = Vizinho1(m)
print
print "numero de elementos que os vizinhos sao iguais a 1: ", c
print
prtmat(m)
