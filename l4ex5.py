s=raw_input('digite uma string: ')
s2= ''
for i in range(0,len(s)):
    if s[i].lower()== 'a':
        s2 += 2*s[i]
    elif s[i].lower()== 'e':
        s2 += 2*s[i]
    elif s[i].lower()== 'i':
        s2 += 2*s[i]
    elif s[i].lower()== 'o':
        s2 += 2*s[i]
    elif s[i].lower()== 'u':
        s2 += 2*s[i]
    else:
        s2 += s[i]
print s2
