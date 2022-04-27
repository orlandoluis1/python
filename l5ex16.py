m = []
for i in range(0,7):
    m.append(0)
    m[i] = []
    for j in range(0,7):
        m[i].append(input('elem: '))

for i in range(0,7):
    for j in range(0,7):
        print m[i][j] ,
    print
print
    
for i in range(0,7):
    for j in range(0,7):
        if i == 2 and j == 3:
            print m[i][j]
print
s6 = 0
for i in range(0,7) :
    for j in range(0,7) :
        if i ==  6:
            s6 += m[i][j]
print s6
print
s2 = 0
for i in range(0,7) :
    for j in range(0,7) :
        if j == 2:
            s2 += m[i][j]
print s2    
print
for i in range(0,7):
    print m[i][i],
print
print
s = 0
for i in range(0,7):
    for j in range(0,7):
        if m[i][j] % 2 == 0:
            s += m[i][j]
print s

