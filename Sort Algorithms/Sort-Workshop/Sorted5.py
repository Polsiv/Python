

def insercion(lista): 
    for i in range(1, len(lista)+1): 
        k=i-1 

        while (k>0) and (lista[k]["porcentaje"]<lista[k-1]["porcentaje"]): 
            lista[k], lista[k-1] = lista[k-1], lista[k] 
            k -= 1
    return lista
      
def contar_estudiantes_mas_75(estudiantes):
    count = 0
    for estudiante in estudiantes:
        if estudiante["porcentaje"] >= 0.75:
            count += 1
    return count        

estudiantes=[{"usuario":"Trixnar","porcentaje":0.90},
             {"usuario":"Kilts7","porcentaje":0.45},
             {"usuario":"Sbxz","porcentaje":0.75},
             {"usuario":"Polsiv","porcentaje":0.90},
             {"usuario":"Rafiki","porcentaje":0.76},
             {"usuario":"Tyviz","porcentaje":0.50}
]

listaOrdenada=insercion(estudiantes)
#PORCENTAJE MAS ALTO
print("=========================================\n")
porcentajeMasAlto=listaOrdenada[-1]["porcentaje"]
listaMasAltos=[]

for i in listaOrdenada:
    if i["porcentaje"]==porcentajeMasAlto:
        listaMasAltos.append(i)

print(f'Estudiantes con el porcentaje mas alto ({int(listaMasAltos[-1]["porcentaje"]*100)}%) son:')

for z in listaMasAltos:
    print(z["usuario"])
    
print("\n=========================================\n")

#ENLISTADO DE MAYOR A MENOR
for x in reversed(listaOrdenada):
    print(x)
print("\n=========================================\n")

#CANTIDAD DE ESTUDIANTES POR ENCIMA DE 75%
print("La cantidad de estudiantes que tienen mas de 75% son:",contar_estudiantes_mas_75(listaOrdenada),"\n")
print("=========================================\n")