#Taller De Energia
consumo_energia = {
    'Coca Codo Sinclair':{
        'Quito': {'consumos': (400, 432, 400, 420, 432, 460, 432, 400, 432, 300, 213), 'tarifa': 65},
        'Guayaquil': {'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84},
    },
    'Sopladora': {
        'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
        'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
        'Tena': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
 },
}
tot_coca_codo_g = (120 + 55 + 32 + 120 + 75 + 32 + 150 + 55 + 32 + 120 + 97 + 32)
tot_coca_codo_q = (400 + 432 + 400 + 420 + 432 + 460 + 432 + 400 + 432 + 300 + 213)
tot_sopladora_g = (310 + 220 + 321 + 310 + 220 + 321 + 310 + 220 + 321 + 310 + 220 + 321)
tot_sopladora_q = (400 + 432 + 587 + 400 + 432 + 587 + 400 + 432 + 587 + 400 + 432 + 587)
tot_sopladora_l = (50 + 32 + 32 + 50 + 32 + 32 + 50 + 32 + 32 + 50 + 32 + 32)

informacion = {
 'costa': ('Guayaquil', 'Manta'),
 'sierra': ('Quito', 'Ambato', 'Loja'),
 'oriente': ('Tena', 'Nueva Loja')
}

costa = tot_coca_codo_g + tot_sopladora_g
sierra = tot_sopladora_q + tot_coca_codo_q + tot_sopladora_l
oriente = ('No hay planta en oriente')

print('''
    ===============================
          PLANTAS ENERGETICAS
    ===============================
    ''')
print('<1>. Total de Megavatios ')
print('<2>. Total de Energia ')
print('<3>. Dinero Recaudado ')
print('<4>. Escriba (salir) para Salir del programa')
opcion = input('Elija una opcion: ')

if opcion == 'salir':
    exit

#1. Solicite al usuario el nombre de una planta y de una ciudad y presente el total de
#megavatios de consumos para dicha ciudad en dicha planta.
elif opcion == '1':
    
    print('''
    ===============================
         TOTAL DE MEGAVATIOS
               PLANTAS
    Coca Codo Sinclair,Sopladora
              CIUDADES
    Guayaquil,Quito,Tena
    ===============================
    ''')

    n_planta = input('Ingrese el nombre de la planta: ')

    if n_planta == 'Coca Codo Sinclair':
        n_ciudad = input('Ingrese el nombre de la ciudad: ')

        if n_ciudad == 'Quito':
            print('Total de Megavatios de consumo en Coca Codo Sinclair, Quito: ', tot_coca_codo_q, 'Megavatios')
            print('Con tarifa de: ', consumo_energia['Coca Codo Sinclair']['Quito']['tarifa'])
        elif n_ciudad == 'Guayaquil':
            print('Total de Megavatios de consumo en Coca Codo Sinclair, Guayaquil: ', tot_coca_codo_g, 'Megavatios')
            print('Con tarifa de: ', consumo_energia['Coca Codo Sinclair']['Guayaquil']['tarifa'])
        elif n_ciudad =='Tena':
            print("No hay una planta de Coca Codo Sinclair en Tena")
    print()

    if n_planta == 'Sopladora':
        n_ciudad = input('Ingrese el nombre de la ciudad: ')

        if n_ciudad == 'Quito':
            print('Total de MMegavatios de consumo en Sopladora, Quito: ', tot_sopladora_q, 'Megavatios')
            print('Con tarifa de: ', consumo_energia['Sopladora']['Quito']['tarifa'])
        elif n_ciudad == 'Guayaquil':
            print('Total de Megavatios de consumo en Sopladora, Guayaquil: ', tot_sopladora_g, 'Megavatios')
            print('Con tarifa de: ', consumo_energia['Sopladora']['Guayaquil']['tarifa'])
        elif n_ciudad == 'Tena':
            print('Total de Megavatios de consumo en Sopladora, Tena: ', tot_sopladora_l)
            print('Con tarifa de: ', consumo_energia['Sopladora']['Tena']['tarifa'])
    else:
        print("Digite correctamente la primera en mayuscula")

    exit
    

    

#2. Solicite al usuario el nombre de una ciudad y presente un nuevo diccionario cuyas claves
#son los nombres de las plantas generadoras y el valor es el total megavatios que cada
#planta le ha dado a ciudad. Si la planta no entrega energía a la ciudad entonces esa planta
#no debería aparecer en el nuevo diccionario  
elif opcion == '2':
    print('''
    ===============================
    TOTAL DE ENERGIA 
       CIUDAD POR CADA PLANTA
               CIUDADES
    Guayaquil
    Quito
    Loja
    Ambato
    Tena
    Nueva loja
    ===============================
    '''),

    n_ciudad2 = input('Ingrese el nombre de la ciudad: ')

    if n_ciudad2 == 'Guayaquil':
        print('Total de Megavatios, Coca Codo Sinclair: ', tot_coca_codo_g, 'Megavatios')
        print('Total de Megavatios, Sopladora:', tot_sopladora_g, 'Megavatios')
    elif n_ciudad2 == 'Ambato':
        print('Total de Megavatios, Coca Codo Sinclair: ', tot_coca_codo_q, 'Megavatios')
        print('Total de Megavatios, Sopladora:', tot_sopladora_q, 'Megavatios')
    elif n_ciudad2 == 'Tena':
        print('Total de MMegavatios, Sopladora:', tot_sopladora_l, 'Megavatios')
    else:
        print('Ninguna planta otorga energía la ciudad seleccionada')
    print()

    exit


#3. Solicite el nombre de una región al usuario y presente cuento dinero ha recaudado la
#región
elif opcion == '3':
    print('''
    ===============================
          TOTAL DEL DINERO RECAUDADO 
              REGIONES
    Costa
    Sierra
    Oriente
    ===============================
    '''),

    n_region = input('Ingrese nombre de Región: ')

    if n_region == 'Oriente':
        print('Total Recaudado en la Región Oriente: ', oriente, '$')
    elif n_region == 'Costa':
        print('Total Recaudado en la Región Costa: ', costa, '$')
    elif n_region == 'Sierra':
        print(sierra)
    else:
        print("Digite correctamente la primera en mayuscula")
    exit

