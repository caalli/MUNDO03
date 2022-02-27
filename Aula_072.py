cont = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    num = int(input('Digite um número de 0 até 20 : '))
    if 0 <= num <=  20:
        break
    print('Número fora da faixa, tente de novo!')
print(f'Você digitou o número {cont[num]}')