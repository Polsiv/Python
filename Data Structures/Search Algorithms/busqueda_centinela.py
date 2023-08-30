def centinela(lista, buscado):
    posicion = -1
    for i in range(0, len(lista)):
        # print(i)
        if (lista[i] == buscado):
            posicion = i
            print(str(buscado)+" está en la posición "+str(posicion))
            break
    return posicion

listaimpares = [41, 33, 7, 27, 73, 19]
datobusca = 27
print(listaimpares)
centinela(listaimpares, datobusca)
