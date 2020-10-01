lista = []
soma= 0
for i in range(6):
    lista.append(float(input()))

for numero in lista :
    if numero >0:
        soma+=1
print(soma,'valores positivos')

