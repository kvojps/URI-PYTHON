from math import sqrt

A, B, C = map(float, input().split())
delta = B ** 2 - (4 * A * C)

if A == 0 or delta < 0:
    print('Impossivel calcular')

elif A != 0 or delta > 0:
    raiz_1 = (-B + sqrt(delta)) / (2 * A)
    raiz_2 = (-B - sqrt(delta)) / (2 * A)
    print('R1 = %1.5f' % raiz_1)
    print('R2 = %1.5f' % raiz_2)

