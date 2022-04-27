def palin(s):
    palin = True
    for i in range(0,(len(s)//2)+1):
        if s[i] != s[len(s)- i -1]:
            palin = False
    return palin
    
cad = raw_input("entre com cadeia: ")
p = palin(cad)
if p:
    print cad, " e palindromo"
else:
    print cad, " nao e palindromo"
