1.
x = 7
while x > 0:
    x -= 1
    if x == 3:
        continue
    print(x)

2.
cadena = 'Python'
for letra in cadena:
    if letra == 'o':
        continue
    print(letra)
    print("..........")
    
3.
a=0
for i in range(10):
    a+=2
    print("i:",i,"a:",a)
    if a>=2 and  a<=18:
        continue
    print("el valor de a:",a)
