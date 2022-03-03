1.# Calcular el promedio de un alumno que tiene 8 calificaciones en la materia de Cálculo.

n = 8
suma = 0
for i in range(n):
    nota = float(input('Ingrese nota ' + str(i) + ': '))
    suma = suma + nota

promedio = suma/n
print('Promedio:', promedio)

2.# Leer 20 números y obtener su cubo y su cuarta.

n = 20
for i in range(n):
    num = int(input('Ingrese numero: '))
    print('Cubo:', num**3)
    print('Cuarta:', num**4)

3.# Leer 5 números e imprimir cuantos 
positivos = 0; negativos =0;neutros=0

for i in range(5):
    num = int(input('Ingrese numero: '))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        neutros += 1

print('Total positivos:', positivos)
print('Total negativos:', negativos)
print('Total neutros:', neutros)
