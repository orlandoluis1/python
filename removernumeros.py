s=raw_input('digite uma string: ')
s2= ''
for i in range(0,len(s)):
    if s[i].isdigit() == False:
        s2 += s[i]
print s2
