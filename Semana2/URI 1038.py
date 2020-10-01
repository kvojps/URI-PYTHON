codigo, quantidade = map(int, input().split())

if codigo == 1:
    cachorroQuente = 4.00 * quantidade
    print("Total: R$ %.2f" % cachorroQuente)

elif codigo == 2:
    xSalada = 4.50 * quantidade
    print("Total: R$ %.2f" % xSalada)

elif codigo == 3:
    xBacon = 5.00 * quantidade
    print("Total: R$ %.2f" % xBacon)

elif codigo == 4:
    torradaSimples = 2.00 * quantidade
    print("Total: R$ %.2f" % torradaSimples)

elif codigo == 5:
    refrigerante = 1.50 * quantidade
    print("Total: R$ %.2f" % refrigerante)
