i= input('digite sua idade: ')
if i <= 0:
    print 'erro'
else:
    if i <= 3:
        print 'bebe'
    else:
        if i <= 11:
            print 'criança'
        else:
            if i <= 17:
                print 'teen'
            else:
                if i <= 30:
                    print 'jovem'
                else:
                    if i < 65:
                        print 'adulto'
                    else:
                        print 'senior'
