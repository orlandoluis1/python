mat=[]
for i in range(0,3):
    mat.append(0)
    mat[i]=[]
    for j in range(0,3):
        mat[i].append(input('n: '))

for i in range(0,3):
    for j in range(0,3):
        print mat[i][j],
    print

sd=0
for i in range(0,3):
    for j in range(0,3):
        if i == j:
            sd += mat[i][j]
print "soma da diagonal principal: ", sd
            
