def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato. ')


# Programa Principal
jogador = str(input('Nome do jogador : '))
gols = str(input('Quantos gols marcados : '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if jogador.strip() == '':
    ficha(gol=gols)
else:
    ficha(jogador, gols)
