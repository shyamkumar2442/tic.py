import random

board = [' '] * 9
computer = 'X'
player = 'O'

def display_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print(f"__ |__ |__")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print(f"__ |__ |__")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print(f"   |   |  ")
    print()

def win_checking():
    
      #vertical win movements
    if board[0] == board[3] == board[6] and board[0] != ' ':
        return True
    elif board[1] == board[4] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] == board[8] and board[2] != ' ':
        return True
    #Horizontal win Movement
    elif board[0] == board[1] == board[2] and board[0] != ' ':
        return True
    elif board[3] == board[4] == board[5] and board[3] != ' ':
        return True
    elif board[6] == board[7] == board[8] and board[6] != ' ':
        return True
    #Diagonal win movements
    elif board[0] == board[4] == board[8] and board[0] != ' ':
        return True
    elif board[6] == board[4] == board[2] and board[6] != ' ':
        return True
    else:
        return False


def check_position(position):
    return board[position] == ' '

def draw_checking():
    return ' ' not in board

def player_move(letter):
    while True:
        try:
            position = int(input("Enter the position you want to choose from 0 to 8: "))
            if check_position(position):
                insert(letter, position)
                break
            else:
                print("Position is not available, re-enter the position.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 0 and 8.")

def computer_move(letter):
    while True:
        position = random.randint(0, 8)
        if check_position(position):
            insert(letter, position)
            break

def insert(letter, position):
    board[position] = letter
    display_board(board)
    if win_checking():
        if letter == 'X':
            print("Computer wins!!!!")
            exit()
        else:
            print("Player wins!!!!!")
            exit()

# Main game loop
while True:
    display_board(board)
    player_move(player)
    if win_checking() or draw_checking():
        if draw_checking():
            print("The game is a draw!!!")
        break
    
    computer_move(computer)
    if win_checking() or draw_checking():
        if draw_checking():
            print("The game is a draw!!!")
        break