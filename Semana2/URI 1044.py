lista = []
A,B = map(int,input().split())
lista.append(A)
lista.append(B)
lista = sorted(lista)

if lista[1] % lista[0] == 0:
    print("Sao multiplos")

else:
    print("Nao sao Multiplos")