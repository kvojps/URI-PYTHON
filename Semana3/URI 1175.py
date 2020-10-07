lista = []
contador = 0
for x in range(20):
    lista.append(int(input()))
lista = reversed(lista)
for y in lista:
    print(f'N[{contador}] = {y}')
    contador += 1
