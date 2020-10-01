numerosPorLinha, limite = map(int, input().split())
lista = []
for x in range(1, limite + 1):
  lista.append(x)
  if(len(lista) == numerosPorLinha):
    print(' '.join(map(str, lista)))
    lista = []