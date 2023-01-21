# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

def candy(k):
    m = 28
    while True:
        choice = int(input('Сколько конфет забрать: '))
        if (k - choice) < 0:
            print(f'Осталось лишь {k} конфет, нельзя забрать больше')
        else:
            if choice > m or choice < 1:
                print(f'Брать можно не меньше 1 конфеты и не больше {m}')
            else:
                return k - choice
def pvp():
    k = 2021
    player = 2
    while k != 0:
        player = player%2 + 1
        print(f'\nКонфет осталось: {k}\nХодит игрок №{player}')
        k = candy(k)
    print(f'\nПобедил игрок №{player}')
def bot(k):
    import random as r
    m = 28
    chois = k%(m+1)
    if chois == 0:
        chois = r.randrange(1, 28)
    return chois
def pvb():
    k = 2021
    player = 2
    while k != 0:
        player = player % 2 + 1
        print(f'\nКонфет осталось: {k}')
        if player == 1:
            print('Ходит игрок')
            k = candy(k)
        else:
            choice = bot(k)
            k -= choice
            print(f'Бот забрал {choice} конфет')
    if player == 1:
        print(f'\nКаким-то чудом победил игрок')
    else:
        print(f'\nЗакономерно победил бот')

while True:
    print('Для игры с другим мешком мяса жми 1\nДля игры с ботом - 2')
    game = int(input('Твой выбор: '))

    while game != 1 and game != 2:
        print('\nРусским же языком написано: 1 или 2 нажми. Что сложного-то?')
        game = int(input('Как думаешь, сейчас справишься? '))

    if game == 1:
        pvp()
    else:
        pvb()