# Крестики нолики v.0.1
# Day 16.07.2022
import random


# Функция для вывода игрового поля
def playing_field():
    print('\n ', boxes[0], '|', boxes[1], '|', boxes[2])
    print(' ---|---|---')
    print(' ', boxes[3], '|', boxes[4], '|', boxes[5])
    print(' ---|---|---')
    print(' ', boxes[6], '|', boxes[7], '|', boxes[8])


# Функция проверки символа пользователя
def check_user_symbol(input_user_symbol):
    # Проверка символа на 'О' или 'X'
    flag = True
    while flag:
        if input_user_symbol == 'X' or input_user_symbol == 'Х':
            user_symbol_def = 'X'
            flag = False
            return user_symbol_def
        if input_user_symbol == 'O' or input_user_symbol == 'О':
            user_symbol_def = 'O'
            flag = False
            return user_symbol_def
        else:
            input_user_symbol = input('[Ошибка] Выберите символ, (O или X): ').upper()


# Функция для получения числа от 0 до 8
def random_number():
    return random.randint(0, 8)


boxes = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Выбор символа пользователем
user_symbol = check_user_symbol(input_user_symbol=input('Выберите символ, (O или X): ').upper())

Game = True
# Основный цикл программы
while Game:
    # Ход Игрока
    while True:
        input_user_box = int(input('\n(Ваш ход "' + user_symbol + '") Выберите ячейку для хода >> '))
        # Проверяет чтобы число было от 0 до 8
        if 0 <= input_user_box <= 8:
            # Если ячейка свободная то вписываем символ пользователя
            if boxes[input_user_box] == ' ':
                boxes[input_user_box] = user_symbol
                break
            else:
                print('Эта ячейка занята')
        else:
            print('[Ошибка] Выберите число от 0 до 8')
    # Ход Компьютера
    while True:
        if boxes[random_number()] == ' ':
            if user_symbol == 'X':
                boxes[random_number()] = 'O'
            elif user_symbol == 'O':
                boxes[random_number()] = 'X'
            break

    playing_field()

    # Выигрышные комбинации 'X'
    if boxes[0] == 'X' and boxes[1] == 'X' and boxes[2] == 'X' or boxes[3] == 'X' and boxes[4] == 'X' and boxes[
        5] == 'X' or boxes[6] == 'X' and boxes[7] == 'X' and boxes[8] == 'X':
        print("\n[!] Выиграл 'X'.")
        Game = False

    if boxes[0] == 'X' and boxes[3] == 'X' and boxes[6] == 'X' or boxes[1] == 'X' and boxes[4] == 'X' and boxes[
        7] == 'X' or boxes[2] == 'X' and boxes[5] == 'X' and boxes[8] == 'X':
        print("\n[!] Выиграл 'X'.")
        Game = False

    if boxes[0] == 'X' and boxes[4] == 'X' and boxes[8] == 'X' or boxes[2] == 'X' and boxes[4] == 'X' and boxes[
        6] == 'X':
        print("\n[!] Выиграл 'X'.")
        Game = False

    # Выигрышные комбинации 'О'
    if boxes[0] == 'O' and boxes[1] == 'O' and boxes[2] == 'O' or boxes[3] == 'O' and boxes[4] == 'O' and boxes[
        5] == 'O' or boxes[6] == 'O' and boxes[7] == 'O' and boxes[8] == 'O':
        print("\n[!] Выиграл 'O'.")
        Game = False

    if boxes[0] == 'O' and boxes[3] == 'O' and boxes[6] == 'O' or boxes[1] == 'O' and boxes[4] == 'O' and boxes[
        7] == 'O' or boxes[2] == 'O' and boxes[5] == 'O' and boxes[8] == 'O':
        print("\n[!] Выиграл 'O'.")
        Game = False

    if boxes[0] == 'O' and boxes[4] == 'O' and boxes[8] == 'O' or boxes[2] == 'O' and boxes[4] == 'O' and boxes[
        6] == 'O':
        print("\n[!] Выиграл 'O'.")
        Game = False
