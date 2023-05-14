from math import fabs


# pivoteamento
def gausspivoteamento(A, b):

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
        # Eliminação de gauss
        for m in range(i + 1, len(A)):
            multiplicador = A[m][i]/A[i][i]
            for n in range(i, len(A)):
                A[m][n] -= multiplicador*A[i][n]
            b[m] -= multiplicador*b[i]
    # printar Matriz A escalonada e o vetor b
    print('MATRIZ ESCALONADA:')
    for k in range(len(A)):
        print(f'{A[k]} = {b[k]}')
    solucao(A, b)


def solucao(A, b):

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
        print('x'+str(j+1)+'='+str(vetorSolucao[j]))


gausspivoteamento([[-9, 5, 6], [2, 3, 1], [1, 1, -3]], [11, 4, -2])

