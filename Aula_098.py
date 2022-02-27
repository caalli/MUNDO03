from time import sleep
def contador(i,f,p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    print('-='*15)

    cont = i
    if i <= f:
        while cont <= f:
            print(f'{cont}',end=' ', flush=True)
            sleep(1)
            cont += p
        print('FIM!')
    else:
          cont = i
          while cont >= f:
                print(f'{cont}', end=' ',flush=True)
                sleep(1)
                cont -= p
          print('FIM!')
    print('-='*15)
#Programa Principal
contador(1,10,1)
contador(10,0,2)
print('Agora é a sua vez de personalizar a contagem.')
ini = int(input('Início : '))
fim = int(input('Fim : '))
pas = int(input('Passo : '))
contador(ini,fim,pas)
