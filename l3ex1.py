i= input('idade: ')
contf = 0
contm = 0
mf= 0
mm= 0
msa = 0
sf = 0
sm = 0
while i > 0:
   s= raw_input('sexo: ').upper()
   sa= float(input('salario: '))
   if i < 30:
       if msa < sa:
           msa = sa
   if s == 'F':
       sf = sf + sa
       contf += 1
       mf += sf / contf
   else:
       if s == "M":
           sm = sm + sa
           contm += 1
           mm += sm / contm
   i= input('idade: ')    
print 'media de salario das mulheres: ', mf
print 'media de salario dos homens: ', mm
print 'maior salario dos menores de 30 anos: ', msa

   
