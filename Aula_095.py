jogador = dict()
partidas = list()
times = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador : '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ? : '))
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c} : ')))

    print('-=' * 30)
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    times.append(jogador.copy())

    while True:
        resp = str(input('Deseja continuar ? [S/N] : ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite S ou N.')
    if resp == 'N':
        break

print('-=' * 30)
for k, v in enumerate(times):
    print(f'{k:>3}', end='')
    for d in v.values():
            print(f'{str(d):<15}', end='')
    print()
print('-' * 40)