def contador(i, f, p):
    """
    --> Faz uma contagem e mostra na tela
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
        print()
    print('FIM')


# Programa Principal

help(contador)

# contador(0,100,2)