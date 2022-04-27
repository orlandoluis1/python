def lervet(v):
    for i in range (0,t):
        v[i] = float(input('temp em C: '))

def CpF(v):
    for i in range(0,t):
        v[i] = (v[i]*(9/5.0)) + 32

def med(v):
    s = 0
    for i in range(0,t):
        s += v[i]
    m = s/t
    return m
def amed(v,m):
    cont = 0
    for i in range(0,t):
        if v[i] > m:
            cont += 1
    return cont

t = 50
c = [0.0]*t
lervet(c)
f = [0.0]*t
f = c
CpF(f)
mc = med(c)
mf = med(f)
caf = amed (f,mf)
print f
print
print mc , mf
print
print caf

    
