# Создайте программу для игры в ""Крестики-нолики"".

def change_field(field, chois, symbol):
    # chois = list(map(lambda x: x-1, (map(int, (chois.split('.'))))))
    field[chois[0]][chois[1]] = symbol
    flag = 0

    for i in range(len(field)):
        if field[i].count(symbol) == 3:
            flag = 1

    f = list(zip(field[0], field[1], field[2]))
    for i in range(len(f)):
        if f[i].count(symbol) == 3:
            flag = 1

    diagonal = []
    diagonal.append(field[0][0])
    diagonal.append(field[1][1])
    diagonal.append(field[2][2])
    if diagonal.count(symbol) == 3:
        flag = 1
    diagonal.remove(field[0][0])
    diagonal.append(field[0][2])
    diagonal.remove(field[2][2])
    diagonal.append(field[2][0])
    if diagonal.count(symbol) == 3:
        flag = 1

    if flag == 1:
        if symbol == 'X':
            return 1
        else:
            return 2
    else:
        return 0


def check(field):
    if field == '_':
        return True
    else:
        print('Error!')
        return False


field = ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']
player1 = 'X'
player2 = 'O'
move = 2
win = 0
counter = 0

while win == 0:
    factorization = False
    move = move%2 + 1
    for i in range(len(field)):
        print(*field[i])
    print()
    # chois = input(f"Player {move} chois: ")
    # chois = list(map(lambda x: x - 1, (map(int, (input(f"Player {move} chois: ").split('.'))))))
    # print(chois)
    while not factorization:
        chois = list(map(lambda x: x - 1, (map(int, (input(f"Player {move} chois: ").split('.'))))))
        factorization = check(field[chois[0]][chois[1]])
    win = change_field(field, chois, player1 if move == 1 else player2)
    if counter == 9:
        print('Draw')

for i in range(len(field)):
    print(*field[i])
print(f'\nPlayer {move} WIN!')



# while True:
#     print('Для игры с другим человеком нажми 1\nДля игры с ботом - 2')
#     game = int(input('Твой выбор: '))
#
#     while game != 1 and game != 2:
#         print('\nРусским же языком написано: 1 или 2 нажми. Что сложного-то?')
#         game = int(input('Как думаешь, сейчас справишься? '))
#
#     if game == 1:
#         pvp()
#     else:
#         pvb()