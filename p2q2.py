#nome: orlando luis xavier fernandes
#data: 28/04/2021

cad1 = raw_input("entre com uma cadeia: ")
cad2 = raw_input("entre com outra cadeia: ")
resp1=''
resp2=''
for i in range(0,len(cad1)):
    if i % 2 == 0:
        resp1 += cad1[i]
for j in range(0,len(cad2)):
    if j % 2 != 0:
        resp1 += cad2[j]
if len(resp1)%2== 0:
    for i in range(0,len(resp1),2):
        resp2 += resp1[i+1]+resp1[i]
else:
    for i in range(0,len(resp1)-1,2):
        resp2 += resp1[i+1]+resp1[i]
    resp2 = resp2 + resp1[len(resp1)-1]
print 'primeiro par e segundo impar: ', resp1
print 'respota alternada: ', resp2
