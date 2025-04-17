# Componente base (interfazs0)
class Medidor:
    def operar(self):
        pass
    
# Componente concreto
class MedidorBasico(Medidor):
    def operar(self):
        return "Medidor funcionando."

# decorador base
class MedidorDecorator(Medidor):
    _medidor: Medidor = None
    
    def __init__(self, medidor: Medidor):
        self._medidor = medidor
        
    def operar(self):
        return self._medidor.operar()
    
# Decorador concreto (monitoreo)
class MonitoreoDecorator(MedidorDecorator):
    def operar(self):
        return f"{super().operar()} Enviado alertas por consumo excesivo."
    
# Decorador concreto (alertas)
class AlertaDecorator(MedidorDecorator):
       def operar(self):
            return f"{super().operar()} Enviando alertas por consumo excesivo."


# Ajuste automatico
class AjusteAutomaticoDecorator(MedidorDecorator):
    def operar(self):
        return f"{super().operar()} Ajustando suministro según patrones de uso."


def main():
    medidor = MedidorBasico()
    medidor = MonitoreoDecorator(medidor)
    medidor = AlertaDecorator(medidor)
    medidor = AjusteAutomaticoDecorator(medidor)
    print(medidor.operar())
    
    
if __name__ == "__main__":
    main()