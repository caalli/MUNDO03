temp = []
princ = []
mai = men = 0
while True:
  temp.append(str(input('Nome : ')))
  temp.append(float(input('Peso : ')))
  if len(princ) == 0:
      mai = men = temp[1]
  else:
      if temp[1] > mai:
          mai = temp[1]
      if temp[1] < men:
          men = temp[1]
  princ.append(temp[:])
  temp.clear()
  resp = ' '
  while resp not in 'SN':
    resp = str(input('Quer continuar ? [S/N] : ')).upper().strip()[0]
  if resp == 'N':
    break
print('-='*30)
print(f'Os dados foram {princ}')
print(f'Foram cadastradas {len(princ)} pessoas')
print(f'O maior peso foi de {mai} KG. Peso de ',end='')
for p in princ:
    if p[1] == mai:
      print(f'[{p[0]}] ',end='')
print()
print(f'O menor peso foi de {men} KG. Peso de ',end='')
for p in princ:
    if p[1] == men:
      print(f'[{p[0]} ]',end='')
print()