1.#Escribir un programa que solicite un valor entero al usuario y determine si es positivo o negativo.
num1=int(input("Ingrese un numero Entero:"))
if num1>0:
    print("El numero es positivo")
else:
    print("El numero es negativo")
    
2.# Calcular el mayor de dos números enteros introducidos por teclado.

# entradas
num1 = int(input("Ingreso num 1: "))
num2 = int(input("Ingreso num 2: "))

# proceso
if num1 > num2:
    # salida
    print("El numero mayor es:", num1)
elif num2 > num1:
    # salida
    print("El numero mayor es:", num2)
else:
    print("Los numeros son iguales")   

3.#Calcular el mayor de tres números enteros introducidos por teclado.

num1= int(input("Ingrese primer numero entero:"))
num2= int(input("Ingrese segundo numero entero:"))
num3= int(input("Ingrese tercer numero entero:"))

if num1>num2:
    print("Primer numero es mayor")
elif num2>num3:
    print("Segundo numero es mayor")
elif num3>num1:
    print("Tercer numero es mayor")
else:
    print("Todos son iguales")
