import random

class nodoPila(object):
    info,sig=None, None

class Pila(object):
    def __init__(self):
        self.cima=None
        self.tamano=0

def apilar(pila,dato):
    nodo=nodoPila()
    nodo.info=dato
    nodo.sig=pila.cima
    pila.cima=nodo
    pila.tamano+=1

def desapilar(pila):
    x=pila.cima.info
    pila.cima=pila.cima.sig
    pila.tamano-=1
    return x

def pila_vacia(pila):
    return pila.cima is None

def en_cima(pila):
    if pila.cima is not None:
        return pila.cima.info
    else:
        return None

def tamano(pila):
    return pila.tamano

def barrido(pila):
    paux=Pila()
    while(not pila_vacia(pila)):
        dato=desapilar(pila)
        print(dato)
        apilar(paux,dato)
    while(not pila_vacia(paux)):
        dato=desapilar(paux)
        apilar(pila,dato)

def barrido_modificado(pila):
    list_barrido = []
    paux=Pila()
    while(not pila_vacia(pila)):
        dato=desapilar(pila)
        list_barrido.append(dato)
        apilar(paux,dato)
    while(not pila_vacia(paux)):
        dato=desapilar(paux)
        apilar(pila,dato)

    return list_barrido

def act_flip(pila):

    flip_position = random.randint(2, 5)
    pos = 0
    list = []
    while(pos != flip_position):
        list.append(desapilar(pila))
        pos +=1

    print(f'flip at: {5 - flip_position}')
    for i in list:
        apilar(pila, i)
    
    return barrido_modificado(pila), (5 - flip_position)
    
