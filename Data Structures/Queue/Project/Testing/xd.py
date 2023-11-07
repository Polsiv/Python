# def atender_vuelo(cola_despegues, cola_aterrizajes):
#     if pista:
#         if not cola_vacia(cola_aterrizajes):
#             if not cola_vacia(cola_despegues):
#                 if cola_aterrizajes.frente.info.horaLlegada <= cola_despegues.frente.info.horaSalida:
#                     avion = atencion(cola_aterrizajes)
#                     pista = False
#                     print("Atendiendo vuelo de aterrizaje:", avion.aerolinea, avion.horaLlegada, avion.aeropuertoOrigen, avion.aeropuertoDestino, avion.tipoVuelo)
#                 else:
#                     avion = atencion(cola_despegues)
#                     pista = False
#                     print("Atendiendo vuelo de despegue:", avion.aerolinea, avion.horaSalida, avion.aeropuertoOrigen, avion.aeropuertoDestino, avion.tipoVuelo)
#             else:
#                 avion = atencion(cola_aterrizajes)
#                 pista = False
#                 print("Atendiendo vuelo de aterrizaje:", avion.aerolinea, avion.horaLlegada, avion.aeropuertoOrigen, avion.aeropuertoDestino, avion.tipoVuelo)
#         elif not cola_vacia(cola_despegues):
#             avion = atencion(cola_despegues)
#             pista = False
#             print("Atendiendo vuelo de despegue:", avion.aerolinea, avion.horaSalida, avion.aeropuertoOrigen, avion.aeropuertoDestino, avion.tipoVuelo)
#         else:
#             print("No hay vuelos para atender")
#     return