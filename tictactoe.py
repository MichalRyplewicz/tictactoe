import numpy as np
turn_number = 0

board = np.zeros((3,3), dtype = int)

lines =[
[(0,0), (0,1), (0,2)],
[(1,0), (1,1), (1,2)],
[(2,0), (2,1), (2,2)],
[(0,0), (1,0), (2,0)],
[(0,1), (1,1), (2,1)],
[(0,2), (1,2), (2,2)],
[(0,0), (1,1), (2,2)],
[(0,2), (1,1), (2,0)]
]

def check_win(board):
    for line in lines:
        values = [board[i][j] for (i,j) in line] 
        if np.prod(values) == 1: 
            return 1
        if np.prod(values) == 8:
            return 2 

    return None

def X_or_Y(number):
    if number == 1:
        return "X"
    elif number == 2:
        return "O"
    else:
        return " "

def print_board():
    for i in range (3):
        for j in range (3):
            print(X_or_Y(board[i][j]), end=" ")
            if j == 0 or j == 1:
                print("I", end=" ")
        print()
        if (i == 0 or i == 1)and j==2:
                print("--------")

def move(turn):
    while True:
        col = int(input("input collumn"))
        row = int(input("input row"))
        if  0 <= col <= 2 and 0 <= row <= 2:
            if board[col][row] == 0:
                board[col][row] = turn%2+1
                break
            else:
                print("place taken")
        else:
            print("invalid input, try again")


while check_win(board) == None:
    print_board()
    move(turn_number)
    turn_number += 1

    if turn_number ==9:
        break

winner = check_win(board)
print_board()
print(f"Win {X_or_Y(winner)}" if winner else "Draw")
