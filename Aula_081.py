numeros = []
while True:
    numeros.append(int(input('Digite um número : ')))
    flag = ' '
    while flag not in 'SN':
        flag = str(input('Deseja continuar ? [S/N] : ')).upper().strip()[0]
    if flag == 'N':
        break
print(f'Foram digitados {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são : {numeros}')
if 5 in numeros:
    print('O números 5 foi digitado e está na lista!!')
else:
    print('O número 5 não está na lista!!')