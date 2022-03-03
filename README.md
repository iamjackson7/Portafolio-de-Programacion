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

### Resta

### Multiplicación

### División

### Módulo

## Tipos de datos en Python

### Integer

### Float

### String

## Casting en Python

### List

### Tuple

### Dictionary

## Tomando decisiones

### Sentencia if

### Ciclo For
El bucle se repetira el numero de veces que le indiquemos ya sea una tupla, lista, variables, etc.
### Ciclo While
Al contrario del ciclo for, este bucle se repetira indeterminadas o determinadas veces.
### Break
En terminos comunes se podria decir que esta condicion se rompe el ciclo cuando ejecute el programa.
### Continue
La instrucción continue da la opción de omitir la parte de un bucle en la que se activa una condición externa, pero continuar para completar el resto del bucle.

´´´python

contador=0
for a in range (20):
    for b in range (20):
        contador +=1
        print ("a:",a,"b:",b)
        if contador >60:
            continue
print ("contador:",contador)

´´´
