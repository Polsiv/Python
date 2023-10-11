from AvionesDespegue import *
from AvionesAterrisaje import *
from ColaDespegue import *
from ColaAterrisaje import *
import time
import re


time_obj = time.localtime()
tiempo_actual = time.strftime("%X", time_obj)
ColaDespegues, ColaAterrisajes = ColaDespegue(), ColaAterrisaje()
print(tiempo_actual)
pista = True



def validate_time_format(time_str):
    pattern = re.compile(r'^([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$')
    if pattern.match(time_str):
        return True
    else:
        return False
    

def comparar_hora(input: str) -> bool:
    if input > tiempo_actual: return False
    else: return True

#def analizar_pista():
    #return ""


def crear_vuelo_despegue(): 
    Aereolinea = input("Ingrese la aereolínea: ")
    HoraSalida = str(input("Ingrese la hora de salida: "))
    while(comparar_hora(HoraSalida)):
        HoraSalida = str(input("La hora ingresada ya pasó, por favor ingrese otra hora válida: "))

    AereopuertoD = input("Ingrese el aereopuerto de destino: ")
    print("Ingrese el tipo de vuelo: ")
    controlador = True
    while(controlador):
        x = int(input("1. Carga\n2. Persona\n"))
        if x == 1: 
            TipoVuelo = "Carga"
            controlador = False
        elif x == 2:
            TipoVuelo = "Persona"
            controlador = False
        else:
            print("Opción no válida")
    Codigovuelo = int(input("Ingrese el cádigo de vuelo: "))
    if not cola_vacia(ColaDespegues):
        while comparar_codigo_despegue(ColaDespegues, Codigovuelo):
            Codigovuelo = int(input(" El código ya existe, por favor ingrese otro código de vuelo: "))
    AvionesDespegue = AvionDespegue(Codigovuelo, Aereolinea, HoraSalida, AereopuertoD, TipoVuelo)
    arribo(ColaDespegues, AvionesDespegue)
    acomodar_cola_despegue(ColaDespegues)

def crear_vuelo_aterrisaje():
    Aereolinea = input("Ingrese la aereolinea: ")
    Horallegada = str(input("Ingrese la hora de llegada: "))
    AereopuertoO = input("Ingrese el aereopuerto de origen: ")
    controlador = True
    while(controlador):
        x = int(input("1. Carga\n2. Persona\n"))
        if x == 1: 
            TipoVuelo = "Carga"
            controlador = False
        elif x == 2:
            TipoVuelo = "Persona"
            controlador = False
        else:
            print("Opción no válida")
    Codigovuelo = int(input("Ingrese el código de vuelo: "))
    if not cola_vacia(ColaAterrisajes):
        while comparar_codigo_aterrizaje(ColaAterrisajes, Codigovuelo):
            Codigovuelo = int(input(" El código ya existe, por favor ingrese otro código de vuelo: "))
    AvionesAterrisaje = AvionAterrisaje(Codigovuelo, Aereolinea, Horallegada, AereopuertoO, TipoVuelo)
    arribo(ColaAterrisajes, AvionesAterrisaje)
    acomodar_cola_aterrizaje(ColaAterrisajes)

def menu():
    apagar = True
    x = 0
    while (apagar): 
        try:
            x = int(input("---------Elige la opción a ejecutar---------\n1)Agregar Vuelo de Despegue\n2)Agregar Vuelo de Aterrizaje\n3)mostrar cola Avión\n4)Modificar hora de salida\n5)Salir\n"))
        except ValueError:
            print("El dato ingresado no esta permitido, se esperaba un entero(1-5)")

        if x == 1: crear_vuelo_despegue()
        if x == 2: crear_vuelo_aterrisaje()
        if x == 3: 
            y = int(input("Elige el tipo de cola: \n1)Despegue. \n2)Atterizaje.\n"))
            if y == 1: barrido(ColaDespegues) 
            elif y == 2: barrido(ColaAterrisajes)
            else: print("Número ingresado no válido")
        if x == 4:
            codigo = int(input("Ingrese el codigo del avion a modificar: "))
            cambiar_hora(ColaDespegues, codigo)
            acomodar_cola_despegue(ColaDespegues)
        if x == 5: 
            print("Gracias por su uso")
            apagar = False

menu()