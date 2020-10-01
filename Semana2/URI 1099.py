soma = 0
n = int(input())

while n != 0:
    soma = 0
    x, y = map(int, input().split())
    if x > y:
        for i in range(y+1, x):
            if i % 2 != 0:
                soma += i
    elif y > x:
        for i in range(x+1, y ):
            if i % 2 != 0:
                soma += i
    print(soma)
    n -= 1