class AvionAterrizaje(object):
    def __init__(self, CodigoVuelo, Aerolinea, Horasalida, Horallegada, AeropuertoO, TipoVuelo):
        self._codigovuelo = CodigoVuelo
        self._aerolinea = Aerolinea
        self._horasalida = Horasalida
        self._horallegada = Horallegada
        self._aeropuertoO = AeropuertoO
        self._tipoVuelo = TipoVuelo

    def InformacionVueloAterrizaje(self):
        return f'Codigo del Vuelo: {self._codigovuelo}, Aerolinea: {self._aerolinea}, Hora de salida: {self._horasalida}, Hora de llegada: {self._horallegada}, Aereopuerto de Destino: Alfonzo Bonilla, Aereopuerto Origen: {self._aeropuertoO}, Tipo de Vuelo: {self._tipoVuelo}'

    #@property
    def CodigoVuelo(self):
        return self._codigovuelo

    #@property
    def Aereolinea(self):
        return self._aerolinea

    #@property
    def Horallegada(self):
        return self._horallegada
    
    def Horasalida(self):
        return self._horasalida


    #@property
    def AereopuertoO(self):
        return self._aeropuertoO

    #@property
    def TipoVuelo(self):
        return self._tipoVuelo