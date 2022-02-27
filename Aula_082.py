numeros = []
par = []
impar = []
while True:
    numeros.append(int(input('Digite um número : ')))
    flag = ' '
    while flag not in 'SN':
        flag = str(input('Deseja continuar ? [S/N] : ')).upper().strip()[0]
    if flag == 'N':
        break

for i, v in enumerate(numeros):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)

numeros.sort()
par.sort()
impar.sort()
print(f'A lista completa digitada é : {numeros}.')
print(f'A lista de pares é : {par}.')
print(f'A lista de ímpares é : {impar}')
