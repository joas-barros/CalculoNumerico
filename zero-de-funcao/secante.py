from math import fabs

a = float(input('Insira o valor de a: '))
b = float(input('Insira o valor de b: '))
e = float(input('Insira o erro: '))
i = 1
n = 1
Xn = 0
x = list()
x.append(a)
x.append(b)
limite = 100


def f(x):
    return x**5 - (10/9) * x**3 + (5/21) * x


if f(a) * f(b) > 0:
    print('NÃO HÁ RAIZES NESSE INTERVALO!')
else:
    Xn = x[n] - (f(x[n]) * (x[n] - x[n - 1])) / (f(x[n]) - f(x[n - 1]))
    while fabs(f(Xn)) > e:
        x.append(Xn)
        i += 1
        n += 1
        Xn = x[n] - (f(x[n]) * (x[n] - x[n - 1])) / (f(x[n]) - f(x[n - 1]))
        if i >= limite:
            print('NÃO FOI ENCONTRADA NENHUMA RAÍZ')
            break

print(f'Foram necessarias {i} iterações e a raiz é {Xn}')
