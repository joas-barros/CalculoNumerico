from math import fabs

x0 = float(input('Insira o chute inicial: '))
e = float(input('Defina o erro: '))
i = 0
x = 0
ni = 100


def f(x):
    return x ** 5 - (10/9) * x ** 3 + (5/21) * x


def df(x):
    h = 0.00000001
    return (f(x + h) - f(x)) / h


while fabs(f(x0)) > e:

    x = x0 - f(x0)/df(x0)
    x0 = x
    i += 1
    if i >= ni:
        print('NÃO FOI ENCONTRADO NENHUMA RAIZ! ')
        break

print(f'Foram necessarias {i} iterações e a raiz é {x0}')
