#Crear un programa que cuando encuentre la letra "b", pare.
cadena = 'programacion'
for letra in cadena:
    if letra == 'b':
        print("Se encontró la b")
        break
    print(letra)
