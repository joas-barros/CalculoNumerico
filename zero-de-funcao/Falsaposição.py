#Importar a biblioteca matemática
from math import fabs

#Definir o intervalo
a = float(input('Defina o valor de a: '))
b = float(input('Defina o valor de b: '))
e = float(input('Defina o erro: '))
c = 1

#Definir a função
def f(x):
    return x**4 - 2*(x**3) - 4*(x**2) + 4*x + 4

#Teorema de bolzano
xi = (a*f(b) - b*f(a))/(f(b) - f(a))

if f(a)*f(b) < 0:
    if f(xi) == 0:
        print(f'A raíz exata é {xi}')
    else:
        while fabs(f(xi)) > e:
            if f(a)*f(xi) < 0:
                b = xi
            else:
                a = xi
            xi = (a * f(b) - b * f(a)) / (f(b) - f(a))
            c += 1
        print(f'Foram necessarias {c} iterações e a raiz é {xi}')
else:
    print('Não há raíz no intervalo!')


