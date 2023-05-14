import math

# Definir o intervalo:
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
while True:
    n = int(input('Digite o número de subintervalos:(MÚLTIPLO DE 3) '))
    if (n % 3) != 0:
        print('ERRO! Por favor digite um múltiplo')
    else:
        break
y = s3 = s = 0
h = (b - a) / n
x = a
tabela = list()


# Definir a função:
def f(x):
    return math.cos(2 * x)


# Tabelamento
while x <= b:
    y = f(x)
    tabela.append(y)
    # print(x)
    x += h

# Termos das pontas
y0 = tabela[0]
yn = tabela[len(tabela) - 1]

# Soma dos múltiplos e não múltiplos de 3
for i in range(len(tabela) - 2):
    c = i + 1
    if (c % 3) == 0:
        s3 += tabela[c]
    else:
        s += tabela[c]

integral = ((3 * h) / 8) * (y0 + (3 * s) + (2 * s3) + yn)
print('Integral =', integral)
