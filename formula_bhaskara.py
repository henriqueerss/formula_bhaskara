import math
a = float(input("Digite o valor de A\n"))
b = float(input("Digite o valor de B\n"))
c = float(input("Digite o valor de C\n"))

delta = b ** 2 - 4 * a * c

if delta == 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print("\nA única raiz do delta é ", raiz1)

else:
    if delta < 0:
        print("\nEsta equação não possui raízes reais.\n")
    
    else:
        raiz1 = ((-b + math.sqrt(delta)) / (2 * a))
        raiz2 = ((-b - math.sqrt(delta)) / (2 * a))
        print("\nA raiz do delta 1 é ", raiz1)
        print("\nA raiz do delta 2 é ", raiz2)