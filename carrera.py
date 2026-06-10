from Personaje import Personaje

personajes=[]

menu='''
1. Crear personaje
2. Correr
3. Mostrar info de corredores
4. Salir

'''

while True:
    print(menu)
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        nombre = input("Ingrese el nombre del personaje: ")
        altura = float(input("Ingrese la altura del personaje: "))
        velocidad = float(input("Ingrese la velocidad del personaje: "))
        resistencia = float(input("Ingrese la resistencia del personaje: "))
        fuerza = float(input("Ingrese la fuerza del personaje: "))
        personaje= Personaje(nombre, altura, velocidad, resistencia, fuerza)
        personajes.append(personaje)
        print(f"{personaje.nombre} creado exitosamente")
    elif opcion == 2:      
        
        tiempo = personajes.corer()
        print(f"{personaje.nombre}demoro {tiempo}")
    elif opcion == 3:
        print(personajes)