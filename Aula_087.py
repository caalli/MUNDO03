matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = soma3C = maioSL = 0

for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um valor para [{l} {c}] : '))

        # Calcula a Soma dos número pares
        if matrix[l][c] % 2 == 0:
            somaPares += matrix[l][c]

    # Imprime todos os números digitados
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()

    # Soma os valores da terceira coluna
for l in range(0, 3):
    soma3C += matrix[l][2]

for c in range(0, 3):
    if matrix[1][c] > maioSL:
        maioSL = matrix[1][c]

print(f'A soma dos valores "PARES" digitados é : [{somaPares}]')
print(f'A soma dos valores da "Terceira Coluna" é : [{soma3C}]')
print(f'O maior valor na segunda linha é : [{maioSL}]')
