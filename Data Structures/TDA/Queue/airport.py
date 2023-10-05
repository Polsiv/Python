from queuetda import *
import time
vuelos_salida, vuelos_llegada = [], []
vuelo = {"Aerolinea": None, "HoraSalida": None, "HoraLlegada": None, "Aeropuerto0": None,"AeropuertoD": None, "TipoVuelo": None}
VueloDespegue = Cola()
VueloAtterizaje = Cola()


x = 0
while (x != 5):
    try:
        x = int(input("---------Elige la opción a ejecutar---------\n1)Agregar Vuelo de Despegue\n2)Agregar Vuelo de Aterrizaje\n3)mostrar cola Avión\n4.\n5)Salir\n"))
    except ValueError:
        print("El dato ingresado no esta permitido, se esperaba un entero(1-4)")

    if x == 1:
        vuelo["Aerolinea"] =input("Ingrese la aerolinea:\n")
        vuelo["HoraSalida"] = int(input("Ingrese la hora de salida (Sistema horario de 24 horas):\n"))
        vuelo["HoraLlegada"] = int(input("Ingrese la hora de llegada (Sistema horario de 24 horas):\n"))
        vuelo["Aeropuerto0"] = str(input("Ingrese el aeropuerto de origen:\n"))
        vuelo["AeropuertoD"] = str(input("Ingrese el aeropuerto destino:\n"))
        vuelo["TipoVuelo"] = str(input("Ingrese el tipo de vuelo(Pasajeros o Carga):\n"))        
        vuelos_salida.append(vuelo)
        vuelos_salida = seleccion_despegue(vuelos_salida)
        for i in vuelos_salida:
            arribo(VueloDespegue, i)

    if x == 2:
        vuelo["Aerolinea"] = aeroL=input("Ingrese la aerolinea:\n")
        vuelo["HoraSalida"] = int(input("Ingrese la hora de salida (Sistema horario de 24 horas):\n"))
        vuelo["HoraLlegada"] = int(input("Ingrese la hora de llegada (Sistema horario de 24 horas):\n"))
        vuelo["Aeropuerto0"] = str(input("Ingrese el aeropuerto de origen:\n"))
        vuelo["AeropuertoD"] = str(input("Ingrese el aeropuerto destino:\n"))
        vuelo["TipoVuelo"] = str(input("Ingrese el tipo de vuelo(Pasajeros o Carga):\n"))        
        vuelos_llegada.append(vuelo)
        vuelos_llegada = seleccion_atterizaje(vuelos_llegada)
        for i in vuelos_llegada:
            arribo(VueloAtterizaje, i)

    if x == 3:
        barrido(VueloDespegue)


    elif (x == 5):
        print("\nEl programa fue finalizado con éxito.\n")


