import random  # get a random number for computer turn

# program defines
PLAYER1_SIGN = "X"
PLAYER2_SIGN = "0"
EMPTY_SQUARE_SIGN = "-"
HUMAN = "human"
COMPUTER = "computer"
NO_WINNER = -1
SQUARE_TAKEN = -1
NO_WIN_MOVE = -1
NUMBER_OF_PLAYERS_IN_GAME = 2

class player:
    # 0 for computer and 1 for human
    def __init__(self, user_name: str, is_human: str, sign: str):
        self.is_human = is_human
        self.user_name = user_name
        self.sign = sign

    def print_player_data(self):
        print(f"{self.user_name}, {self.is_human}, {self.sign}")

def initializing_board(board_size: int):
    board = list()
    for i in range(board_size):
        row_list = list()
        for j in range(board_size):
            row_list.append(EMPTY_SQUARE_SIGN)
        board.append(row_list)
    return board

def print_board(board: list):
    board_size = len(board)
    line1 = "+" + "-" * 4 * board_size + "+"
    print(line1)
    print(f"  |", end="")
    for col in range(board_size):
        print(f" {col} ", end="")
    print("|")
    print(line1)
    for row in range(board_size):
        print(f"{row} |", end="")
        for col in range(board_size):
            print(f" {board[row][col]} ", end="")
        print("|", end="")
        print()
    print(line1)

def check_is_square_empty(row, col, board: list):
    if board[row][col] == EMPTY_SQUARE_SIGN:
        return True
    else:
        return False

def play_turn(row: int, col: int, board: list, player: player):
    board[row][col] = player.sign
    return board

# ---------------------------------------------------------------------------------------------------------

def check_if_is_winner_in_rows(board: list):
    # check winner in rows
    for row in board:
        if all(x == PLAYER1_SIGN for x in row):
            return PLAYER1_SIGN
        if all(x == PLAYER2_SIGN for x in row):
            return PLAYER2_SIGN
    else:
        return NO_WINNER

def check_if_is_winner_in_cols(board: list):
    # check winner in cols
    board_size = len(board)
    for col in range(board_size):
        check_counter = 0
        sign_to_check = board[0][col]
        if sign_to_check != PLAYER1_SIGN and sign_to_check != PLAYER2_SIGN:
            continue
        for row in range(board_size):
            if board[row][col] == sign_to_check:
                check_counter += 1
        if check_counter == board_size:
            return sign_to_check
    else:
        return NO_WINNER

def check_if_is_winner_in_diagonal1(board: list):
    # check winner in diagonal left up corner to right bottom corner
    board_size = len(board)
    check_counter = 0
    sign_to_check = board[0][0]
    if sign_to_check == PLAYER1_SIGN or sign_to_check == PLAYER2_SIGN:
        for num in range(board_size):
            if board[num][num] == sign_to_check:
                check_counter += 1
        if check_counter == board_size:
            return sign_to_check
    return NO_WINNER

def check_if_is_winner_in_diagonal2(board: list):
    # check winner in diagonal right up corner to left bottom corner
    board_size = len(board)
    check_counter = 0
    sign_to_check = board[0][board_size - 1]
    if sign_to_check == PLAYER1_SIGN or sign_to_check == PLAYER2_SIGN:
        for num in range(board_size):
            if board[num][board_size - num - 1] == sign_to_check:
                check_counter += 1
        if check_counter == board_size:
            return sign_to_check
    return NO_WINNER

def check_if_is_winner(board: list):
    is_winner = check_if_is_winner_in_rows(board)
    if is_winner != NO_WINNER:
        return is_winner

    is_winner = check_if_is_winner_in_cols(board)
    if is_winner != NO_WINNER:
        return is_winner

    is_winner = check_if_is_winner_in_diagonal1(board)
    if is_winner != NO_WINNER:
        return is_winner

    is_winner = check_if_is_winner_in_diagonal2(board)
    if is_winner != NO_WINNER:
        return is_winner

    return NO_WINNER

# ---------------------------------------------------------------------------------------------------------

def check_is_user_input_corrct(_row_or_col_chosen, board_size):
    if 0 <= _row_or_col_chosen <= board_size - 1:
        return True
    else:
        return False

def human_player_to_act(player_num: player, board: list):
    board_size = len(board)
    while (True):
        print(f"{player_num.user_name} with sign {player_num.sign} to play")
        row = input("enter row: ")
        if not check_is_user_input_corrct(int(row), board_size):
            print("choose row again")
            continue
        col = input("enter col: ")
        if not check_is_user_input_corrct(int(col), board_size):
            print("choose col again")
            continue
        if check_is_square_empty(int(row), int(col), board):
            break
    return play_turn(int(row), int(col), board, player_num)

def get_opposite_sign(player_num: player):
    if player_num.sign == PLAYER1_SIGN:
        return PLAYER2_SIGN
    else:
        return PLAYER1_SIGN

def computer_player_to_act(player_num: player, board: list):
    print(f"{player_num.user_name} to play")
    # check if a winning move exists
    row, col = check_winning_move(board, player_num.sign)
    if row != NO_WIN_MOVE and col != NO_WIN_MOVE:
        return play_turn(row, col, board, player_num)
    # check if opponent have a winning move
    row, col = check_winning_move(board, get_opposite_sign(player_num))
    if row != NO_WIN_MOVE and col != NO_WIN_MOVE:
        return play_turn(row, col, board, player_num)
    # play random move
    board_size = len(board)
    while (True):
        row = random.randint(0, board_size - 1)
        col = random.randint(0, board_size - 1)
        if check_is_square_empty(row, col, board):
            break
    return play_turn(row, col, board, player_num)

def check_if_board_full(board: list):
    for row in board:
        for i in row:
            if i == EMPTY_SQUARE_SIGN:
                return False
    else:
        return True

def get_player_by_sign(list_of_players: list, sign: str):
    for player_num in list_of_players:
        if player_num.sign == sign:
            return player_num

# ---------------------------------------------------------------------------------------------------------

def check_winning_move_in_rows(board: list, sign_to_check: str):
    # check  in rows
    board_size = len(board)
    for row in range(board_size):
        check_counter = 0
        empty_spot_row = NO_WIN_MOVE
        empty_spot_col = NO_WIN_MOVE
        for col in range(board_size):
            if board[row][col] == sign_to_check:
                check_counter += 1
            elif board[row][col] == EMPTY_SQUARE_SIGN:
                empty_spot_row = row
                empty_spot_col = col
        if check_counter == board_size - 1 and empty_spot_col != NO_WIN_MOVE and empty_spot_col != NO_WIN_MOVE:
            return empty_spot_row, empty_spot_col
    else:
       return NO_WIN_MOVE, NO_WIN_MOVE

def check_winning_move_in_cols(board: list, sign_to_check: str):
    board_size = len(board)
    # check  in cols
    for col in range(board_size):
        check_counter = 0
        empty_spot_row = NO_WIN_MOVE
        empty_spot_col = NO_WIN_MOVE
        for row in range(board_size):
            if board[row][col] == sign_to_check:
                check_counter += 1
            elif board[row][col] == EMPTY_SQUARE_SIGN:
                empty_spot_row = row
                empty_spot_col = col
        if check_counter == board_size - 1 and empty_spot_col != NO_WIN_MOVE and empty_spot_col != NO_WIN_MOVE:
            return empty_spot_row, empty_spot_col
    else:
       return NO_WIN_MOVE, NO_WIN_MOVE

def check_winning_move_in_diagonal1(board: list, sign_to_check: str):
    # check winner move in diagonal left up corner to right bottom corner
    board_size = len(board)
    check_counter = 0
    empty_spot_row = NO_WIN_MOVE
    empty_spot_col = NO_WIN_MOVE
    for num in range(board_size):
        if board[num][num] == sign_to_check:
            check_counter += 1
        elif board[num][num] == EMPTY_SQUARE_SIGN:
            empty_spot_row = num
            empty_spot_col = num
    if check_counter == board_size - 1 and empty_spot_col != NO_WIN_MOVE and empty_spot_col != NO_WIN_MOVE:
        return empty_spot_row, empty_spot_col
    else:
        return NO_WIN_MOVE, NO_WIN_MOVE

def check_winning_move_in_diagonal2(board: list, sign_to_check: str):
    # check winner move in diagonal right up corner to left bottom corner
    board_size = len(board)
    check_counter = 0
    empty_spot_row = NO_WIN_MOVE
    empty_spot_col = NO_WIN_MOVE
    for num in range(board_size):
        if board[num][board_size - num - 1] == sign_to_check:
            check_counter += 1
        elif board[num][board_size - num - 1] == EMPTY_SQUARE_SIGN:
            empty_spot_row = num
            empty_spot_col = board_size - num - 1
    if check_counter == board_size - 1 and empty_spot_col != NO_WIN_MOVE and empty_spot_col != NO_WIN_MOVE:
        return empty_spot_row, empty_spot_col
    else:
        return NO_WIN_MOVE, NO_WIN_MOVE

def check_winning_move(board: list, sign_to_check: str):
    row, col = check_winning_move_in_rows(board, sign_to_check)
    if row != NO_WIN_MOVE and col != NO_WIN_MOVE:
        return row, col

    row, col = check_winning_move_in_cols(board, sign_to_check)
    if row != NO_WIN_MOVE and col != NO_WIN_MOVE:
        return row, col

    row, col = check_winning_move_in_diagonal1(board, sign_to_check)
    if row != NO_WIN_MOVE and col != NO_WIN_MOVE:
        return row, col

    row, col = check_winning_move_in_diagonal2(board, sign_to_check)
    if row != NO_WIN_MOVE and col != NO_WIN_MOVE:
        return row, col

    return NO_WIN_MOVE, NO_WIN_MOVE

# ---------------------------------------------------------------------------------------------------------

def check_is_move_creates_2winning_moves(board: list, sign_to_check: str, row: int, col: int):
    board_size = len(board)
    move_counter = 0
    #check row
    check_counter = 0
    empty_square_flag = 0
    for run_on_row in range(board_size):
        if board[run_on_row][col] == sign_to_check:
            check_counter += 1
        elif board[run_on_row][col] == EMPTY_SQUARE_SIGN:
            empty_square_flag = 1
    if check_counter == board_size - 1 and empty_square_flag == 1:
        move_counter += 1

    #check col
    check_counter = 0
    empty_square_flag = 0
    for run_on_col in range(board_size):
        if board[row][run_on_col] == sign_to_check:
            check_counter += 1
        elif board[row][run_on_col] == EMPTY_SQUARE_SIGN:
            empty_square_flag = 1
    if check_counter == board_size - 1 and empty_square_flag == 1:
        move_counter += 1

    #check diagonal 1
    if row == col:
        check_counter = 0
        empty_square_flag = 0
        for row_col in range(board_size):
            if board[row_col][row_col] == sign_to_check:
                check_counter += 1
            elif board[row_col][row_col] == EMPTY_SQUARE_SIGN:
                empty_square_flag = 1
        if check_counter == board_size - 1 and empty_square_flag == 1:
            move_counter += 1

    #check diagonal 2
    is_on_diagonal_2 = False
    for num in range(board_size):
           if num == row and (board_size - num - 1) == col:
               is_on_diagonal_2 = True

    if is_on_diagonal_2 == True:
        check_counter = 0
        empty_square_flag = 0
        for num in range(board_size):
            if board[num][board_size - num - 1] == sign_to_check:
                check_counter += 1
            elif board[num][board_size - num - 1] == EMPTY_SQUARE_SIGN:
                empty_square_flag = 1
        if check_counter == board_size - 1 and empty_square_flag == 1:
            move_counter += 1

    if 2 <= move_counter:
        return True
    else:
        return False

def check_move_creates_2winning_moves(board: list, sign_to_check: str):
    board_size = len(board)
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == EMPTY_SQUARE_SIGN:
                board[row][col] = sign_to_check
                answer = check_is_move_creates_2winning_moves(board, sign_to_check, row, col)
                board[row][col] = EMPTY_SQUARE_SIGN
                if answer == True:
                    return  row, col
    else:
        return NO_WIN_MOVE, NO_WIN_MOVE

# ---------------------------------------------------------------------------------------------------------

def main():
    board_size = 0
    while True:
        try:
            board_size = input("Welcome to Tic Tac Toe! please enter board size greater or equal to 3: ")
            board_size = int(board_size)
            if 3 <= board_size:
                break
        except ValueError:
            continue

    board = initializing_board(board_size)
    print_board(board)

    list_of_players = list()
    for player_num in range(1, NUMBER_OF_PLAYERS_IN_GAME+1):
        player_type = ""
        player_sign = ""
        if player_num == 1:
            player_sign = PLAYER1_SIGN
        else:
            player_sign = PLAYER2_SIGN
        while (player_type != "c" and player_type != "h"):
            player_type = input(f"player {player_num} will be computer or human? (press c or h): ")
        if player_type == "c":
            list_of_players.append(player("computer"+str(player_num), COMPUTER, player_sign))
        else:
            player_name = input("enter a name for human player: ")
            list_of_players.append(player(player_name, HUMAN, player_sign))

    while (True):
        for player_num in list_of_players:
            if player_num.is_human == HUMAN:
                board = human_player_to_act(player_num, board)
            else:
                board = computer_player_to_act(player_num, board)

            print_board(board)

            check_winner_result = check_if_is_winner(board)
            if check_winner_result != NO_WINNER:
                winner_player = get_player_by_sign(list_of_players, check_winner_result)
                print(f"the winner is {winner_player.user_name} !")
                quit()

            if check_if_board_full(board):
                print("the game ended in a tie")
                quit()

if __name__ == "__main__":
    main()
