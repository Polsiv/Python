peliculas = [ 
    {'titulo': 'starwars the return of jedi', 'año_estreno':1967, 'recaudacion':1000000, 'valoracion_publico': 4.5},
    {'titulo': 'avengers end game', 'año_estreno':2017, 'recaudacion':230000, 'valoracion_publico': 4.9},
    {'titulo': 'iron man', 'año_estreno':2014, 'recaudacion':7890000, 'valoracion_publico': 5},
    {'titulo': 'fast and avengers', 'año_estreno':2017, 'recaudacion':4500000, 'valoracion_publico': 3},
    {'titulo': 'ironthor', 'año_estreno':2012, 'recaudacion':2000000, 'valoracion_publico': 5},
    {'titulo': 'avengers infinity war', 'año_estreno':2020, 'recaudacion':120000, 'valoracion_publico': 5}
    ]

# ordenar lista

MIN_MERGE = len(peliculas)

def calcMinRun(n):
    
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j]["titulo"] < arr[j - 1]["titulo"]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1



def merge(arr, l, m, r):

    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if left[i]["titulo"] <= right[j]["titulo"]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1

def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)

    size = minRun
    while size < n:

        for left in range(0, n, 2 * size):

            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(arr, left, mid, right)

        size = 2 * size


#=============================TIME SORT (LANZAMIENTO)============================


def insertionSortDos(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j]["año_estreno"] < arr[j - 1]["año_estreno"]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def mergeDos(arr, l, m, r):

    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if left[i]["año_estreno"] <= right[j]["año_estreno"]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1



def timSortDos(arr):
    n = len(arr)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSortDos(arr, start, end)

    size = minRun
    while size < n:

        for left in range(0, n, 2 * size):

            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                mergeDos(arr, left, mid, right)

        size = 2 * size


#=============================TIME SORT (RECAUDACION)============================

def insertionSortTres(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j]["recaudacion"] > arr[j - 1]["recaudacion"]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def mergeTres(arr, l, m, r):

    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if left[i]["recaudacion"] >= right[j]["recaudacion"]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k]= right[j]
            j += 1

        k += 1

    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1

def timSortTres(arr):
    n = len(arr)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSortTres(arr, start, end)

    size = minRun
    while size < n:

        for left in range(0, n, 2 * size):

            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                mergeTres(arr, left, mid, right)

        size = 2 * size


#=============================Imprimir Informacion(Tomas)============================


def imprimir_titulo():
    print("\n=====================Peliculas ordenadas por su titulo============================\n")
    for elemento in peliculas:
        print(f'Titulo: {elemento["titulo"].capitalize()} Año estreno: {elemento["año_estreno"]} Recaudacion: {elemento["recaudacion"]} Valoracion del publico: {elemento["valoracion_publico"]}')

def imprimir_year():
    print("\n=====================Peliculas ordenadas por su lanzamiento============================\n")
    for elementoDos in peliculas:
        print(f'Titulo: {elementoDos["titulo"].capitalize()} Año estreno: {elementoDos["año_estreno"]} Recaudacion: {elementoDos["recaudacion"]} Valoracion del publico: {elementoDos["valoracion_publico"]}')

def imprimir_recaudacion():
    print("\n=====================Peliculas ordenadas por su recaudacion ============================\n")
    for x in peliculas:
        print(f'Titulo: {x["titulo"].capitalize()} Año estreno: {x["año_estreno"]} Recaudacion: {x["recaudacion"]} Valoracion del publico: {x["valoracion_publico"]}')  
            

#Parte sebastian============================================================================================

def secuencialG(lista, buscado):
    posicion = -1
    print("========================Peliculas estrenadas en ",buscado,":==================================\n")
    for i in lista:
        if (i["año_estreno"] == buscado):
            posicion = i
            print(i["titulo"].capitalize())
    if posicion==-1:
        print("No existe en la lista alguna pelicula que se estrenara en: ",buscado)
    return posicion

def secuencialH(lista, buscado):
    posicion = -1
    print("\n========================peliculas que inician con la palabra ",buscado,":========================\n")
    for i in lista:
        if (buscado in i["titulo"]):
            posicion = i
            print(i["titulo"].capitalize())
    if posicion==-1:
        print("No existe en la lista alguna pelicula que inicie con la palabra ",buscado)
    return posicion



# parte silv===================================================================

def secuencial(list, found):
        posicion = -1
        for i in range(0, len(list)):
            if (list[i]["titulo"] == found):
                posicion = i
                print(f'{found.capitalize()} esta en la #{i + 1} posicion')

        if (posicion == -1):
            print("pelicula no encontrada.")

def secuencial1(list, found):
    posicion = -1
    total = 0
    for i in range(0, len(list)):
        if (found in list[i]["titulo"]):
            total+= list[i]["recaudacion"]
            posicion = i
    print("Total recaudado", total)

    if (posicion == -1):
        print("No hay peliculas que tengan la palabra Avengers.")

# parte alejo===================================================================

def secuencialvaloracion(lista, buscado):

    posicion = -1

    for i in range(0, len(lista)):
        if (lista[i]["valoracion_publico"] == buscado):
            posicion = i

            print("Titulo: ", lista[i]["titulo"].capitalize())

    if  posicion == -1:
        print("No se encontro ningua pelicula con valoracion ", buscado)

    return posicion

def secuencialinfinity(lista, buscado):

    posicion = -1

    for i in range(0, len(lista)):
        if (lista[i]["titulo"] == buscado):
            posicion = i
            print(f'Titulo: {lista[i]["titulo"].capitalize()} Año estreno: {lista[i]["año_estreno"]} Recaudacion: {lista[i]["recaudacion"]} Valoracion del publico: {lista[i]["valoracion_publico"]}')

    if  posicion == -1:
        print("No se encontro la pelicula Avengers infity War")

    return posicion

#Menu=======================================================================

x = 0

while x != 9:
    x = int(input("\n--------------Inserta la opcion que quieras-------------\n1) Ordenar listas\n2) Imprimir la pelicula con mayor recaudacion \n3) Impirmir peliculas con fecha de estrenacion determinada \n4) Imprimir peliculas con un inicio de palabra determinado\n5) Imprimir posicion de la pelicula StarWars the return of Jedi \n6) Imprimir cantidad recaudada por las peliculas que contengan la palabra Avengers \n7) Imprimir peliculas con valoracion 5\n8) Imprimir la informacion de la pelicula Avengers infinity war\n9) Salir \n")
)
    if x == 1:
        timSort(peliculas)
        imprimir_titulo()
        timSortDos(peliculas)
        imprimir_year()
        timSortTres(peliculas)
        imprimir_recaudacion()
          
    elif x == 2: 
        imprimir_recaudacion()
        print(f'\nLa pelicula que tuvo mayor recaudacion fue {peliculas[0]["titulo"].capitalize()}, con un total de {peliculas[0]["recaudacion"]}\n')
        
    elif x == 3:
        fechaG= 2017
        secuencialG(peliculas, fechaG)
              
    elif x == 4:
        palabraH="iron"
        secuencialH(peliculas,palabraH.lower())
       
    elif x == 5:
        timSort(peliculas)
        print("\n========================Imprimir la posicion de la pelicula deseada a encontrar (en orden alfabetico)========================")
        finddata = "starwars the return of jedi"
        secuencial(peliculas, finddata.lower())
        
    elif x == 6: 
        print("\n========================Imprimir la cantidad recaudada por las peliculas que contienen la palabra Avengers========================")
        findavengers = "avengers"
        secuencial1(peliculas, findavengers.lower())
    
    elif x == 7:
        datobusca = 5
        print(f'=========================Peliculas con valoracion {datobusca}========================\n')
        secuencialvaloracion(peliculas, datobusca)
      
    elif x == 8:
        datobusca2 = "avengers infinity war"
        print(f'=========================Buscar Infinity war========================\n')
        secuencialinfinity(peliculas, datobusca2.lower())
    
    elif x == 9:
        print("Programa ejecutado.")
