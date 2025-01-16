#SORTING LIST---------------------------------------------------------

def shellSort(array, n):

    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval]["porcentaje"] > temp["porcentaje"]:
                 array[j]= array[j - interval]
                 j -= interval

            array[j] = temp
        interval //= 2

#FINDING THE HIGHEST PERCENTAGE---------------------------------------------------------

def HighestPercentage(array):

    HighestPercentage = array[-1]["porcentaje"]
    HighestPercentages = []
    
    for i in array:
        if(i["porcentaje"] == HighestPercentage):
            HighestPercentages.append(i)

    return(HighestPercentages)


#FIND GREATER THAN 75---------------------------------------------------------
def centinela(lista, buscado):

    CoolStudents = []

    for i in lista:
        if (i["porcentaje"] >= buscado):
            CoolStudents.append(i)
            print(i["usuario"], ":", i["porcentaje"])


    if len(CoolStudents) == 0:
        print("There is not a single student with a percentage higher than 75 :(")
    else:
        return CoolStudents
    

#List---------------------------------------------------------

estudiantes=[{"usuario":"Trixnar","porcentaje":0.95},
             {"usuario":"Kilts7","porcentaje":0.1},
             {"usuario":"Sbxz","porcentaje":0.25},
             {"usuario":"Polsiv","porcentaje":0.20},
             {"usuario":"Rafiki","porcentaje":0.92},
             {"usuario":"Tyviz","porcentaje":0.80}
]

greaterThan = 0.75
shellSort(estudiantes,len(estudiantes))


x = int(input("--------------Enter the option yuu want--------------\n1) Students higher than 75% \n2) Students with the Highest Percentage \n3) Sorted List in inversed order \n4) Leave \n")
)

if x == 1:
    print("-----------Students higher than 75%-----------------")
    centinela(estudiantes, greaterThan)

elif x == 2: 
    print("---------Students with the Highest Percentage------------------")
    for i in HighestPercentage(estudiantes):
        print(i["usuario"], ":", i["porcentaje"])

elif x == 3:
    print("---------Sorted List in inversed order------------------")
    for i in reversed(estudiantes):
        print(i["usuario"], ":", i["porcentaje"])

elif x == 4:
    print("Done")
