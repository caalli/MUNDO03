numeros = []
while True:
  n = int(input('Digite um número : '))
  if n not in numeros:
    numeros.append(n)
    print('Valor adicionado com sucesso!!!')
  else:
    print('\033[32:40mValor duplicado! Não vou adicionar...\033[m')
  resp = ' '
  while resp not in 'SN':
      resp = str(input('Quer continuar ? [S/N] : ')).upper().strip()[0]
  if resp in 'N':
    break
numeros.sort()
print(numeros)