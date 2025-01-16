def centinelaw(lista, buscado):
    posicion = -1
    i=0
    while (i<len(lista)) and (posicion==-1):
        # print(i)
        if (lista[i] == buscado):
            posicion = i
        i +=1
    print(str(buscado)+" está en la posición "+str(posicion))
    return posicion

listaimpares = [41, 33, 7, 27, 73, 19]
datobusca = 27
print(listaimpares)
centinelaw(listaimpares, datobusca)
