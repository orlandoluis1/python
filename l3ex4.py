p= raw_input('digite o produto: ').upper()
maior=0
while p != 'XXX':
    n= input('digite o preço: ')
    if maior < n:
        maior=n
    p= raw_input('digite o produto: ').upper()
print 'maior preço: ',maior
