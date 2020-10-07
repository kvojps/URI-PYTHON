contador = 0
numero = int(input())

for x in range(1000):
    print(f'N[{x}] = {contador}')
    contador += 1
    if contador == numero:
        contador = 0
