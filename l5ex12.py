def lervet(v):
    for i in range(0,10):
        v[i]= input('n:')


def achI(v,v1):
    for i in range(0,10):
        aux = ''
        for j in range(0,10):
            if v[i] == v1[j]:
                aux = str(v[i])
        if aux != '':
            vi [i] = aux


def achU(v,v1):
    for i in range(0,10):
        vu[i] = str(v[i])
    for i in range(0,10):
        u = True
        aux = ''
        for j in range(0,10):
            if vu[j] == str(v1[i]):
                u = False
        if u:
            aux = str(v1[i])
        if aux !='':
            vu[i+10] = aux

v = [0]*10
lervet(v)
print
v1 = [0]*10
lervet(v1)

vu = ['']*20
achU(v,v1)

vi = ['']*10
achI(v,v1)
print
print vu
print
print vi

            
