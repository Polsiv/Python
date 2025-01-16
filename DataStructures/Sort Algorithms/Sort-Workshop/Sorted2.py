# Lista de los jugadores
plantilla_titular = [
    {'nombre': 'valdes', 'dorsal': 1, 'posicion': 'po'},
    {'nombre': 'alba', 'dorsal': 18, 'posicion': 'li'},
    {'nombre': 'mascherano', 'dorsal': 14, 'posicion': 'dfc'},
    {'nombre': 'pique', 'dorsal': 3, 'posicion': 'dfc'},
    {'nombre': 'alves', 'dorsal': 13, 'posicion':'ld'},
    {'nombre': 'xavi', 'dorsal': 6, 'posicion':'mc'},
    {'nombre': 'busquets', 'dorsal': 5, 'posicion':'md'},
    {'nombre': 'cesc', 'dorsal': 4, 'posicion':'mc'},
    {'nombre': 'iniesta', 'dorsal': 8, 'posicion':'ei'},
    {'nombre': 'messi', 'dorsal': 10, 'posicion':'dc'},
    {'nombre': 'pedro', 'dorsal': 7, 'posicion':'ed'}
]

# Ordenar lista por nombres alfabéticamente
def mergesort(lista):
    if len(lista) <= 1:
        return lista
    
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    izquierda = mergesort(izquierda)
    derecha = mergesort(derecha)
    
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    lista_mezclada = []
    i, j = 0, 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i]['nombre'] < derecha[j]['nombre']:
            lista_mezclada.append(izquierda[i])
            i += 1
        else:
            lista_mezclada.append(derecha[j])
            j += 1
    
    while i < len(izquierda):
        lista_mezclada.append(izquierda[i])
        i += 1
    
    while j < len(derecha):
        lista_mezclada.append(derecha[j])
        j += 1

    return lista_mezclada

ordenado = mergesort(plantilla_titular)

print("\n-----Nombre jugadores ordenados alfabeticamente: \n")
for jugador in ordenado:
    print(jugador)

#ordenar de menor a mayor los dorsales
def mergesortDos(lista):
    if len(lista) <= 1:
        return lista
    
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    izquierda = mergesortDos(izquierda)
    derecha = mergesortDos(derecha)
    
    return mergeDos(izquierda, derecha)

def mergeDos(izquierda, derecha):
    lista_mezclada = []
    i, j = 0, 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i]['dorsal'] < derecha[j]['dorsal']:
            lista_mezclada.append(izquierda[i])
            i += 1
        else:
            lista_mezclada.append(derecha[j])
            j += 1
    
    while i < len(izquierda):
        lista_mezclada.append(izquierda[i])
        i += 1
    
    while j < len(derecha):
        lista_mezclada.append(derecha[j])
        j += 1

    return lista_mezclada

ordenadoDorsal = mergesortDos(plantilla_titular)

print("\n-----Dorsal jugadores ordenados de menor a mayor: \n")
for jugador in ordenadoDorsal:
    print(jugador)  

#Buscar el jugador que ocupa la posicion de portero

def binaria(lista, buscado):
    posicion = -1
    primero = 0
    ultimo = len(lista)-1
    while (primero <= ultimo) and (posicion == -1):
        medio = (primero + ultimo)//2
        if(lista[medio]["posicion"]==buscado):
            posicion = medio
        else:
            if (buscado < lista[medio]["posicion"]):
                ultimo = medio-1
            else:
                primero = medio+1
    if(posicion == -1):
        print("\nNO SE ENCUENTRA EL ELEMENTO\n")
        
    else:
        print("\nJugador a encontrar: ",str(buscado)+" está en la posición "+str(posicion),"\n")
        print(lista[posicion])
   
    
    return posicion
ordenadoPosicion = sorted(plantilla_titular, key=lambda x: x["posicion"])
portero = "po"
print("\n-----Jugadores ordenados respecto a la posicion: \n")
for jugador in ordenadoPosicion:
    print(jugador)
binaria(ordenadoPosicion,portero)
