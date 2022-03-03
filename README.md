"# Portafolio-de-Programacion" 
## ¿Qué es Python?
Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Se trata de un lenguaje de programación multiparadigma, ya que soporta parcialmente la orientación a objetos, programación imperativa y, en menor medida, programación funcional.
## ¿Qué es una variable?
Una variable es donde se guarda y se recupera datos que se utilizan en un programa.
### Nombrando una variable
La creación de variables se realiza a través de la estimación de un valor a la misma. El operador de imprimir en Python es el “=“.
- x = 30
De derecha a izquierda
"correcto"
- 30 = x
De izquierda a derecha
"incorrecto"

### Asignando valores a una variable

## Operadores básicos
-suma (+)
-multiplicación (*)
-resta (-)
-Division (/)
-módulo (%)

### Suma
Operación aritmética que consiste en sumar 2 o varias cantidades; se representa con el signo +.

```python
n1=float(input("Intro número uno: "))
n2=float(input("Intro numero dos: "))
suma=n1+n2

print("La suma es: ",suma

```
### Resta
Operación aritmética que consiste en quitar una cantidad de otra para averiguar la diferencia entre las dos, se representa con el signo -.

```python
num1=20
num2=12
resta=num1-num2
print(num1,'-',num2,'=',resta)

```
### Multiplicación
Operación aritmética que consiste en calcular el resultado de sumar un mismo número  tantas veces como indica otro número; se representa con los signos · o *.

```python
numero1 = int(input("Ingrese un numero"))
numero2 = int(input("Ingrese un numero"))
numero3 = int(input("Ingrese un numero"))
multiplicacion = numero1 * numero2 * numero3
print('Los valores ingresados multiplicados hacen un total' , multiplicacion)

```
### División
La división es aquella operación matemática mediante la cual se trata de descomponer un número.

```python
division = int(6/3)
print("La division es", division)
[output] 2

```
### Módulo
El operador módulo da como resultado el resto de la división entera.

```python
num1=25
num2=4
modulo=num1%num2
print(num1,'%',num2,'=',modulo)

```
## Tipos de datos en Python

### Integer

### Float

### String

## Casting en Python

### List
List en Python son un tipo de estructuras de datos muy flexible que guardan de forma ordenada un conjunto de datos que no tiene porque ser del mismo tipo.

```python
list= [1, 3.1416, 'j', 'jackson.com',  True]
print 'Imprimimos los elementos de una lista y el tipo de dato de cada elemento'
for l in list:
    print '%s - %s' %(l, type(l))

```
### Tuple
Una tupla es un conjunto ordenado e inmutable de elementos del mismo o diferente tipo. Las tuplas se representan escribiendo los elementos entre paréntesis y separados por comas. Una tupla puede no contener ningún elemento, es decir, ser una tupla vacía.

```python
>>> numeros = (2, 4, 6, 8, 10)

```

```python
>>> elementos = (3, 'a', 8, 7.2, 'holi')

```

```python
>>> vocales = (a, e, i, o, u)

```
### Dictionary
Un Diccionario es una estructura de datos y un tipo de dato en Python con características especiales que nos permite almacenar cualquier tipo de valor como enteros, cadenas, listas e incluso otras funciones. 

```python
>>> d2 = dict(uno=1, dos=2, tres=3)
>>> d2
{'uno': 1, 'dos': 2, 'tres': 3}
```
## Tomando decisiones

### Sentencia if
La sentencia if se utiliza para ejecutar un bloque de código si, y solo si, se cumple una determinada condición. Por tanto, if es usado para la toma de decisiones. Es decir, solo si condición se evalúa a True , se ejecutarán las sentencias que forman parte de bloque de código .

```python
valores = [5,7,8,12]
if 5 in valores:
    print('está en valores')
print('fin')

```
### Ciclo For
El bucle se repetira el numero de veces que le indiquemos ya sea una tupla, lista, variables, etc.

```python
nums = [4, 78, 9, 84]
for n in nums:
    print(n)
4
78
9
84

```
### Ciclo While
Ciclo while en Python es una sentencia de control de flujo que se utiliza para ejecutar un bloque de instrucciones de forma continuada mientras se cumpla una condición determinada.

```python
numero = 0
print('Tabla del 3')
while numero <= 10:
    print(f'{numero * 3}')
    numero += 1
print('Fin')

```
### Break
La instrucción break le proporciona la oportunidad de cerrar un bucle cuando se activa una condición externa. Debe poner la instrucción break dentro del bloque de código bajo la instrucción de su bucle, generalmente después de una instrucción if condicional.

```python
number = 0

for number in range(10):
    if number == 5:
        break    # break here

    print('Number is ' + str(number))

print('Out of loop')

```
### Continue
La instrucción continue da la opción de omitir la parte de un bucle en la que se activa una condición externa, pero continuar para completar el resto del bucle. Es decir, la iteración actual del bucle se interrumpirá, pero el programa volverá a la parte superior del bucle.

```python

contador=0
for a in range (20):
    for b in range (20):
        contador +=1
        print ("a:",a,"b:",b)
        if contador >60:
            continue
print ("contador:",contador)

```
