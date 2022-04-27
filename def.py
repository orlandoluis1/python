def somamult(x,y):
 
    mult7sub13 =0
    for i in range(n1+1,n2):
        if i%7==0:
            mult7sub13 += i
        if i%13==0:
            mult7sub13 -= i
    return mult7sub13

n1= input('n1: ')
n2= input('n2: ')
print "mult7 - mult13 = ", somamult(n1,n2)
