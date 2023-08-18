#Alphabetic order
def insercion(list):
    for i in range(1, len(list)+1):
        k=i-1
        while (k>0) and (list[k]["name"]<list[k-1]["name"]):
            list[k]["name"], list[k-1]["name"] = list[k-1]["name"], list[k]["name"]
            k -= 1

    print("-------Sorted in alphabetic order:---------")
    for i in range(len(list)):
        print(list[i]["name"])

#Find the Position of the Company

def sequential(list, found):
    posicion = -1
    for i in range(0, len(list)):
        if(list[i]["CompanyPosition"] == found):
            posicion = i
            print(f'---------{found} found at: {posicion+1}---------')   
    if(posicion == -1):
        print("-----Not found------")


#Sort codes 
def inserction1(list):
    for i in range(1, len(list)+1):
        k=i-1
        while (k>0) and (list[k]["code"]<list[k-1]["code"]):
            list[k]["code"], list[k-1]["code"] = list[k-1]["code"], list[k]["code"]
            k -= 1

    print("-------Sorted in incremental order:---------")
    for i in range(len(list)):
        print(f'{list[i]["name"]}: {list[i]["code"]}')
    

Employes = [
    {"name": "Juan Pérez", "code": 23456, "CompanyPosition": "Gerente General"},
    {"name": "María López", "code": 80192, "CompanyPosition": "Jefe de Ventas"},
    {"name": "Carlos García", "code": 56789, "CompanyPosition": "Contador"},
    {"name": "Ana Martínez", "code": 12345, "CompanyPosition": "Asistente Admin"},
    {"name": "Luis Torres", "code": 67890, "CompanyPosition": "Director Ejecutivo"},
    {"name": "Laura Ramírez", "code": 43210, "CompanyPosition": "Ingeniero"},
    {"name": "Andrés Cruz", "code": 98765, "CompanyPosition": "Marketing"},
    {"name": "Sofia rojas", "code": 34567, "CompanyPosition": "Analista de TI"}
]

toFind = "Director Ejecutivo"
insercion(Employes)
sequential(Employes, toFind)
inserction1(Employes)


