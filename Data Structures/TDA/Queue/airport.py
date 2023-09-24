from cola import *
despegues=[]

def convertirHoraAMinutos(hora):
    if isinstance(hora, int):
        hora = str(hora)
    hora, minutos = map(int, hora.split(':'))
    totalMinutos = hora * 60 + minutos
    return totalMinutos

def ordenarDespegues():
    global despegues
    despegues=sorted(despegues,key=lambda x: convertirHoraAMinutos(x.horaSalida))

x = 0
while (x != 4):
    try:
        x = int(input("---------Elige la opción a ejecutar---------\n1)Agregar Vuelo de Despegue\n2)Agregar Vuelo de Aterrizaje\n3)Ver Playlist.\n4)Salir\n"))
    except ValueError:
        print("El dato ingresado no esta permitido, se esperaba un entero(1-4)")
    if (x == 1):
        aeroL=input("Ingrese la aerolinea:\n")
        horaS=convertirHoraAMinutos(input("Ingrese la hora de salida (Sistema horario de 24 horas):\n"))
        horaL=convertirHoraAMinutos(input("Ingrese la hora de llegada (Sistema horario de 24 horas):\n"))
        aeropuertoO=str(input("Ingrese el aeropuerto de origen:\n"))
        aeropuertoD=str(input("Ingrese el aeropuerto destino:\n"))
        tipoV=str(input("Ingrese el tipo de vuelo(Pasajeros o Carga):\n"))
        avion=vuelo(aeroL,horaS,horaL,aeropuertoO,aeropuertoD,tipoV)
        
        despegues.append(avion)
        ordenarDespegues()       
    elif (x == 4):
        print("\nEl programa fue finalizado con éxito.\n")