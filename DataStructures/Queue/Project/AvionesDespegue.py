class AvionDespegue(object):
    def __init__(self, CodigoVuelo, Aerolinea, Horasalida, Horallegada, AeropuertoD, TipoVuelo):
        self._codigovuelo = CodigoVuelo
        self._aerolinea = Aerolinea
        self._horasalida = Horasalida
        self._horallegada = Horallegada
        self._aeropuertoD = AeropuertoD
        self._tipoVuelo = TipoVuelo

    #@property
    def CodigoVuelo(self):
        return self._codigovuelo

    #@property
    def Aereolinea(self):
        return self._aerolinea

    #@property
    def HoraSalida(self):
        return self._horasalida

    def HoraLlegada(self):
        return self._horallegada

    #@property
    def AereopuertoD(self):
        return self._aeropuertoD

    #@property
    def TipoVuelo(self):
        return self._tipoVuelo

    #@HoraSalida.setter
    def Horasalida(self, horasalida):
        self._horasalida = horasalida


    def InformacionVueloDespegue(self):
        return f'Código del Vuelo: {self._codigovuelo}, Aerolínea: {self._aerolinea}, Hora de salida: {self._horasalida}, Hora de llegada: {self._horallegada} Aereopuerto de Origen: Alfonso Bonilla, Aereopuerto Destino: {self._aeropuertoD}, Tipo de Vuelo: {self._tipoVuelo}'