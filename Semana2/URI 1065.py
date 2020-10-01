lista = []
soma= 0
for i in range(5):
    lista.append(float(input()))

for numero in lista :
    if numero % 2 == 0:
        soma+=1
print(soma,'valores pares')

