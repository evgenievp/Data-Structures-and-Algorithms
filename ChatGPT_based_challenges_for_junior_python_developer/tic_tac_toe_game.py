import random

def create_board():
    board = []
    count = 1
    for _ in range(3):
        row = []
        for _ in range(3):
            row.append(f"{count}")
            count += 1
        board.append(row)
    return board


def print_board(board):
    for row in board:
        print(row)
    print("-" * 15)


def player_place(num, board, symbol):
    if num < 4:
        num -= 1
        if not board[0][num].isdigit():
            print(f"Can't place on {num + 1}, because it is not empty.")
            return board, True
        board[0][num] = symbol
    elif 3 < num < 7:
        num -= 4
        board[1][num] = symbol
    elif 6 < num < 10:
        num -= 7
        board[2][num] = symbol
    return board, False


def check_row(board, row, symbol):
    for i in range(3):
        if board[row][i] == symbol:
            pass
        else:
            return False
    return True


def check_col(board, column, symbol):
    for i in range(3):
        if board[i][column] == symbol:
            pass
        else:
            return False
    return True


def check_left_diag(board, symbol):
    for i in range(3):
        if board[i][i] == symbol:
            pass
        else:
            return False
    return True


def check_right_diag(board, symbol):
    column = 2
    for i in range(3):
        if board[i][column] == symbol:
            pass
        else:
            return False
        column -= 1
    return True


def check_winner(board, player_1_symbol, player_2_symbol):
    winner = False
    for i in range(3):
        winner = check_row(board, i, player_1_symbol)
        if winner:
            return True, player_1_symbol
        winner = check_col(board, i, player_1_symbol)
        if winner:
            return True, player_1_symbol
        winner = check_left_diag(board, player_1_symbol)
        if winner:
            return True, player_1_symbol
        winner = check_right_diag(board, player_1_symbol)
        if winner:
            return True, player_1_symbol
        winner = check_row(board, i, player_2_symbol)
        if winner:
            return True, player_2_symbol
        winner = check_col(board, i, player_2_symbol)
        if winner:
            return True, player_2_symbol
        winner = check_left_diag(board, player_2_symbol)
        if winner:
            return True, player_2_symbol
        winner = check_right_diag(board, player_2_symbol)
        if winner:
            return True, player_2_symbol
    return False


def set_starter():
    x = random.randint(1, 2)
    if x == 1:
        player_1_symbol = "X"
        player_2_symbol = "0"
    else:
        player_2_symbol = "X"
        player_1_symbol = "0"
    return player_1_symbol, player_2_symbol


def check_game_ends(board):
    flag = True
    for i in range(2):
        row = board[i]
        for j in range(2):
            if row[j] in "123456789":
                return False
    return True


def main():
    flag = False
    print("Welcome to our tic tac toe game. Random set would choice who will start.")
    board = create_board()
    print_board(board)
    while not flag:
        player_1_symbol = "X"
        player_2_symbol = "0"
        player_1_num = int(input("Player 1: Please enter your num to place in board: "))
        board, flag = player_place(player_1_num, board, player_1_symbol)
        if flag:
            break
        flag = check_winner(board, player_1_symbol, player_2_symbol)
        print_board(board)
        if flag:
            print(f"{player_1_symbol} wins.")
            print_board(board)
            break
        player_2_num = int(input("Player 2: Please enter your num to place in board: "))
        board, flag = player_place(player_2_num, board, player_2_symbol)
        if flag:
            break
        print_board(board)
        flag = check_winner(board, player_1_symbol, player_2_symbol)
        if flag:
            print(f"{player_2_symbol} wins.")
            print_board(board)
            break
        end_game = check_game_ends(board)
        if end_game:
            flag = True
            print("Game ends - Draw.")

main()
