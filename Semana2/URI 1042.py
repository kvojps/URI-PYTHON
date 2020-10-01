numeros = []

numeros.append(list(map(int,input().split())))
for numero in numeros:
    for item in sorted(numero) :
        print(item)
    print()
    for item_2 in numero:
        print(item_2)

