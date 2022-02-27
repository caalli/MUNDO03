def leiaInt(msg):
    while True:
        try:
            n1 = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não digitar.\033[m')
            return 0
        else:
            return n1


def leiaFloat(msg):
    while True:
        try:
            n2 = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mErro! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não digitar.\033[m')
            return 0
        else:
            return n2

# Programa Principal

n1 = leiaInt('Digite um inteiro : ')
n2 = leiaFloat('Digite um real : ')

print(f'\033[32mO valor inteiro digitado foi {n1} e o real foi {n2}\033[m')
