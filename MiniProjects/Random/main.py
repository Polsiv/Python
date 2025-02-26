
multiplication = lambda x, y: x * y
add = lambda x, y: x + y
subtract = lambda x, y: x - y
divide = lambda x, y: x / y

operations = {"*": multiplication,
               "/": divide,
               "+": add,
               "-": subtract
               }


def analizador(ecuation: str):
    equationSolved = ecuation[:ecuation.find("=") - 1].split(" ")
    print(equationSolved)

    for operation in operations.keys():
        index = 0
        while index < len(equationSolved):
            if len(equationSolved) == 1:
                break 

            if equationSolved[index] == operation:
                print(ecuation)
                
                result = operations[operation](int(equationSolved[index - 1]), int(equationSolved[index + 1]))
                element_to_be_replaced = " ".join(equationSolved[index - 1: index + 2])

                ecuation = ecuation.replace(element_to_be_replaced, str(result))

                equationSolved = ecuation[:ecuation.find("=") - 1].split(" ")
                index = 0
            else:
                index += 1  

    print(ecuation)


def main():
    ecuation = input("Enter the equation to solve: ")
    analizador(ecuation)

main()
