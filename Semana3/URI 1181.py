matriz = []
tamanho = 12
linhaMatriz = int(input())
tipo = input()

for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0
for x in matriz[linhaMatriz]:
    soma += x
resultado = soma
if tipo == 'M':
    resultado = soma / tamanho

print('{:.1f}'.format(resultado))