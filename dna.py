dna=raw_input('digite a cadeia de dna: ').upper()
print 'cadeia de dna: ', dna
comp = dna.replace("A","V")
aux= comp
aux = comp.replace("T","A")
comp=aux
comp = aux.replace("C","B")
aux=comp
comp = aux.replace("G","C")
aux = comp
comp = aux.replace('B','G')
aux = comp
comp = aux.replace('V','T')
print 'cadeia de dna complementar: ',comp
