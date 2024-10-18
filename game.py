# количество клеток
board_size = 3
step = 1
# игровое поле
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def draw_board():
    """ Выводим игровое поле """
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|') * 3)
        print('', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print(('_' * 3 + '|') * 3)
        pass



def start_game():
    # текущий игрок
    current_player = 'X'
    # номер шага
    step = 1
    draw_board()

def game_step(index, char):
    """ выполняем ход """
    if (index > 9 or index < 1 or board[index - 1] in ('X', 'O')):
        return False
    board[index - 1] = char
    return True


def check_win():
    """ Проверяем победу одного из игроков """
    while (step < 10) and (check_win() == False):
        index = input('Ходит игрок ' + current_player + '. Введите номер поля (0 - выход):')
        if (index == '0'):
            break
        # Проверка ввода
        try:
            index = int(index)
        except ValueError:
            print('Неверный ввод! Повторите!')
            continue

        # если получилось сделать шаг
        if (game_step(index, current_player)):
            print('Удачный ход')

            if (current_player == 'X'):
                current_player = 'O'
            else:
                current_player = 'X'
def start_game():
    draw_board()

print('Добро пожаловать в крестики-нолики!')
start_game()

