from math import sqrt
import time

print("########### CALCULADORA DE FORMULA QUADRÁTICA v1.1.2 ###########")

con = "s"

while (con.lower() == "s"):

    a = int(input('digite o valor de a: '))
    b = int(input('digite o valor de b: '))
    c = int(input('digite o valor de c: '))

    D = pow(b, 2) - 4 * a * c

    if D > 0:

        x1 = (-b + sqrt(D) / (2 * a))
        x2 = (-b - sqrt(D) / (2 * a))

        print('Valor de x1: {0}'.format(x1))
        print('Valor de x2: {0}'.format(x2))

    else:
        print("Não existe raizes reais")

    con = input("Deseja realizar mais algum cálculos? (S/N): \n")

else:
   print("Fim! ")
   time.sleep(1)