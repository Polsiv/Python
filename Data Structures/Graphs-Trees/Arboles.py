from Colas import *

class nodoArbol(object):
    #Crea un nodo con la informacion cargada
    def __init__(self, info) :
        self.izq = None
        self.der = None
        self.info = info
        self.altura = 0

#elimina un elemento del arbol y lo devuelve si lo encuentra
def eliminar_nodo(raiz, clave):
    x = None
    
    if (raiz is not None):
        if (clave < raiz.info):
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif (clave > raiz.info):
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info
            
            if(raiz.izq is None):
                raiz = raiz.der
            elif (raiz.der is None):
                raiz = raiz.izq
            else:
                raiz.izq, aux = reemplazar(raiz.izq)
                raiz.info = aux.info

    return raiz, x

#Inserta un dato al arbol
def insertar_nodo(raiz, dato):
    if (raiz is None):
        raiz = nodoArbol(dato)
    elif (dato < raiz.info):
        raiz.izq = insertar_nodo(raiz.izq, dato)
    else:
        raiz.der = insertar_nodo(raiz.der, dato)
    return raiz

#Devuelve true si el arbol esta vacio

def arbolvacio(raiz):
    return raiz is None


#SEGUNDA===========================================================


#determina el nodo que reemplazara al que se elimina
def reemplazar(raiz):
    aux = None
    
    if (raiz.der is None):
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = reemplazar(raiz.der)
    
    return raiz, aux

#realiza el barrido postorden del arbol
def por_nivel(raiz):
    pendientes = Cola()
    arribo(pendientes, raiz)

    while (not cola_vacia(pendientes)):
        nodo = atencion(pendientes)
        print(nodo.info)

        if(nodo.izq is not None):
            arribo(pendientes, nodo.izq)
        if(nodo.der is not None):
            arribo(pendientes, nodo.der)

#devuelve la direccion del elemento buscado
def buscar(raiz, clave):
    pos = None

    if (raiz is not None):
        if (raiz.info == clave):
            pos = raiz
        elif clave < raiz.info:
            pos = buscar(raiz.izq, clave)
        else:
            pos = buscar(raiz.der, clave)
    return pos

#TERCERA===========================================================

#Realiza el barrido inorden del arbol
def inorden(raiz):
    if(raiz is not None):
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)

#realiza el barrido preorden del arbol
def preorden(raiz):
    if (raiz is not None):
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)

#realiza el barrido postorden del arbol
def postorden(raiz):
    if(raiz is not None):
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)
    

#SIG SIG SIG PAGINA===============================================

#devuelve la altura de un nodo
def altura (raiz):
    if (raiz is None):
        return -1
    else:
        return raiz.altura
    
#actualiza la altura de un nodo    
def actualizaraltura(raiz):
    if (raiz is not None):
        alt_izq = altura(raiz.izq)
        alt_der = altura(raiz.der)
        raiz.altura = (alt_izq if alt_izq > alt_der else alt_der) + 1

#Realiza una rotacion simple de nodos a la derecha o a la izquierda
def rotar_simple(raiz, control):
    if control:
        aux = raiz.iqz
        raiz.izq = aux.der
        aux.der = raiz
    else:
        aux = raiz.der
        raiz.der = aux.izq
        aux.izq = raiz
    actualizaraltura(raiz)
    actualizaraltura(aux)

    raiz = aux
    return raiz


#Realiza una rotacion doble de nodos a la derecha o a la izquierdaWWWWAQ        WWWSWWWWQ   SASAAaAaSSSSSSSSSSSSS8732ECXDXSSSXSDCSSA
def rotar_doble(raiz, control):
    if control:
        raiz.izq = rotar_simple(raiz.izq, False)
        raiz = rotar_simple(raiz, True)
    else:
        raiz.der = rotar_simple(raiz.der, True)
        raiz = rotar_simple(raiz, False)
    return raiz

#Determina que rotacion hay que hacer para balancear el arbol
def balancear(raiz):

    if(raiz is not None):
        if(altura(raiz.izq) - altura(raiz.der) == 2):
            if(altura(raiz.izq.izq) >= altura(raiz.izq.der)):
                raiz = rotar_simple(raiz, True)
            else:
                raiz = rotar_doble(raiz, True)
        elif(altura(raiz.der) - altura(raiz.izq) == 2):
            if(altura(raiz.der.der) >= altura(raiz.der.izq)):
                raiz = rotar_simple(raiz, False)
            else:
                raiz = rotar_doble(raiz, False)

    return raiz

#SIG SIG SIG SIG PAGINA===============================================

