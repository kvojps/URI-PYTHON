valorTotal = int(input())
valor = valorTotal

notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
notas1 = 0

while valor > 0:
    if valor > 100:
        valor -= 100
        notas100 += 1

    elif valor >= 50:
        valor -= 50
        notas50 += 1

    elif valor >= 20:
        valor -= 20
        notas20 += 1

    elif valor >= 10:
        valor -= 50
        notas50 += 1

    elif valor >= 5:
        valor -= 5
        notas5 += 1

    elif valor >= 2:
        valor -= 2
        notas2 += 1

    elif valor >= 1:
        valor -= 1
        notas1 += 1

print(valorTotal)
print("%.0f nota(s) de R$ 100,00"%notas100)
print("%.0f nota(s) de R$ 50,00"%notas50)
print("%.0f nota(s) de R$ 20,00"%notas20)
print("%.0f nota(s) de R$ 10,00"%notas10)
print("%.0f nota(s) de R$ 5,00"%notas5)
print("%.0f nota(s) de R$ 2,00"%notas2)
print("%.0f nota(s) de R$ 1,00"%notas1)
