valores = list()
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um número para a posição {c} : ')))
    if c == 0:
            maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print(f'\033[34mOs números digitados foram : {valores}')
print(f'O número maior é o {maior}, e está na posição : ',end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...',end='')
print('')
print(f'O número menor é o {menor}, e está na posição : ',end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...',end='')


