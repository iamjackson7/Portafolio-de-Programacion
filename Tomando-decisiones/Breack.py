1.#Crear un programa que cuando encuentre la letra "b", pare.
cadena = 'programacion'
for letra in cadena:
    if letra == 'b':
        print("Se encontró la b")
        break
    print(letra)

2.#Crear un programa que cuando llegue al 10 pare.
j=0
for i in range(15):
    j+=2
    print("i:",i,"j:",j)
    if j==10:
        break
        
3.
contandor=0
for i in range(10):
    for j in range(10):
        contandor += 1
        print(i,j)
        break
#Nunca se realiza más de una iteración
#El break no afecta a este for
print("contandor:",contandor)
 

