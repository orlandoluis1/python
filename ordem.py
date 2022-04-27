for j in range(2,100):
    n = j - 1
    m = (j)
    mdc = 1
    for i in range (2 , n+1):
        if n % i == 0 and m % i == 0:
            mdc = i 
    print "MDC(",n ,",", m ,')=', mdc
