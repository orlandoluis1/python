import math
x=input('digite x: ')
y=input('digite y: ')
soma=0
for i in range(1,51):
    soma=soma + (( x + math.sqrt(y+2) )/float(3) ) + i**2 - y**5
print soma
