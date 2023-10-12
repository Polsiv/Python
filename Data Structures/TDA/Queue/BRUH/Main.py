#Hecho por: Juan Pablo Silvestre, Sebastián López, Tomás Mancera, Alejandro Salazar Tovar


from AvionesDespegue import *
from AvionesAterrisaje import *
from ColaDespegue import *
from ColaAterrizaje import *
import time
import re


time_obj = time.localtime()
tiempo_actual = time.strftime("%X", time_obj)
ColaDespegues, ColaAterrizajes = ColaDespegue(), ColaAterrizaje()


def esperar_aterrizaje(tipo):
    if(tipo == "Carga"): time.sleep(12)
    else: time.sleep(10)
    print(f'{"="*20}\nAterrizaje exitoso!\n{"="*20}\n')

def esperar_despegue(tipo):
    if(tipo == "Carga"): time.sleep(9)
    else: time.sleep(5)
    print(f'{"="*20}\nVuelo exitoso!\n{"="*20}\n')

def validate_time_format(time_str: str) -> bool:
    pattern = re.compile(r'^([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$')
    return pattern.match(time_str)
      
def comparar_hora(input_time: str) -> bool:
    return input_time >= tiempo_actual

def atender_vuelo(cola_despegues, cola_aterrizajes):
 
    if not cola_vacia(cola_aterrizajes):
        if not cola_vacia(cola_despegues):
            if en_frente_hora_aterrizaje(cola_aterrizajes) <= en_frente_hora_despegue(cola_despegues):
                print(f'Atendiendo vuelo atterizaje:[ {en_frente(cola_aterrizajes)}]')
                esperar_aterrizaje(atencion_Aterrizaje(cola_aterrizajes))
            else:
                print(f'Atendiendo vuelo despegue: [{en_frente_despegue(cola_despegues)}]')
                esperar_despegue(atencion_despegue(cola_despegues))
   
        else:
            print(f'Atendiendo vuelo atterizaje:[ {en_frente(cola_aterrizajes)}]')
            esperar_aterrizaje(atencion_Aterrizaje(cola_aterrizajes))
        
                 
    elif not cola_vacia(cola_despegues):
        print(f'Atendiendo vuelo despegue: [{en_frente_despegue(cola_despegues)}]')
        esperar_despegue(atencion_despegue(cola_despegues))
           
    else:
        print("No hay vuelos para atender")
    return

def crear_vuelo_despegue(): 
    Aereolinea = input("Ingrese la aereolínea: ")
    HoraSalida = str(input("Ingrese la hora de salida: "))
    while not (validate_time_format(HoraSalida) and comparar_hora(HoraSalida)):
        HoraSalida = str(input("La hora ingresada ya pasó, o el formato no es valido, por favor ingrese otra hora válida: "))

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
    Codigovuelo = int(input("Ingrese el código de vuelo: "))
    if not cola_vacia(ColaDespegues):
        while comparar_codigo_despegue(ColaDespegues, Codigovuelo):
            Codigovuelo = int(input(" El código ya existe, por favor ingrese otro código de vuelo: "))
    AvionesDespegue = AvionDespegue(Codigovuelo, Aereolinea, HoraSalida, AereopuertoD, TipoVuelo)
    arribo(ColaDespegues, AvionesDespegue)
    acomodar_cola_despegue(ColaDespegues)

def crear_vuelo_aterrisaje():
    Aereolinea = input("Ingrese la aereolinea: ")
    Horallegada = str(input("Ingrese la hora de llegada: "))
    while not (validate_time_format(Horallegada) and comparar_hora(Horallegada)):
        Horallegada = str(input("La hora ingresada ya pasó, o el formato no es valido, por favor ingrese otra hora válida: "))
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
    if not cola_vacia(ColaAterrizajes):
        while comparar_codigo_aterrizaje(ColaAterrizajes, Codigovuelo):
            Codigovuelo = int(input(" El código ya existe, por favor ingrese otro código de vuelo: "))
    AvionesAterrisaje = AvionAterrisaje(Codigovuelo, Aereolinea, Horallegada, AereopuertoO, TipoVuelo)
    arribo(ColaAterrizajes, AvionesAterrisaje)
    acomodar_cola_aterrizaje(ColaAterrizajes)

def menu():
    apagar = True
    x = 0
    while (apagar): 
        try:
            x = int(input("---------Elige la opción a ejecutar---------\n1)Agregar Vuelo de Despegue\n2)Agregar Vuelo de Aterrizaje\n3)mostrar cola Avión\n4)Modificar hora de salida\n5)Controlar aviones\n6)Cancelar vuelo de despegue\n7)Salir\n"))
        except ValueError:
            print("El dato ingresado no esta permitido, se esperaba un entero(1-5)")

        if x == 1: crear_vuelo_despegue()
        elif x == 2: crear_vuelo_aterrisaje()
        elif x == 3: 
            y = int(input("Elige el tipo de cola: \n1)Despegue. \n2)Atterizaje.\n"))
            if y == 1: barrido_despegue(ColaDespegues)
            elif y == 2: barrido_aterrizaje(ColaAterrizajes)
            else: print("Número ingresado no válido")
        elif x == 4:
            codigo = int(input("Ingrese el código del avión a modificar: "))
            cambiar_hora(ColaDespegues, codigo)
            acomodar_cola_despegue(ColaDespegues)
        elif x == 5:
            atender_vuelo(ColaDespegues, ColaAterrizajes)
        elif x == 6:
            codigo = int(input("Ingrese el código del avión a modificar: "))
            if eliminar_despegue(ColaDespegues, codigo):
                print("Se eliminó el vuelo")
            else:
                print("No existe el vuelo")
        elif x == 7: 
            print("Gracias por su uso")
            apagar = False
        else:
            print("Opcion no valida")

menu()