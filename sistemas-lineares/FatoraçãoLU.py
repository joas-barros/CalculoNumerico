from math import fabs
from copy import deepcopy


# pivoteamento
def LUpivoteamento(A, b):

    # acessar as linhas
    for i in range(len(A)):
        # Verificar qual é o maior pivo
        pivo = fabs(A[i][i])
        linhapivo = i
        if pivo == 0:
            for j in range(i + 1, len(A)):
                if fabs(A[j][i]) > pivo:
                    pivo = fabs(A[j][i])
                    linhapivo = j
        # Permutar as linhas
        if linhapivo != i:
            linhaauxiliar = A[i]
            A[i] = A[linhapivo]
            A[linhapivo] = linhaauxiliar

            bauxiliar = b[i]
            b[i] = b[linhapivo]
            b[linhapivo] = bauxiliar
        # Matriz L + U
        for m in range(i + 1, len(A)):
            multiplicador = A[m][i] / A[i][i]
            for n in range(i, len(A)):
                A[m][n] += -multiplicador * A[i][n]
                if A[m][n] == 0:
                    A[m][n] = multiplicador
    # Dividir as matrizes L e U
    L = deepcopy(A)
    U = deepcopy(A)
    lower(L)
    y = solucao(L, b)
    print('VETOR Y:')
    for k in range(len(y)):
        print(f'y({k + 1}) = {y[k]}')
    upper(U, y)


# Retrosubtituição de cima pra baixo
def solucao(A, b):

    y = list()
    for i in range(len(A)):
        y.append(0)
    linha = 0
    while linha <= (len(A) - 1):
        x = b[linha]
        coluna = 0
        while coluna < linha:
            x -= A[linha][coluna] * y[coluna]
            coluna += 1
        x /= A[linha][linha]
        linha += 1
        y[coluna] = x
    return y


# Matriz L
def lower(A):
    for i in range(len(A)):
        for j in range(len(A)):
            if j > i:
                A[i][j] = 0
            elif j == i:
                A[i][j] = 1
    print('MATRIZ LOWER:')
    for k in range(len(A)):
        print(A[k])


# Matriz U
def upper(A, b):
    for i in range(len(A)):
        for j in range(len(A)):
            if j < i:
                A[i][j] = 0
    print('MATRIZ UPPER:')
    for k in range(len(A)):
        print(A[k])
    # Resolução do sistema
    vetorSolucao = list()
    for i in range(len(A)):
        vetorSolucao.append(0)
    linha = len(A) - 1
    while linha >= 0:
        x = b[linha]
        coluna = len(A) - 1
        while coluna > linha:
            x -= A[linha][coluna] * vetorSolucao[coluna]
            coluna -= 1
        x /= A[linha][linha]
        linha -= 1
        vetorSolucao[coluna] = x
    print('VETOR SOLUÇÃO: ')
    for j in range(len(vetorSolucao)):
        print('x' + str(j + 1) + '=' + str(vetorSolucao[j]))


# Acessar a função
LUpivoteamento([[-9, 5, 6], [2, 3, 1], [1, 1, -3]], [11, 4, -2])
