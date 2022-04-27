vetor = [0.0] * 40
sa = 0
c = 0
m = 0
for i in range(0,40):
    nota = input('digite a media final do aluno: ')
    vetor[i] = nota
    sa += nota
m = sa / 40
for j in range(0,40):
    if vetor[j] > m :
      c += 1
print "qtd de alunos acima da media da turma: ", ca
