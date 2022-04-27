s= raw_input('string: ')
contN=0
contA=0
contO=0
for i in range (0, len(s)):
    if s[i].isdigit() == True:
        contN +=1
    else:
        if s[i].isalpha() == True:
            contA +=1
        else:
            contO += 1
print "letras: ", contA
print "numeros: ", contN
print 'outros caracteres: ', contO
