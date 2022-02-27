def dobro(preço = 0, formato=False):
    """
    --> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preço: O preço que se quer reajustar
    :param taxa: qual é a porcetagem do aumento
    :param formato: quer a saída formatada ou não ?
    :return:  O valor reajustado, com ou sem formato.

    """
    res = preço * 2
    return res if formato is False else moeda(res)


def aumentar(preço = 0, taxa=0, formato=False):
     res = preço + (preço * taxa / 100)
     return res if formato is False else moeda(res)


def diminuir(preço = 0, taxa = 0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def metade(preço = 0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço = 0, moeda='R$'):
    return f'{moeda} {preço:>.2f}'.replace('.',',')

