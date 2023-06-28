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

hello()

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
field_1 = [[' '] * 3 for i in range(3)] # inline
#print(field_1)
def view_1():
    print('  | 0 | 1 | 2 | ')
    print('-----------------')
    for i, j in enumerate(field_1):
        row_str = f"{i} | {' | '.join(j)} | "
        print(row_str)
        print('-----------------')
    print(' ')
view_1()

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

        return string, row

enter()
