def fatorial(n, show=False):
    """
    Fatorial(n, show False)
    :param num: O número a ser calculado
    :param show:(Opcional)
    :return: O valor do fatorial de um número.
    """
    f = 1

    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
n = int(input('Digite um número : '))
print(fatorial(n, show=True))


# help(fatorial)