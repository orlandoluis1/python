mat=[]
for i in range(0,4):
    mat.append(0)
    mat[i]=[]
    for j in range(0,4):
        mat[i].append(input('n: '))

for i in range(0,4):
    for j in range(0,4):
        print mat[i][j],
    print

for i in range(0,4):
    sl=0
    for j in range(0,4):
        sl += mat[i][j]                               
    print sl ,
print

s=0
for i in range(0,4):
    for j in range(0,4):
        if mat[i][j] % 2 == 0:
            s += mat[i][j]
print s
