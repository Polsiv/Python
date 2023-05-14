
multiplication = lambda x, y: x * y
add = lambda x, y: x + y
subtract = lambda x, y: x - y
divide = lambda x, y: x / y

operations = {"*": multiplication,
               "/": divide,
               "+": add,
               "-": subtract
               }


def analizador(ecuacion: str):
    equationSolved = ecuacion[:ecuacion.find("=") - 1].split(" ")
    print(equationSolved)

    for operation in operations.keys():
        index = 0
        while index < len(equationSolved):
            if len(equationSolved) == 1:
                break 

            if equationSolved[index] == operation:
                print(ecuacion)
                
                result = operations[operation](int(equationSolved[index - 1]), int(equationSolved[index + 1]))
                element_to_be_replaced = " ".join(equationSolved[index - 1: index + 2])

                ecuacion = ecuacion.replace(element_to_be_replaced, str(result))

                equationSolved = ecuacion[:ecuacion.find("=") - 1].split(" ")
                index = 0
            else:
                index += 1

    print(ecuacion)


def main():
    ecuacion = input("Ingresa la ecuacion a resolver: ")
    analizador(ecuacion)

main()
