from AvionesDespegue import *
from AvionesAterrisaje import *
from ColaDespegue import *
from ColaAterrisaje import *

ColaDespegues, ColaAterrisajes = ColaDespegue(), ColaAterrisaje()

def crear_vuelo_despegue(): 
    Aereolinea = input("Ingrese la aereolinea: ")
    HoraSalida = int(input("Ingrese la hora de salida: "))
    AereopuertoD = input("Ingrese el aereopuerto de destino: ")
    TipoVuelo = input("Ingrese el tipo de vuelo: ")
    Codigovuelo = int(input("Ingrese el codigo de vuelo: "))
    
    while CompararCodigoDespegue(ColaDespegues, Codigovuelo):
        int(input(" El codigo ya existe, por favor ingrese otro codigo de vuelo: "))

    AvionesDespegue = AvionDespegue(Codigovuelo, Aereolinea, HoraSalida, AereopuertoD, TipoVuelo)
    arribo(ColaDespegues, AvionesDespegue)
    

def crear_vuelo_aterrisaje():
    Codigovuelo = int(input("Ingrese el codigo de vuelo: "))
    Aereolinea = input("Ingrese la aereolinea: ")
    Horalleaga = int(input("Ingrese la hora de llegada: "))
    AereopuertoO = input("Ingrese el aereopuerto de Origen: ")
    TipoVuelo = input("Ingrese el tipo de vuelo: ")
    AvionesAterrisaje = AvionAterrisaje(Codigovuelo, Aereolinea, Horalleaga, AereopuertoO, TipoVuelo)
    arribo(ColaAterrisajes, AvionesAterrisaje)

def menu():
    apagar = True
    x = 0
    while (apagar): 
        try:
            x = int(input("---------Elige la opción a ejecutar---------\n1)Agregar Vuelo de Despegue\n2)Agregar Vuelo de Aterrizaje\n3)mostrar cola Avión\n4)Reprogramar Vuelo\n5)Salir\n"))
        except ValueError:
            print("El dato ingresado no esta permitido, se esperaba un entero(1-5)")

        if x == 1: crear_vuelo_despegue()
        if x == 2: crear_vuelo_aterrisaje()
        if x == 3: 
            y = int(input("Elige el tipo de cola: \n1)Despegue. \n2)Atterizaje."))
            if y == 1: barrido(ColaDespegues) 
            elif y == 2: barrido(ColaAterrisajes)
            else: print("Número ingresado no válido")
        if x == 4:
            #codigo = int(input("Ingrese el codigo del vuelo a reprogramar: "))
            print(largodedespegue(ColaDespegues))
                
        if x == 5: 
            print("Gracias por su uso")
            apagar = False

menu()