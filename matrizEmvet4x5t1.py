mat=[]
for i in range(0,4):
    mat.append(0)
    mat[i]=[]
    for j in range(0,5):
        mat[i].append(input('n: '))

for i in range(0,4):
    for j in range(0,5):
        print mat[i][j],
    print
print

vet = [0]*20
ind = 0
for i in range(0,4):
    for j in range(0,5):
       vet[ind] = mat[i][j]
       ind += 1
print 'vetor: ',vet
