def imprimirCalendario():
    # Pedir al usuario el día de la semana en que comienza Enero de 2021.
    primer_dia_enero_2021 = int(input("Ingrese el día de la semana en que comienza Enero de 2021 (0 para Lunes, 1 para Martes, etc.): "))

    # Asegurarse de que el valor ingresado esté en el rango de 0 a 6.
    if primer_dia_enero_2021 < 0 or primer_dia_enero_2021 > 6:
        print("El valor ingresado no es válido. Debe ser un número del 0 al 6.")
    else:
        años = [2021, 2022, 2023]
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        dias = ["L", "M", "Mi", "J", "V", "S", "D"]
        formatoDias = []
        # Este ciclo For es para darle un nuevo formato a los dias de la semana para que cada uno tenga un ancho de 3 caracteres.
        for dia in dias:
                formatoDia = dia.rjust(3)
                formatoDias.append(formatoDia)

        # Inicializamos el día de la semana en el valor ingresado.
        dia_semana = primer_dia_enero_2021

        for año in años:
            print("-" * 28)
            print(f"{' ' * 7}{año}")
            print("-" * 28)

            for mes in meses:
                print(f"{' ' * 9}{mes}")

                if mes in ["Enero", "Marzo", "Mayo", "Julio", "Agosto", "Octubre", "Diciembre"]:
                    dias_mes = []
                    for i in range (1, 32):
                        dias_mes.append(i)

                elif mes == "Febrero":
                    dias_mes = []
                    for i in range (1, 29):
                        dias_mes.append(i)

                else:
                    dias_mes = []
                    for i in range (1, 31):
                        dias_mes.append(i)

                # Crear arreglos para las semanas del mes
                semanas = [[], [], [], [], []]  # 5 semanas, cada una inicialmente vacía

                # Ajustar las semanas según el día de la semana en que comienza el mes
                for i in range(dia_semana):
                    semanas[0].append(" ")  # Agregar espacios en blanco al principio de la primera semana

                # Llenar las semanas con números de días
                for dia in dias_mes:
                    if len(semanas[0]) < 7:
                        semanas[0].append(dia)
                    else:
                        # Si la primera semana está llena, mover los números a las semanas siguientes
                        for semana in semanas:
                            if len(semana) < 7:
                                semana.append(dia)
                                break

                # Imprime los días de la semana con formato adecuado
                print(" ".join(formatoDias))

                # Imprimir los números de los días de cada semana
                for semana in semanas:
                    semana_str = []  # Creamos una lista vacía para almacenar los números de día formateados
                    for dia in semana:
                        numero_formateado = str(dia).rjust(3)
                        semana_str.append(numero_formateado)  # Agregamos el número formateado a la lista semana_str

                    # Imprimimos la fila de días formateados como una cadena
                    print(" ".join(semana_str))

                print("-" * 28)

                # Calcular el día de la semana en el que comienza el siguiente mes
                dia_semana = (dia_semana + len(dias_mes)) % 7
    

imprimirCalendario()