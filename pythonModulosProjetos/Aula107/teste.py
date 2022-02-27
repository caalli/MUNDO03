from Aula107 import moeda
p = float(input('Digite o preço : R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'A dobro de {p} é {moeda.dobro(p)}')
print(f'A aumentando 10% temos {moeda.aumentar(p, 10)}')
print(f'A reduzindo 13% temos {moeda.diminuir(p, 13)}')