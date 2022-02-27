num = (int(input('Digite um número : ')), int(input('Digite um número : ')), int(input('Digite um número : ')),
       int(input('Digite um número : ')))

print(f'Você digitou {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
   print(f'O número 3 aparece na posição : {num.index(3) + 1} ')
else:
    print(f'O número 3 não foi digitado em nenhuma posição.')
print(f'Os número pares digitados são : ',end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
