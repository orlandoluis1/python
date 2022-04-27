vet = []
for i in range(0,100):
    vet.append(float(input('nota do aluno: ')))

st=0
mt=0
for i in range(0,100):
    st += vet[i]
mt = st/100

cp = 0
cr = 0
for i in range(0,100):
    if vet[i] >= mt:
        cp += 1
    else:
        cr += 1
print 'alunos acima da media: ',cp
print 'alunos abaixo da media: ',cr
