def dobro(preço=0):
    """
        --> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preço: O preço que se quer reajustar
    :return:  O valor
    """
    res = preço * 2
    return res


def aumentar(preço=0, taxa=0):
     res = preço + (preço * taxa / 100)
     return res


def diminuir(preço=0, taxa = 0):
    res = preço - (preço * taxa / 100)
    return res


def metade(preço=0):
    res = preço / 2
    return res


def moeda(preço=0, moeda='R$'):
    return f'{moeda} {preço:.2f}'.replace('.',',')

