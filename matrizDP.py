mat=[]
for i in range(0,3):
    mat.append(0)
    mat[i]=[]
    for j in range(0,3):
        mat[i].append(input('n: '))

for i in range(0,3):
    for j in range(0,3):
        print '%4d'% mat[i][j],
    print

print
for i in range(0,3):
    print mat[i][i],
