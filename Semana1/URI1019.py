N = int(input())

horas = N//3600
N -= horas*3600

minutos = N//60
N -= minutos*60

segundos = N

print('{}:{}:{}'.format(horas, minutos, segundos))

