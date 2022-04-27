n=input('digite n: ')
if n <= 0:
    print 'erro'
if n == 1:
    print "0"
if n == 2:
    print '0','1'
else:
    n1 = 0
    n2 = 1
    print "0","1",
    for i in range(3,n+1):
        soma= n1 + n2
        print soma,
        n1=n2
        n2=soma
    
