mat=[]
s=0
for i in range(0,3):
    mat.append(0)
    mat[i]=[]
    for j in range(0,3):
        mat[i].append(input('n: '))
print mat

for i in range(0,3):
    for j in range(0,3):
        if mat[i][j] % 2 == 0:
            s += mat[i][j]
print s
