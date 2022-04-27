vet = []
for i in range(0,30):
    vet.append(input('n: '))
print '-----'

x = input('x: ')
cx=0
for i in range(0,30):
    if x == vet[i]:
        cx+=1

print 'qtd x no vet: ',cx
