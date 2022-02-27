# def leiaInt():
#     if n.isnumeric():
#         print(f'Você acabou de digitar o número {n}')
#     else:
#         print('\033[0:30:41m ERRO! Digite um número inteiro válido.\033[m')
#
#
# # Programa Principal
# n = str(input('Digite um número : '))
# leiaInt()

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0:31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Programa Principal

n = leiaInt('Digite um número : ')
print(f'Você acabou de digitar o número {n}')
