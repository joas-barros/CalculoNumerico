from math import fabs


# Critério de parada (Erro relativo)
def comparar(x, xk, eps):
    max = maior = 0
    zip_object = zip(x, xk)
    for list1_i, list2_i in zip_object:
        Eabs = fabs(list2_i - list1_i)
        if Eabs > max:
            max = Eabs
        if fabs(list2_i) > maior:
            maior = list2_i
    ERel = max / maior
    print('Eabs =', max)
    print(f'Erel = {ERel}')
    if ERel < eps:
        return True
    else:
        return False


def gaussJacobi(A, b):
    n = len(b)
    sol = True
    x = b.copy()

    # Chute inicial

    for i in list(range(1, n + 1, 1)):
        if fabs(A[i-1][i-1]) != 0:
            x[i-1] = b[i-1]/A[i-1][i-1]
        else:
            sol = False
            break

    if sol:
        print('Iteração 0')
        print('x(0) =', x)
        xk = x.copy()
        maxiter = 100
        eps = 0.001
        iter = 0
        # Somatorio
        while iter < maxiter:
            iter += 1
            for i in list(range(1, n+1, 1)):
                s = 0
                for j in list(range(1, n+1, 1)):
                    if (i-1) != (j-1):
                        s = s + A[i-1][j-1]*x[j-1]

                xk[i-1] = (1/A[i-1][i-1])*(b[i-1] - s)
            # Resultado
            print('-' * 30)
            print('Iteração: ', iter)
            print('x(', iter, ') = ', xk)
            if comparar(x, xk, eps):
                x = xk.copy()
                break
            x = xk.copy()

    return x


A = [[-9, 5, 6],
     [2, 3, 1],
     [1, 1, -3]]

b = [11, 4, -2]

x = gaussJacobi(A, b)

