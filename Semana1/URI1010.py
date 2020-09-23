produto1 = input().split(" ")
codigo1, quantidade1, valor1 = produto1

produto2 = input().split(" ")
codigo2, quantidade2, valor2 = produto2

precoTotal = (int(quantidade1) * float(valor1)) + (int(quantidade2) * float(valor2))
print("VALOR A PAGAR: R$ %0.2f"%precoTotal)