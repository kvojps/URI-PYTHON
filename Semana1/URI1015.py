import math

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

calc = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
distanciaPontos = math.sqrt(calc)

print("%1.4f" % distanciaPontos)
