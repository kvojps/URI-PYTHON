listaNumeros = []

numeros = map(int,input().split())
for x in numeros:
    listaNumeros.append(x)

print(max(listaNumeros),"eh o maior")

