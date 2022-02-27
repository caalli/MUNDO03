from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1' : randint(1,6),
        'Jogador2' : randint(1,6),
        'Jogador3' : randint(1,6),
        'Jogador4' : randint(1,6)}
for k, v in jogo.items():
  print(f'{k} tirou {v} no dados.')
  sleep(2)
ranking = sorted(jogo.items(), key = itemgetter(1), reverse=True)
print('-='*30)
print('  == RANKING DOS JOGADORES  ==')
for i, v in enumerate(ranking):
    print(f' {i+1}º Lugar : {v[0]} com {v[1]}')
    sleep(2)
