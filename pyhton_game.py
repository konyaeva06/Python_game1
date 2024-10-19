#количество клеток
board_size = 3
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

def game_step(index, char):
    """ выполняем ход """
    if index > 9 or index < 1 or board[index - 1] in ('X', 'O'):
        return False
    board[index - 1] = char
    return True

def start_game():
    draw_board()

print('Добро пожаловать в крестики-нолики!')
start_game()
