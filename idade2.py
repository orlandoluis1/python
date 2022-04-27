i= input('digite sua idade: ')
if i <= 0:
    print 'erro'
elif i <= 3:
    print 'bebe'
elif i <= 11:
    print 'criança'
elif i <= 17:
    print 'teen'
elif i <= 30:
    print 'jovem'
elif i < 65:
    print 'adulto'
else:
    print 'senior'
