dias = int(input())
anos = 0
meses = 0

while True:
    if dias >= 365:
        dias -= 365
        anos += 1

    elif dias >= 30:
        dias -= 30
        meses += 1

    elif dias <30 :
        break

print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))