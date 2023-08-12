listaPersonajes=["darth vader","yoda","chewbacca","r2-d2","anakin skywalker","hera syndulla","luke skywalker"]
# Ordenamiento
print(f'Lista normal: {listaPersonajes}')
def mergesort(lista):
    if(len(lista)<=1):
        return lista
    else:
        medio=len(lista)//2
        izquierda=[]
        for i in range(0, medio):
            izquierda.append(lista[i])
        derecha=[]
        for i in range(medio, len(lista)):
            derecha.append(lista[i])
        izquierda=mergesort(izquierda)
        derecha=mergesort(derecha)
        if(izquierda [medio-1]<= derecha[0]):
            izquierda+=derecha
            return izquierda
        resultado=merge(izquierda, derecha)
        return resultado

def merge(izquierda, derecha):
    lista_mezclada=[]
    while (len(izquierda)>0) and (len(derecha)>0):
        if(izquierda [0] <derecha[0]):
            lista_mezclada.append(izquierda.pop(0))
        else:
            lista_mezclada.append(derecha.pop(0))
    if(len(izquierda)>0):
        lista_mezclada +=izquierda
    if(len(derecha)>0):
        lista_mezclada +=derecha
    #print(lista_mezclada)
    return lista_mezclada
        
# Llamado a la funcion (para ordenar la lista en orden alfabetico)
print("Orden alfabetico:============================================")
listaOrdenada = mergesort(listaPersonajes)
print(listaOrdenada, "Lista ordenada", "\n")

def secuencial(lista, buscado):
    posicion = -1

    for i in range(0, len(lista)):
        #print(i)
        if (lista[i] == buscado):
            posicion = i
            print(str(buscado)+" Sí existe, está en la posición "+str(posicion))
    if(not(buscado in lista)):
        print(str("Personaje no existe"))
        
      
            
    return posicion


datobusca = "darth maul"
print("Personaje a buscar:============================================")
secuencial(listaOrdenada, datobusca)
print("\n")

# Listar todos los personajes que comienzan con la letra L


def secuencialUno(lista, buscado):
    posicion = -1
    listL = []

    for i in range(0, len(lista)):
        #print(i)
        if (lista[i].startswith(buscado) == True):
            posicion = i
            nombre=[]
            nombre=lista[i]
    return nombre

test = 'l'
print("Personaje a Con la letra L: ============================================")
print("los personajes iniciados en l: ",secuencialUno(listaOrdenada, test))

#Mostrar la informacion de los personajes que se encuentran antes y despues de Hera Syndulla
def secuencialDos(lista, buscado):
    posicion = -1

    for i in range(0, len(lista)):
        #print(i)
        if (lista[i] == buscado):
            posicion = i
            print(str(buscado)+" está en la posición: "+str(posicion)+"============================================")
            print(str(buscado)+" tiene a la izquierda a "+str(lista[posicion-1]))
            print(str(buscado)+" tiene a la derecha a "+str(lista[posicion+1]))
          
    return posicion


datobusca = "hera syndulla"
print(listaOrdenada)
print("\n")
secuencialDos(listaOrdenada, datobusca)






