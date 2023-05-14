import math

# Definir o intervalo:
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
while True:
    n = int(input('Digite o número de subintervalos:(PAR) '))
    if (n % 2) != 0:
        print('ERRO! Por favor digite um valor par')
    else:
        break
y = sp = si = 0
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
    x += h

# Termos das pontas
y0 = tabela[0]
yn = tabela[len(tabela) - 1]

# Soma dos ímpares e pares
for i in range(len(tabela) - 2):
    c = i + 1
    if (c % 2) == 0:
        sp += tabela[c]
    else:
        si += tabela[c]

integral = (h / 3) * (y0 + (4 * si) + (2 * sp) + yn)
print('Integral =', integral)

