mat=[]
for i in range(0,3):
    mat.append(0)
    mat[i]=[]
    for j in range(0,3):
        mat[i].append(input('n: '))
print
for i in range(0,3):
    for j in range(0,3):
        print mat[i][j],
    print

mat2=[]
for i in range(0,3):
    mat2.append(0)
    mat2[i]=[]
    for j in range(0,3):
        mat2[i].append(input('n: '))
print
for i in range(0,3):
    for j in range(0,3):
        print mat2[i][j],
    print

sdp=0
for i in range(0,3):
    sdp += mat[i][i]

sds=0
for i in range(0,3):
    for j in range(0,3):
        if i + j == 2:
            sds += mat2[i][j]
print
vet = [0]*2
vet[0] = sdp
vet[1] = sds
print vet
