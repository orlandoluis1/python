for j in range(1,100,2):
    n = 6
    m = (j*j) + 6*j + 9
    mdc = 1
    for i in range (2 , n+1):
        if n % i == 0 and m % i == 0:
            mdc = i 
    print "MDC(",n ,",", m ,')=', mdc
