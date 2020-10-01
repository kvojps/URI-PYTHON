salario = float(input())
salarioAntigo = salario

if salario <=400:
    salario += 0.15 * salario
elif salario > 400 and salario <=800:
    salario += 0.12 * salario
elif salario > 800 and salario <= 1200:
    salario += 0.10 * salario
elif salario >1200 and salario <= 2000:
    salario += 0.07 * salario
elif salario > 2000:
    salario += 0.04 * salario

print('Novo salario: %0.2f'%salario)
reajuste = salario - salarioAntigo
print('Reajuste ganho: %0.2f'%reajuste)
percentual = ((salario/salarioAntigo) *100) - 100
print('Em percentual: %1.0f'%percentual,'%')
