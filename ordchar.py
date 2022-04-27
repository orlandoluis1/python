c= raw_input('digite uma cadeia: ')
soma= 0
for i in range(0,len(c)):
    soma += ord(c[i])
print 'a soma dos valores dos caracteres e de: ', soma
