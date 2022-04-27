f= raw_input('frase: ')
aux = ''
for i in range(0,len(f)):
    if f[i] == ' ':
        aux += ''
    else:
        aux += f[i]

vet =['']*len(aux)
for i in range(0,len(aux)):
    vet[i] = aux[i]
print vet
