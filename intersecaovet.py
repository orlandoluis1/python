vet1 = [0]* 5
vet2 = [0] * 5
for i in range (0,5):
    n1 = input('digite n1: ')
    vet1[i]= n1
for i in range (0,5):
    n2 = input('digite n2: ')
    vet2[i]= n2
for k in range(0,5):
    for j in range (0,5):
        if vet1[k] == vet2[j]:
            print vet1[i]
