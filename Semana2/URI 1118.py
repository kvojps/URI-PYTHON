condicao = 'n'
while condicao == 'n':
    contador = 0
    media = 0
    continuar = 3

    while contador < 2:
        nota = float(input())
        if 0 <= nota <= 10:
            contador += 1
            media += nota
        else:
            print("nota invalida")
    print('media = %.2f' % (media / 2))

    while (continuar != 1 and continuar != 2):
        continuar = int(input("novo calculo (1-sim 2-nao)\n"))
        if continuar == 1:
            condicao = 'n'
        elif continuar == 2:
            condicao = 's'
        else:
            continuar = int(input("novo calculo (1-sim 2-nao)\n"))
