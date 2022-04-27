a= input('digite o valor de a: ')
b= input('digite o valor de b: ')
s=0
if a > b:
    print 'erro'
else:
    for i in range (a+1,b):
        s+=i
print "soma dos inteiros entre a e b e: ",s
