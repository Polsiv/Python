from pila import *
import time
import threading

rockola = Pila()
cancion = ""
reproduciendo = False

def reproducir(pila):
    global cancion, reproduciendo

    if not pila_vacia(pila) and not reproduciendo:
        reproduciendo = True
        cancion = desapilar(pila)
        print(f"Reproduciendo: {cancion}")
        print(f"Duración: 5 Segundos")
        t = threading.Thread(target=esperar, args=(cancion,))
        t.start()
    elif reproduciendo:
        print("Ya hay una canción en reproducción. Espere a que termine de reproducirse la canción actual")
    else:
        print("La playlist está vacía.")

def esperar(cancion):
    time.sleep(5)
    print("\n===========================================\n")
    print(f"La canción: {cancion} terminó de ser reproducida")
    print("\n===========================================\n")
    global reproduciendo
    reproduciendo = False

x = 0
while (x != 4):
    try:
        x = int(input("---------Elige la opción a ejecutar---------\n1)Agregar Canción a la Playlist\n2)Reproducir Canción\n3)Ver Playlist.\n4)Salir\n"))
    except ValueError:
        print("El dato ingresado no esta permitido, se esperaba un entero(1-4)")
    if (x == 1):
        cancion = input("Escribe el nombre de la Canción:\n").capitalize()
        artista = input("Escribe el nombre del Artista:\n").capitalize()
        dato = cancion + "-" + artista
        apilar(rockola, dato)
    elif (x == 2):
        print("\n===========================================\n")
        reproducir(rockola)
        print("\n===========================================\n")
    elif (x == 3):
        print("\n===========================================\n")
        verPlaylist(rockola)
        print("\n===========================================\n")
    elif (x == 4):
        print("\nEl programa fue finalizado con éxito.\n")