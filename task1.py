try:
    kb = int(input('Введите кол-во килобайов'))
    bites = kb * 1000
    bit = bites * 8
    print(kb, bites, bit)
except:
    print('введите число без букв')