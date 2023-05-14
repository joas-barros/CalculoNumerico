import math

# Definir o intervalo:
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
n = int(input('Digite o número de subintervalos: '))
y = s = 0
h = (b - a) / n
x = a
tabela = list()


# Definir a função:
def f(x):
    return math.cos(2 * x)


# Criando a tabela:
while x <= b:
    y = f(x)
    tabela.append(y)
    x += h

# Termos das pontas
y0 = tabela[0]
yn = tabela[len(tabela) - 1]

# Soma dos termos intermediarios:
for i in range(len(tabela) - 2):
    c = i + 1
    s += tabela[c]

integral = (h / 2) * (y0 + (2 * s) + yn)
print('Integral = ', integral)
