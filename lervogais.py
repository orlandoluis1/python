s=raw_input('string: ')
s2= s.upper()
contvogais = 0
for i in range (0,len(s)):
    if s2[i] == 'A' or s2[i] == 'E' or s2[i] == 'I' or s2[i] == 'O' or s2[i] == 'U':
        contvogais += 1
print 'essa palavra tem, ', contvogais,' vogais.'
