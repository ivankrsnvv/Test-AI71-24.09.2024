#  1 символ 5 байт
try:
    weight = int(input('Введите кол-во байт в 1-ом символе')) #  5
    symbhols = int(input('Введите кол-во символов на строке')) #  112
    line = int(input('Введите кол-во строк'))  #  64
    doublу_sided_printing = input('двухсторонняя печать? (Y/N)')
    if doublу_sided_printing == 'Y' or doublу_sided_printing == 'y':
        print((symbhols * weight+line * weight) * 2)
    elif doublу_sided_printing == 'N' or doublу_sided_printing == 'n':
        print(symbhols * weight+line * weight)
except:
    print('Вводите числа на первах трех вводах')