print('----------------------------------------')
print('|             Калькулятор              |')
print('----------------------------------------')
print('|           Выберите задачу            |')
print('| 1. Вычислить сумму двух чисел        |')
print('| 2. Вычислить разность двух чисел     |')
print('| 3. Произвести умножение двух чисел   |')
print('| 4. Произвести деление двух чисел     |')
print('| 5. Возвести число в степень          |')
print('| 6. Деление без остатка               |')
print('| 0. Выход                             |')
print('----------------------------------------')
print('|             Version 1.0              |')
print('----------------------------------------')
while True:
    znak = int(input('Выберите задачу: '))
    if znak == 0: exit(f'\033[31mзадача завершена\033[0m')
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    if znak == 1: print(f'Результат: \033[34m{a + b}\033[0m')
    elif znak == 2: print(f'Результат: \033[34m{a - b}\033[0m')
    elif znak == 3: print(f'Результат: \033[34m{a * b}\033[0m')
    elif znak == 4: print(f'Результат: \033[34m{a / b}\033[0m')
    elif znak == 5: print(f'Результат: \033[34m{a ** b}\033[0m')
    elif znak == 6: print(f'Результат: \033[34m{a // b}\033[0m')
    else:
        print('----------------------------------------')
        print(f'|       \033[31mВы ввели неверную задачу\033[0m       |')
    print('----------------------------------------')
    print('|   Выберите задачу для продолжения    |')
    print('----------------------------------------')
    print('|           Выберите задачу            |')
    print('| 1. Вычислить сумму двух чисел        |')
    print('| 2. Вычислить разность двух чисел     |')
    print('| 3. произвести умножение двух чисел   |')
    print('| 4. произвести деление двух чисел     |')
    print('| 5. Возвести число в степень          |')
    print('| 6. Деление без остатка               |')
    print('| 0. Выход                             |')
    print('----------------------------------------')

    11