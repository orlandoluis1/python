# nome: Orlando Luis Xavier Fernandes
# data: 14/04/2021
menoridade = 100
contcovid= 0
mediamulher= 0
contmulher = 0
somamulher = 0
conttotal = 0
s= raw_input ('digite seu sexo: ')
while s != 'FIM':
    i= input('digite sua idade: ')
    tcovid = raw_input('resutado do teste de covid: ')
    conttotal += 1
    if s == 'F' and tcovid== "P" :
        somamulher = somamulher + i
        contmulher += 1
        mediamulher += float(somamulher) / contmulher
    if menoridade > i and tcovid == 'P':
        menoridade = i
    if tcovid == 'P':
        contcovid += 1
    s= raw_input ('digite seu sexo: ')
print ' a media de idade das mulheres com covid e de: ', mediamulher
print ' a menor idade das pessoas que testaram positivo para covid e de: ', menoridade
print 'a porcentagem de pessoas com covid e de: ', float(contcovid) / conttotal   
