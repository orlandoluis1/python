s=raw_input('digite uma string: ')
c=raw_input('digite um caracter: ')
cont=0
for i in range(0,len(s)):
    if s[i] == c:
      cont+=1  
print 'quantidade de caractere:',cont
