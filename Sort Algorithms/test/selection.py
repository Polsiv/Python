def seleccion(lista):
    for i in range(0, len(lista) - 1):
        minimo = i
        for j in range(i + 1, len(lista)):
            if (lista[j] < lista[minimo]):
                minimo = j

        lista[i], lista[minimo] = lista[minimo], lista[i]
    print(lista)


listaimpares = [11, 3, 81, 7, 45]
seleccion(listaimpares)