f= raw_input('frase: ')
contv = 0
contb = 0
cont = 0
for i in range(0,len(f)):
    if f[i] == ' ':
        contb += 1
    elif f[i].lower() == 'a' or f[i].lower() == 'e' or f[i].lower() == 'i' or f[i].lower() == 'o' or f[i].lower() == 'u':
        contv += 1
    else:
        cont += 1

vet = []
vet.append(contb)
vet.append(contv)
vet.append(cont)

print 'qtd branco,qtb vogais e qtd resto: ', vet
