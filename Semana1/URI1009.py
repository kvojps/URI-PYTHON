nome = input()
salarioFixo = float(input())
totalVendas = float(input())

bonus = float(totalVendas * (15/100))
valorTotal = salarioFixo + bonus
print("TOTAL = R$ %1.2f" %valorTotal)