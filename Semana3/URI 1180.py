numero = int(input())
lista = []
contador = 0
numeros = list(map(int, input().split()))


for x in range(numero):
    lista.insert(x,numeros[x])
print('Menor valor:',min(numeros))

for y in numeros:
    if y == min(numeros):
        break
    contador+=1
print('Posicao:',contador)