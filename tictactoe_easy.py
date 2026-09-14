board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

game_turn = 0

def show_board():
    print(board[0], "I", board[1], "I",board[2])
    print("--------")
    print(board[3], "I", board[4], "I",board[5])
    print("--------")
    print(board[6], "I", board[7], "I",board[8])


def check_win():
    if board[0] == board[1] == board[2] == "X" or board[3] == board[4] == board[5] == "X" or board[6] == board[7] == board[8] == "X" or board[0] == board[3] == board [6] == "X" or board[1] == board[4] == board [7] == "X" or board[2] == board[5] == board [8] == "X" or board[0] == board[4] ==board[8] == "X" or board[2] == board[4] ==board[6] == "X":
        print("X Won")
        return True
    elif board[0] == board[1] == board[2] == "O" or board[3] == board[4] == board[5] == "O" or board[6] == board[7] == board[8] == "O" or board[0] == board[3] == board [6] == "O" or board[1] == board[4] == board [7] == "O" or board[2] == board[5] == board [8] == "O" or board[0] == board[4] ==board[8] == "O" or board[2] == board[4] ==board[6] == "O":
        print("O Won")
        return True

def turn():
    while True:
        if game_turn % 2 == 1:
            move = int(input("X Chose space from 1 to 9: "))
            if board[move-1] == " ":
                    board[move-1] = "X"
                    break

        else:
            move = int(input("O Chose space from 1 to 9: "))
            if board[move - 1] == " ":
                board[move - 1] = "O"
                break

while True:
    show_board()
    turn()
    game_turn +=1

    if check_win() == True:
        break

    if game_turn == 9:
        print("draw")
        break
