import random   # get a random numbers to shuffle the board
import math     # get a sqrt of board size to know row and col length
import time     # get timestamp to measure solution time

# program defines
EMPTY_SQUARE_SIGN = "-"
NO_SQUARE = -1

def get_board_size_from_user():
    board_size = ""
    while True:
        try:
            board_size = input("Welcome to the Sorting Game! please choose board size (9 ,16 or 25): ")
            board_size = int(board_size)
            if board_size == 9 or board_size == 16 or board_size == 25:
                break
        except ValueError:
            continue
    return board_size

def get_sorted_board(board_size: int):
    row_or_col_length = math.sqrt(board_size)
    row_or_col_length = int(row_or_col_length)
    board = list()
    square_counter=1
    for row in range(row_or_col_length):
        row_list = list()
        board.append(row_list)
        for col in range(row_or_col_length):
            if square_counter == board_size:
                row_list.append(EMPTY_SQUARE_SIGN)
            else:
                row_list.append(square_counter)
                square_counter +=1
    return board

def initializing_board(board_size: int):
    board = get_sorted_board(board_size)
    for i in range(10000):
        num = random.randint(1,board_size-1)
        temp_board = move_num(board, num)
        if temp_board == NO_SQUARE:
            continue
        else:
            board = temp_board
    return board

def move_num(board: list, num: int):
    row_num, col_num = get_row_col_of_num(board, num)
    row_empty, col_empty = check_if_near_empty_square(row_num, col_num, board)
    if row_empty == NO_SQUARE and row_empty == NO_SQUARE:
        return NO_SQUARE
    board[row_empty][col_empty] = int(num)
    board[row_num][col_num] = EMPTY_SQUARE_SIGN
    return board

def print_board(board: list):
    row_or_col_length = len(board)
    line1 = "+" + "-" * 4 * row_or_col_length + "+"
    print(line1)
    for row in range(row_or_col_length):
        print(f"|", end="")
        for col in range(row_or_col_length):
            print(" {:2} ".format(board[row][col]), end="")
        print("|", end="")
        print()
    print(line1)

def check_is_board_sorted(board: list, board_size: int):
    row_or_col_length = len(board)
    board_counter = 1
    for row in range(row_or_col_length):
        for col in range(row_or_col_length):
            if board[row][col] == board_counter or (board[row][col] == EMPTY_SQUARE_SIGN and board_counter == board_size):
                board_counter += 1
            else:
                return False
    return True

def get_row_col_of_num(board: list, num: int):
    row_or_col_length = len(board)
    for row in range(row_or_col_length):
        for col in range(row_or_col_length):
            if board[row][col] == num:
                return row, col

def check_if_near_empty_square(row: int, col: int, board: list):
    row_or_col_length = len(board)
    row_to_check = row-1
    col_to_check = col
    answer = check_if_row_and_col_in_range(row_to_check,col_to_check,row_or_col_length)
    if answer ==  True and board[row_to_check][col_to_check] == EMPTY_SQUARE_SIGN:
            return row_to_check, col_to_check

    row_to_check = row+1
    col_to_check = col
    answer = check_if_row_and_col_in_range(row_to_check,col_to_check,row_or_col_length)
    if answer ==  True and board[row_to_check][col_to_check] == EMPTY_SQUARE_SIGN:
            return row_to_check, col_to_check

    row_to_check = row
    col_to_check = col-1
    answer = check_if_row_and_col_in_range(row_to_check,col_to_check,row_or_col_length)
    if answer ==  True and board[row_to_check][col_to_check] == EMPTY_SQUARE_SIGN:
            return row_to_check, col_to_check

    row_to_check = row
    col_to_check = col + 1
    answer = check_if_row_and_col_in_range(row_to_check, col_to_check, row_or_col_length)
    if answer == True and board[row_to_check][col_to_check] == EMPTY_SQUARE_SIGN:
        return row_to_check, col_to_check

    return NO_SQUARE,NO_SQUARE

def check_if_row_and_col_in_range(row: int, col: int, board_size: int):
        if (0 <= row < board_size) and (0 <= col < board_size):
            return True
        else:
            return False

def check_is_valid_num_in_range(num: int, board_size: int):
    if 0 <= num < board_size:
        return True
    else:
        return False

def main():
    board_size = get_board_size_from_user()
    board = initializing_board(board_size)

    print("This is the final result")
    print_board(get_sorted_board(board_size))
    print()
    print("And this is your board, the purpose of the game is to sort your board!")
    print_board(board)

    move_counter = 0
    input("look carefully on the board and then press any key to start....")
    start = time.time()
    while(True):
        num = input("choose a number to move: ")
        if num.isnumeric() == False:
            continue
        answer = check_is_valid_num_in_range(int(num), board_size)
        if answer == False:
            continue
        temp_board = move_num(board, int(num))
        if temp_board == NO_SQUARE:
            continue
        else:
            board = temp_board
        move_counter += 1
        print_board(board)
        print(f"till now {move_counter} moves")

        flag = check_is_board_sorted(board, board_size)
        if flag:
            end = time.time()
            print("You won with {} moves in {:.2f} seconds, nice job!".format(move_counter, end-start))
            break

if __name__ == "__main__":
    main()
