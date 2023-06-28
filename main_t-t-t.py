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
# Вариант 1
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