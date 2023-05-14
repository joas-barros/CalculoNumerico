import math

# Definir o intervalo:
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
n = int(input('Digite o número de subintervalos: '))
y = se = sd = 0
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

# Soma à esquerda:
for i in range(len(tabela) - 1):
    se += tabela[i]
ie = h * se

# Soma à direita:
for i in range(len(tabela) - 1):
    sd += tabela[i + 1]
id = h * sd

# Média
imed = (ie + id) / 2

print('-' * 30)
print(f'Integral à esquerda = {ie}')
print(f'Integral à direita {id}')
print(f'Integral média= {imed}')
print('-' * 30)
