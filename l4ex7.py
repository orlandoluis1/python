s=raw_input('digite uma string: ')
s2=raw_input('digite outra string: ')
aux = ''
for i in range(0,len(s)):
    for j in range (0,len(s2)):
        if s[i] == s2[j]:
            repetido = False 
            for k in range (0,len(aux)):
                if s[i] == aux [k]:
                    repetido = True
            if not repetido:
                aux += s[i]
                print s[i],
