def temp_calc():
    temp_v = int(input('Температура:'))
    temp_t = input('Шкала:')
    if temp_t == 'Цельсий':
        c = temp_v
        k = temp_v + 273.15
        f = int((temp_v + 459.67) / 1.8)
        print(f'Температура по шкале Цельсий {c}, по шкале Кельвин {k}, по шкале Фарренгейт {f}')
    elif temp_t == 'Кельвин':
        k = temp_v
        c = temp_v - 273.15
        f = int(temp_v - 32) / 1.8
        print(f'Температура по шкале Кельвин {k}, по шкале Цельсий {c},по шкале Фарренгейт {f}')
    elif temp_t == 'Фарренгейт':
        f = temp_v
        k = int((temp_v + 459.67) / 1.8)
        c = int((temp_v - 32) / 1.8)
        print(f'Температура по шкале Фарренгейт {f}, по шкале Кельвин {k}, по шкале Цельсий {c}')

temp_calc()