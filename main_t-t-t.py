# БЛОК 1. ВЫВОД ПРИВЕТСТВИЯ ИГРОКОВ
def hello():
    #print(' <-x-o--x-o--x-o--x-o--x-o-> ')
    print(' <                         > ')
    print(' <  ИГРА КРЕСТИКИ-НОЛИКИ   > ')
    print(' <                         > ')
    #print(' <-x-o--x-o--x-o--x-o--x-o-> ')
    print(' <   играют два игрока     > ')
    print(' < первым ставится крестик > ')
    print(' <  при вводе указываются: > ')
    print(' <  координаты поля в фор- > ')
    print(' <  мате "х" и "y", через  > ')
    print(' <      пробел, где:       > ')
    print(' <   "x" - номер строки    > ')
    print(' <   "у" - номер столбца   > ')
    print(' ')

#hello()

# БЛОК 2. ОТОБРАЖЕНИЕ КЛЕТОК И ПОЛЯ
# Вариант 1_
# field = [
#     [' ', ' ', ' '],
#     [' ', ' ', ' '],
#     [' ', ' ', ' ']
# ]
# def view():
#     print('  | 0 | 1 | 2 | ')
#     print('-----------------')
#     for i, j in enumerate(field):
#         row_str = str(i) + ' | ' + ' ' + ' | ' + ' ' + ' | ' + ' ' + ' | ' + ' '.join(map(str, j))
#         print(row_str)
#         print('-----------------')
#     print(' ')
# view()

# Вариант 2
#field_1 = [[' '] * 3 for i in range(3)] # inline
#print(field_1)
def view_1():
    print('  | 0 | 1 | 2 | ')
    print('-----------------')
    for i, j in enumerate(field_1):
        row_str = f"{i} | {' | '.join(j)} | "
        print(row_str)
        print('-----------------')
    print(' ')

#view_1()

#БЛОК 3. ВВОД И ПРОВЕРКА ДАННЫХ ПОЛЬЗОВАТЕЛЯ
def enter():
    while True: # зацикливаем ввод данных
        move = input('Введите номер для строки и столбца: ').split()
        # установка валидности введенных данных
        if len(move) != 2:
            print('Повторите ввод номера для строки и столбца, через пробел')
            continue # удобно - не нужно строить условные конструкции (здесь и далее)

        string, row = move # присваеваение данных переменным
        # проверка, что string и row натуральыне числа
        if not(string.isdigit()) or not(row.isdigit()):
            print('Повторите ввод номеров в виде чисел от 0 до 2')
            continue
        # проверка, что string и row не выходят за диапазон для чего преобразуем их в вещественные
        if 0 > int(string) or int(string) > 2 or 0 > int(row) or int(row) > 2:
            print('Значения должны быть в диапазоне от 0 до 2')
            continue
        # дополнительно проверка на занятость клетки (иначе значение меняестя с Х на 0 и наоборот
        string, row = int(string), int(row)
        if field_1[string][row] != ' ':
            print("Эта клетка уже занята, повторите ввод")
            continue

        return string, row

#enter()

#БЛОК 5. ОПРЕДЕЛЕНИЕ ВЫИГРЫШНЫХ КОМБИНАЦИЙ
def win_combinat():
    win_combinat = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for moving in win_combinat:
        syns = []
        for numb in moving:
            syns.append(field_1[numb[0]][numb[1]])
        if syns == ['X', 'X', 'X']:
            print('Выиграл Крестик!')
            return True
        if syns == ['0', '0', '0']:
            print('Выиграл Нолик!')
            return True
    return False

# БЛОК 4. ОТОБРАЖЕНИЕ ИГРЫ
hello()
field_1 = [[' '] * 3 for i in range(3)] # inline
count = 0
while True:
    count += 1 #начало игры
    view_1()
    # определяем логику распределения ходов
    if count % 2 == 1:
        print('Поставьте крестик')
    else:
        print('Поставьте нолик')

    string, row = enter() # заправшиваем у пользователя данные и присваеваем их "х" (номер строки) и "y" (номер столбца)
    # определяем логику заполнения двумерной матрицы
    if count % 2 == 1:
        field_1[string][row] = 'X'
    else:
        field_1[string][row] = '0'

    if win_combinat(): # проверка выигрышных комбинаций
        break

    if count == 9: # остановка игры и безусловный выход из цикла
        print('Игра завершена, все поля заполнены')
        break