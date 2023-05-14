#Importar a biblioteca matemática
from math import fabs

#Definir o intervalo [a,b] e o erro
a = float(input('Defina o valor de a: '))
b = float(input('Defina o valor de b: '))
e = float(input('Defina o erro: '))
c = 1

# Definir a função
def f(x):
    return x**4 - 2*(x**3) - 4*(x**2) + 4*x + 4

# Teorema de Bolzano
xi = (a + b)/2

if f(a)*f(b) < 0:

    while fabs(f(xi)) > e:
        c += 1
        if f(xi) == 0:
            print(f'A raiz exata é: {xi}')
            break
        else:
            if f(a)*f(xi) < 0:
                b = xi
            else:
                a = xi
            xi = (a + b) / 2
    print(f'foram necessarias {c} iterações e a raiz no intervalo é {xi}')
else:
    print('Não há raizes nesse intervalo!')
