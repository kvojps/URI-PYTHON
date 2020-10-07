matriz = []
numeroColuna = int(input())
tipo = input()
tamanho = 12

#Criei a matriz
for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append(float(input()))
    matriz.append(linha)

#Obter uma lista para a coluna que eu desejo calcular
coluna = []
for x in range(tamanho):
    coluna.append(matriz[x][numeroColuna])


resultado = 0

if tipo == 'S':
    resultado = sum(coluna)
else:
    resultado = sum(coluna) / len(coluna)

print(f'{resultado:.1f}')