#Taller Energia 2
consumo_energia = {
    'Coca Codo Sinclair':{
        'Quito': {'consumos': (400, 432, 400, 420, 432, 460, 432, 400, 432, 300, 213), 'tarifa': 65},
        'Guayaquil': {'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84}
    },
    'Sopladora': {
        'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
        'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
        'Tena': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
        'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
        'Manta': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32}
 },
}



def total_consumo_por_planta_ciudad(planta, ciudad):
    if planta not in consumo_energia.keys():
        return 'La planta ' + planta + ' no existe'

    if ciudad not in consumo_energia[planta].keys():
        return 'La planta ' + planta + ' no proveé energía a la ciudad de ' + ciudad

    total_consumo = sum(consumo_energia[planta][ciudad]['consumos'])
    return total_consumo

def total_consumo_ciudad(ciudad):
      
    if ciudad not in consumo_energia['Coca Codo Sinclair'].keys():
        return 'No hay planta de Coca Codo Sinclair en:' + ciudad


    total_consumo2 = sum(consumo_energia['Coca Codo Sinclair'][ciudad]['consumos'])
    print( 'El consumo de energía de la planta Coca Codo Sinclair en la ciudad de',ciudad,total_consumo2,"MWh")



def total_consumo_ciudad1(ciudad):
    if ciudad not in consumo_energia['Sopladora'].keys():
        return 'No hay planta de Sopladora en:' + ciudad

    total_consumo2 = sum(consumo_energia['Sopladora'][ciudad]['consumos'])
    print( 'El consumo de energía de la planta Sopladora en la ciudad de',ciudad,total_consumo2,"MWh")

op = -1
while op != 0:

    print('<1> Total de energía consumida por planta y ciudad')
    print('<2>. Total de Energia por Ciudad ')
    print('<3>. Dinero Recaudado por Region ')
    print('<0> Salir')

    op = int(input('Ingrese opción:'))
#1. Solicite al usuario el nombre de una planta y de una ciudad y presente el total de
#megavatios de consumos para dicha ciudad en dicha planta.
    if op == 1:
        print('''
    ===============================
         TOTAL DE MEGAVATIOS
               PLANTAS
    Coca Codo Sinclair,Sopladora
    ===============================
    ''')
        planta = input('Ingrese el nombre de la planta:')
        ciudad = input('Ingrese el nombre de la ciudad:')

        total = total_consumo_por_planta_ciudad(planta, ciudad)

        if type(total) == int:
            print('El consumo de energía en la ciudad de {} fue de {} MWh en la planta {}'.format(ciudad, total, planta))
        else:
            print(total)

#2. Solicite al usuario el nombre de una ciudad y presente un nuevo diccionario cuyas claves
#son los nombres de las plantas generadoras y el valor es el total megavatios que cada
#planta le ha dado a ciudad. Si la planta no entrega energía a la ciudad entonces esa planta
#no debería aparecer en el nuevo diccionario  
    elif op == 2:
        print('''
    ===============================
    TOTAL DE ENERGIA DADA A CADA
       CIUDAD POR CADA PLANTA
               CIUDADES
    Guayaquil
    Quito
    Loja
    Ambato
    Tena
    Nueva loja
    Manta
    ===============================
    ''')
    ciudad = input('Ingrese el nombre de la ciudad:')

    total1 = total_consumo_ciudad(ciudad)
    total2 = total_consumo_ciudad1(ciudad)
    if type(total1 and total2)==int:
        print(total1)
        print(total2)
    else:
        print(total1)
        print(total2)
#3. Solicite el nombre de una región al usuario y presente cuento dinero ha recaudado la
#región    
    elif op == 3:
        print('''
    ===============================
          DINERO TOTAL 
              REGIONES
    Costa
    Sierra
    Oriente
    Insular
    ===============================
    ''')
        region = input('Ingrese región:')
        total3 = total_por_region(region)
        if type(total3)==int:
            print("La Region",region, 'recaudo:', total3,"Dolares$", '\n')
        else:
            print(total3)
    elif op==0:
        exit
        print("saliendo")
    else:
        print("Coloque Bien")
