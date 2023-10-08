from Cola import *

colaDespegue = Cola()
colaAterrizaje = Cola()

def crear_vuelo_despegue(tipo):
    aerolinea = input("Ingrese la aerolinea:\n")
    horasalida = int(input("Ingrese la hora de salida (Sistema horario de 24 horas):\n"))
    horallegada = int(input("Ingrese la hora de llegada (Sistema horario de 24 horas):\n"))
    aeropouertoD = str(input("Ingrese el aeropuerto destino:\n"))
    tipoVuelo = str(input("Ingrese el tipo de vuelo(Pasajeros o Carga):\n"))        
    vuelos = Vuelo(aerolinea, horasalida, horallegada, aeropouertoD, tipoVuelo)
    
    if tipo == 1:
        arribo(colaDespegue, vuelos)
    if tipo == 2:
        arribo(colaAterrizaje, vuelos)

x = 0
while (x != 5):
    try:
        x = int(input("---------Elige la opción a ejecutar---------\n1)Agregar Vuelo de Despegue\n2)Agregar Vuelo de Aterrizaje\n3)mostrar cola Avión\n4.\n5)Salir\n"))
    except ValueError:
        print("El dato ingresado no esta permitido, se esperaba un entero(1-4)")

    if x == 1: crear_vuelo_despegue(1)
    if x == 2: crear_vuelo_despegue(2)



barrido(colaDespegue)

