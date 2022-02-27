def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    if idade < 16:
        return f'Com {idade} anos : NÃO VOTA. '

    elif idade <= 16 < 18 or idade > 60:
        return f'Com {idade} anos : VOTO OPCIONAL. '

    else:
        return f'Com {idade} anos : VOTO OBRIGATÓRIO. '


# Programa Principal
nasc = int(input('Em que ano você nasceu ? : '))
print(voto(nasc))
