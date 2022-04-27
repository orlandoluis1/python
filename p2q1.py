#nome: orlando luis xavier fernandes
#data: 28/04/2021

palindromo = True
cad = raw_input("entre com uma cadeia: ")
aux=''
for i in range(0,len(cad)):
    if cad[i] == ' ':
        aux += ''
    else:
        aux += cad[i]
for j in range(0,len(aux)):
    if aux[j] != aux[len(aux)- j -1]:
        palindromo = False
if palindromo == True:
    print aux,' ',
