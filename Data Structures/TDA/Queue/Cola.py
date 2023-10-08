class Vuelo(object):
    def __init__(self, Aerolinea, Horasalida, Horallegada, AeropuertoD, TipoVuelo):
        self.aerolinea = Aerolinea
        self.horasalida = Horasalida
        self.horallegada = Horallegada
        self.aeropuertoD = AeropuertoD
        self.tipoVuelo = TipoVuelo

class nodoCola(object):
    info, sig = None, None

class Cola(object):
    def __init__(self):
        self.frente, self.final=None, None
        self.tamano=0

def arribo(cola,dato):
    nodo=nodoCola()
    nodo.info=dato
    if cola.frente is None:
        cola.frente=nodo
    else:
        cola.final.sig=nodo
    cola.final=nodo
    cola.tamano+=1
   

def cola_vacia(cola):
    return cola.frente is None

def en_frente(cola):
    return cola.frente.info

def tamano(cola):
    return cola.tamano

def atencion(cola):
    dato=cola.frente.info
    cola.frente=cola.frente.sig
    if cola.frente is None:
        cola.final=None
    cola.tamano-=1
    return dato

def barrido(cola):
    caux=Cola()
    while(not cola_vacia(cola)):
        dato=atencion(cola)
        print(f'Aerolinea: {dato.aerolinea}, Hora de salida: {dato.horasalida}, Hora de llegada: {dato.horallegada}, Aeropuerto de Origen: Alfonso Bonilla, Aeropuerto de destino: {dato.aeropuertoD}, Tipo de vuelo: {dato.tipoVuelo}')

        arribo(caux,dato)
    while(not cola_vacia(caux)):
        dato=atencion(caux)
        arribo(cola,dato)