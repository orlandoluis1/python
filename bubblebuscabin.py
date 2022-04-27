s=0
vet=[]
for i in range(0,5):
    vet.append(input('n: '))


for i in range (0,4):
    for j in range(i+1,5):
        if vet[i] > vet[j]:
            aux = vet[i]
            vet[i]= vet[j]
            vet[j]= aux

elem = input("digite o n que proucura: ")

inicio = 0
fim = len(vet)- 1
achou = False
while inicio <= fim and not achou:
    meio = (inicio + fim) // 2
    if elem == vet[meio]:
        pos = meio
        achou = True
    elif elem < vet[meio]:
        fim = meio - 1
    else:
        inicio = meio + 1

if achou == True:
    print pos
else:
    print 'n achou'
        
