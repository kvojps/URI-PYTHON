a = int(input())
b = int(input())
soma = 0
for x in range((b + 1), a):
    if x % 2 != 0:
        soma += x
print(soma)
