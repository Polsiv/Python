import time
import threading

pista = True



def crear_vuelo_despegue():
    print("atendiendo vuelo")
    time.sleep(5)
    print("despegue con exito")

def crear_vuelo_aterrisaje():
    print("xd")

def barrido_despegue():
    print("xd")

def barrido_aterrizaje():
    print("xd")

def atender_vuelo():
    global pista
    if pista:
        
        print("atendiendo vuelo")
        pista = False
        t = threading.Thread(target=esperar)
        t.start()
    elif not pista: print("se esta atendiendo un vuelo")
    else: print("No hay vuelos")

    
def esperar():
    global pista
    time.sleep(6)
    print("vuelo con exito")
    pista = True
    
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
            if y == 1: barrido_despegue()
            elif y == 2: barrido_aterrizaje()
            else: print("Número ingresado no válido")
        elif x == 4:
            codigo = int(input("Ingrese el codigo del avion a modificar: "))
        elif x == 5:
            atender_vuelo()
        elif x == 7: 
            print("Gracias por su uso")
            apagar = False
        else:
            print("Opcion no valida")

menu()