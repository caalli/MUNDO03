ficha = []

while True:
    nome = str(input('Nome : '))
    nota1 = float(input('Nota 1 : '))
    nota2 = float(input('Nota 2 : '))
    media = (nota1 + nota2)/2
    ficha.append([nome,[nota1,nota2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar ? [S/N] : ')).upper().strip()[0]
    if resp == 'N':
      break

print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
  print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
  print('-'*35)
  opc = int(input('mostrar notas de qual aluno ? (999 Interromper) : '))
  if opc == 999:
      print('Finalizado...')
      break
  if opc <= len(ficha) -1:
      print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<VOLTE SEMPRE!!!>>')

