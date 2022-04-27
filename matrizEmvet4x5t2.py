mat=[]
for i in range(0,4):
    mat.append(0)
    mat[i]=[]
    for j in range(0,5):
        mat[i].append(input('n: '))

for i in range(0,4):
    for j in range(0,5):
        print '%4d' % mat[i][j],
    print
print

vet = [0]*20
for i in range(0,4):
    for j in range(0,5):
       vet[5*i + j] = mat[i][j]
print 'vetor: ',vet
