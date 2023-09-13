def dia_semana(dia, mes, año):
    ajuste = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if mes < 3:
        año -= 1
    return (año + año//4 - año//100 + año//400 + ajuste[mes-1] + dia) % 7

def imprimir_mes(año, mes, dias):
    calendario = list(range(1, dias+1))
    calendario = [''] * dia_semana(1, mes, año) + calendario \
                + [''] * (6 - dia_semana(dias, mes, año))
    print('Do Lu Ma Mi Ju Vi Sa')
    for i in range(0, len(calendario), 7):
        semana = calendario[i:i+7]
        print(('{: >2} '*7).format(*semana))

imprimir_mes(2023, 9, 30)
print()
imprimir_mes(2023, 10, 31)
print()
imprimir_mes(2024, 2, 29)