palin = True
cad = raw_input("entre com cadeia: ")
for i in range(0,len(cad)//2):
    if cad[i] != cad[len(cad)- i -1]:
        palin = False
if palin:
    print cad, " eh palindromo"
else:
    print cad, " nao eh palindromo"
