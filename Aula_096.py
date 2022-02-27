def área(l,c):
    a = l*c
    print(f'A área de um terreno de {l:.1f} X {c:.1f} é de {a:.1f} m²')

#Programa Principal
print('Controle de Terrenos')
print('-'*30)
l = float(input('LARGURA (m) : '))
c = float(input('COMPRIMENTO (m) : '))
área(l,c)