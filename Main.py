the_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
num_moves = 0

get_move_position = {0: [0, 0], 1: [0, 1], 2: [0, 2],
                     3: [1, 0], 4: [1, 1], 5: [1, 2],
                     6: [2, 0], 7: [2, 1], 8: [2, 2]}


class _player:

    def __init__(self, mark):
        self.mark = mark


class _player2:
    def __init__(self, mark):
        self.mark = mark


def display_board(board):
    for i in range(len(board)):
        for k in range(len(board[i])):
            if k <= 1:
                print(the_board[i][k], end=" | ")
            else:
                print(the_board[i][k])
        if i <= 1:
            print("--|---|--")
    print("\n")


def make_move(row, col, mark):
    if the_board[row][col] == ' ':
        the_board[row][col] = mark
        return True
    return False


def check_for_win(board, mark):
    # checking first row
    if board[0][0] == mark and mark == board[0][1] and mark == board[0][2]:
        return True
    # second row win
    if board[1][0] == mark and mark == board[1][1] and mark == board[1][2]:
        return True
    # third row win
    if board[2][0] == mark and mark == board[2][1] and mark == board[2][2]:
        return True
    # diagonal win
    if board[0][0] == mark and mark == board[1][1] and mark == board[2][2]:
        return True
    # diagonal win
    if board[0][2] == mark and mark == board[1][1] and mark == board[2][0]:
        return True
    # first column win
    if board[0][0] == mark and mark == board[1][0] and mark == board[2][0]:
        return True
    # second column win
    if board[0][1] == mark and mark == board[1][1] and mark == board[2][1]:
        return True
    # third column win
    if board[0][2] == mark and mark == board[1][2] and mark == board[2][2]:
        return True


def game():
    global num_moves

    p1 = _player("X")
    cpu = _player2("O")

    current_player_move = p1

    game_over = False

    while not game_over:

        indexes = list(get_move_position.values())
        print(f'Number of moves: {num_moves}')

        m = int(input(f'Enter move({current_player_move.mark}):'))
        my_move = indexes[m]

        if make_move(my_move[0], my_move[1], current_player_move.mark):
            num_moves += 1
            display_board(the_board)

            if num_moves >= 9:
                game_over = True
                print("Tie! There was no Winner.")
            if num_moves >= 4:
                if check_for_win(the_board, current_player_move.mark):
                    print(f'Number of moves: {num_moves}')
                    print(f'Congratulations {current_player_move.mark} won the game!')
                    game_over = True
            if not game_over:
                if current_player_move == p1:
                    current_player_move = cpu
                else:
                    current_player_move = p1
        else:
            print(f'Invalid move re-enter({current_player_move.mark}):')
            display_board(the_board)


if __name__ == '__main__':
    game()
