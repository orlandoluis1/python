n1= float(input('primeira nota: '))
n2= float(input('segunda nota: '))
m= (n1+n2)/2
if m >= 7:
    print 'aprovado'
else:
    if m>=4:
        print 'prova final'
    else:
        print 'reprovado'
