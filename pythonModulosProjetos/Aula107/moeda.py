def dobro(preço):
    """
    --> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preço: O preço que se quer reajustar
    :return:  O valor
    """
    res = preço * 2
    return res


def aumentar(preço, taxa=0):
     res = preço + (preço * taxa / 100)
     return res


def diminuir(preço, taxa = 0):
    res = preço - (preço * taxa / 100)
    return res


def metade(preço):
    res = preço / 2
    return res



