s=raw_input('digite uma string: ')
s2=''
if len(s)%2== 0:
    for i in range(0,len(s),2):
        s2 += s[i+1]+s[i]
else:
    for i in range(0,len(s)-1,2):
        s2 += s[i+1]+s[i]
    s2 = s2 + s[len(s)-1]
print s2
