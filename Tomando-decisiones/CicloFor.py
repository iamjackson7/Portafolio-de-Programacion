# Calcular el promedio de un alumno que tiene 8 calificaciones en la materia de Cálculo.

n = 8
suma = 0
for i in range(n):
    nota = float(input('Ingrese nota ' + str(i) + ': '))
    suma = suma + nota

promedio = suma/n
print('Promedio:', promedio)
