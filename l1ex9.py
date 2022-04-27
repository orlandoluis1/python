m=input('digite m: ')
n=input('digite n: ')
if m<n:
    print 'erro m e menor que n'
else:
    lado1 = (m**2) - (n**2)
    lado2 = 2*m*n
    hipotenusa = (m**2) + (n**2)
    print lado1,'',lado2,'',hipotenusa
    
