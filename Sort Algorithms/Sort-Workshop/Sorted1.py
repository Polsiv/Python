 # Valor historico definido en una escala de 1 a 10
artefactos = [
    {"nombre": "La Máscara de Tutankamón", "valor_historico": 10},
    {"nombre": "El Código de Hammurabi", "valor_historico": 9},
    {"nombre": "El Manuscrito de Voynich", "valor_historico": 8},
    {"nombre": "Los Rollos del Mar Muerto", "valor_historico": 10},
    {"nombre": "Cuenco de travertino", "valor_historico": 9},
    {"nombre": "La Piedra Rosetta", "valor_historico": 10},
    {"nombre": "El Mecanismo de Anticitera", "valor_historico": 7}
]
# Ordenar la lista de manera descendente segun su valor historico
def seleccion(lista):
    for i in range(0, len(lista) - 1):
        maximo = i
        for j in range(i + 1, len(lista)):
            if (lista[j]["valor_historico"] > lista[maximo]["valor_historico"]):
                maximo = j

        lista[i], lista[maximo] = lista[maximo], lista[i]
    print("\n----Lista ordenada: \n")
    print(f"{lista}")     
    

seleccion(artefactos)
    

#Buscar los 3 artefactos de mayor valor historico

def centinela(lista, buscado):
    datos = []
    posicion = -1
    for i in range(0, len(lista)):
       
        if (lista[i]["valor_historico"] == buscado and len(datos) <=2):
            posicion = i
            datos.append(lista[posicion])
           
    print("\n-----Artefactos con mayor valor historico: \n")            
    print(datos)
    return posicion


datobusca = 10

centinela(artefactos, datobusca)

# Mostrar los elementos que preceden a "cuenco de travertino"
def centinelaDos(lista, buscado):
    inicio = 0
    listaDatos = []
    listaDatosFinales = []
    posicion = -1
    for i in range(0, len(lista)):
       
        if (lista[i]["nombre"].lower() == buscado.lower()):
            posicion = i
            print("\n-----",str(buscado)+" está en la posición "+str(posicion),"\n")
            print("Elementos que preceden: \n")
            listaDatos = lista[inicio:posicion]
            print(listaDatos)
            print("\nElementos que siguen en la lista: \n")
            listaDatosFinales.append(lista[posicion+1:len(lista)])
            print(listaDatosFinales)
            print("\n")
            
            
    return posicion


datoBuscar = "cuenco de travertino"

centinelaDos(artefactos, datoBuscar)





