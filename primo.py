n=input('digite um numero: ')
primo=True
for i in range(2,n):
    if n%i==0:
        primo=False
if primo== True:
    print 'primo'
else:
    print 'n e primo'
        
