
board_size = 3

board = [1,2,3,4,5,6,7,8,9]

def draw_board():
    print('_' * 6 * board_size)
    for i in range(board_size):
        print((' ' * 5 + '|')*board_size)
        print(' ', board[i*board_size], ' |', '', board[1 + i*board_size], ' |', '', board[2 + i*board_size], ' |')
        print(('_' * 5 + '|')*board_size)
    pass

def game_step(index, char):
    if (index > 9 or index < 1 or board[index-1] in ('X', 'O')):
        return False
    board[index-1] = char
    return True

def check_win():
    win = False

    win_combination = (
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    )

    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]

    return win

def start_game():
    current_player = 'X'
    step = 1
    draw_board()

    while (step<10) and (check_win() == False):
        index = input('\nStep of player ' + current_player + '. Input Number of field (0 - EXIT): ')

        if (index == '0'):
            break

        if (game_step(int(index), current_player)):
            print('Successful Step')

            if (current_player == 'X'):
                current_player = 'O'
            else:
                current_player = 'X'


            draw_board()
            step += 1

        else:
            print('Wrong Number - Repeat')

    if (step == 10) and (check_win() == False):

        print('Game Over')
    elif check_win() != False:
        print('\n     VICTORY OF - ' + check_win() + ' - PLAYER')



print('-------------------------------------------------------------\n        Welcome to Tic-Tac-Toe Console-Game        \n-------------------------------------------------------------\n     Created by Denzighn on Skillfactory Course     \n\n                    Y_Q_Q_Y\n-------------------------------------------------------------')
start_game()