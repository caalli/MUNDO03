from time import sleep

def maior(*num):
    cont = maior = 0

    print('-=' * 30)
    print('Analisando os valores passados....')

    for valor in num:
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
        sleep(1)
    print(f" foram informados {cont} valores ao todo.")
    print(f'O maior número informado foi {maior}.')


# Programa Principal
maior(50, 2, 9, 4, 5, 7, 1, 13)

