from datetime import datetime

cadastro = {}
cadastro['Nome'] = str(input('Nome : '))
nasc = int(input('Ano de Nascimento : '))
cadastro['Idade'] = datetime.now().year - nasc
cadastro['CTPS'] = int(input('Nº da Carteira de Trabalho (0 não tem) : '))
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano de Contratação : '))
    cadastro['salário'] = float(input('Salário : R$  '))
    cadastro['Aposentadoria'] = cadastro['Idade'] + (cadastro['Contratação'] + 35) - datetime.now().year

print('-=' * 30)

for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')

