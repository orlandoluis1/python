import math
a=float(input("Digite o valor de A: "))
b=float(input("Digite o valor de B: "))
c=float(input("Digite o valor de C: "))
b2 = b*b
xraiz = ((4 * a) * c)
delta = b2 - xraiz
if a == 0:
    print("A tem que ser diferente de 0")
elif delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a )
    x2 = (-b - math.sqrt(delta)) / (2 * a )
    print x1,"",x2
elif delta == 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a )
    print x1
else:
    if delta < 0:
        print "a raiz não pertence aos números reais"
