import time
import re

class nodoCola(object):
    info, sig = None, None

class ColaDespegue(object):
    def __init__(self):
        self.frente, self.final=None, None
        self.largo=0

time_obj = time.localtime()
tiempo_actual = time.strftime("%X", time_obj)

def validate_time_format(time_str: str) -> bool:
    pattern = re.compile(r'^([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$')
    return pattern.match(time_str)

def comparar_hora(input_time: str) -> bool:
    return input_time >= tiempo_actual

def arribo(cola,  dato):
    nodo=nodoCola()
    nodo.info=dato
    if cola.frente is None:
        cola.frente=nodo
    else:
        cola.final.sig=nodo
    cola.final=nodo
    cola.largo+=1

def cola_vacia(cola):
    return cola.frente is None

def en_frente_despegue(cola):
    return cola.frente.info.InformacionVueloDespegue()

def en_frente_tipo_despegue(cola):
    return cola.frente.info.TipoVuelo()

def en_frente_hora_despegue(cola):
    return cola.frente.info.HoraSalida()

def largodedespegue(cola):
    return cola.largo

def atencion(cola):
    dato=cola.frente.info
    cola.frente=cola.frente.sig
    if cola.frente is None:
        cola.final=None
    cola.largo-=1
    return dato

def atencion_despegue(cola):
    dato=cola.frente.info
    cola.frente=cola.frente.sig
    if cola.frente is None:
        cola.final=None
    cola.largo-=1
    return dato.InformacionVueloDespegue()

def barrido_despegue(cola):
    caux=ColaDespegue()
    while(not cola_vacia(cola)):
        dato=atencion(cola)
        print(dato.InformacionVueloDespegue())
        arribo(caux,dato)
    while(not cola_vacia(caux)):
        dato=atencion(caux)
        arribo(cola,dato)

def comparar_codigo_despegue(cola, codigo):
    flag = False
    caux=ColaDespegue()
    while(not cola_vacia(cola)):

        dato=atencion(cola)
        if dato.CodigoVuelo() == codigo:
            flag = True
        arribo(caux,dato)
     
    while(not cola_vacia(caux)):
        dato=atencion(caux)
        arribo(cola,dato)
    return flag

def bubble(list):
    for i in range(0, len(list)-1):
        for j in range(0, len(list)-i-1):
            if (list[j].HoraSalida() > list[j + 1].HoraSalida()):
                list[j], list[j + 1] = list[j+1], list[j]
    return list

def acomodar_cola_despegue(cola):
    lista = []
    caux=ColaDespegue()
    while(not cola_vacia(cola)):
        dato=atencion(cola)
        lista.append(dato)

    lista = bubble(lista)
    for i in lista:
        arribo(caux, i)
    while(not cola_vacia(caux)):
        dato=atencion(caux)
        arribo(cola,dato)

def cambiar_hora(cola, codigo):
    caux=ColaDespegue()
    while(not cola_vacia(cola)):

        dato=atencion(cola)
        if dato.CodigoVuelo() == codigo:
            print("Existe el avion")
            hora = str(input("Ingrese la nueva hora de despegue: "))
            while not (validate_time_format(hora) and comparar_hora(hora)):
                hora = str(input("La hora ingresada ya pasó, o el formato no es valido, por favor ingrese otra hora válida: "))
            dato.Horasalida(hora)
        arribo(caux,dato)
     
    while(not cola_vacia(caux)):
        dato=atencion(caux)
        arribo(cola,dato)

def eliminar_despegue(cola, codigo):
    flag = False
    caux = ColaDespegue()
    
    while not cola_vacia(cola):
        dato = atencion(cola)
        if dato.CodigoVuelo() == codigo:
            flag = True
        else:
            arribo(caux, dato)
     
    while not cola_vacia(caux):
        dato = atencion(caux)
        arribo(cola, dato)
    
    return flag