print('идёт дождь?')
rainy = input()
if rainy == 'да':
    print('сильный?')
heavy = input()
if heavy == 'да':
    print('возьми зонт и одень куртку')
elif heavy == 'нет':
    print('одень худи, зонт не бери')
elif rainy == 'нет':
    print('тепло?')
warm = input()
if warm == 'да':
    print('оденься легко')
elif warm == 'нет':
    print('одень кофту')