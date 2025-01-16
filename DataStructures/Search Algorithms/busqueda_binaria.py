def binaria(lista, buscado):
    posicion = -1
    primero = 0
    ultimo = len(lista)-1
    while (primero <= ultimo) and (posicion == -1):
        medio = (primero + ultimo)//2
        if(lista[medio]==buscado):
            posicion = medio
        else:
            if (buscado < lista[medio]):
                ultimo = medio-1
            else:
                primero = medio+1
    print(str(buscado)+" está en la posición "+str(posicion))
    return posicion

listaimpares = [41, 33, 7, 3, 73, 19]
datobusca = 73
print(listaimpares)
binaria(listaimpares, datobusca)
