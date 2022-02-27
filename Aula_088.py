from random import randint
from time import sleep
lista = []
jogos = []
print('-='*25)
print('{:^50}'.format('JOGA NA MEGA SENA'))
print('-='*25)
quant = int(input('Quantos jogos você quer que eu sorteie ? : '))
tot = 1

while tot <= quant:
  cont = 0
  while True:
      num = randint(1,60)
      if num not in lista:
        lista.append(num)
        cont += 1
      if cont >= 6:
        break
  lista.sort()
  jogos.append(lista[:])
  lista.clear()
  tot += 1

print('-='*3, f'Sorteando {quant} jogos', '-='*3)
for i, l in enumerate(jogos):
    print(f'jogos {i+1} : {l}',end='')
    print()
    sleep(1)

