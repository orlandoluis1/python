a= input('digite o valor de a: ')
b= input('digite o valor de b: ')
s=0
if a > b:
    print 'erro'
else:
    for i in range (a+1,b):
        if i%4==0:
            s+=i
print "soma dos inteiros multiplos de 4 entre a e b e: ",s
