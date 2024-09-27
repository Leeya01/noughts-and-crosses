#Name: leeya01

import random
import os.path
import json


def draw_board(board):
    print(" -----------")
    print("| " + board[0][0] + " | " +  board[0][1] + " | " + board[0][2] + " |")
    print(" -----------")
    print("| " + board[1][0] + " | " +  board[1][1] + " | " + board[1][2] + " |")
    print(" -----------")
    print("| " + board[2][0] + " | " +  board[2][1] + " | " + board[2][2] + " |")
    print(" -----------")


def welcome(board):
    # prints the welcome  message
    print("Welcome to the \"Unbeatable Noughts and Crosses\" game.")
    print("The board layout is show below:")
    # display the board by calling draw_board(board)
    draw_board(board)


def initialise_board(board):
    # Loop through each row and column of the board
    for i in range(3):
        for j in range(3):
            # Set the value of the current cell to a single space character
            board[i][j] = ' '
    return board


def get_player_move(board):
    while True:
        try:
            # Ask the user for the cell to put the X in

            print("\t\t    1 2 3")
            print("\t\t    4 5 6")
            square = int(input("Choose your square: 7 8 9: "))

            # Check if the chosen cell is within the valid range
            if 1 <= square <= 9:
                # Convert the choice to row and col
                row = (square - 1) // 3
                col = (square - 1) % 3

                # Check if the chosen cell is empty
                if board[row][col] == ' ':
                    # Return row and col
                    return row, col
                else:
                    print("Square not empty")
            else:
                print("Square number must be between 1 and 9")
        except ValueError:
            print("Invalid number.")



def choose_computer_move(board):
    # Check for winning moves
    for let in ["O", "X"]:
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    # Check if the move leads to a win
                    board[i][j] = let
                    if check_for_win(board, let):
                        return i, j
                    # Undo the move
                    board[i][j] = ' '

    # Check for corners
    corners = [[0, 0], [0, 2], [2, 0], [2, 2]]
    random.shuffle(corners)
    for i, j in corners:
        if board[i][j] == ' ':
            return i, j

    # Check for edges
    edges = [[0, 1], [1, 0], [1, 2], [2, 1]]
    random.shuffle(edges)
    for i, j in edges:
        if board[i][j] == ' ':
            return i, j


def check_for_win(board, mark):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == mark for j in range(3)) or all(board[j][i] == mark for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True

    # No win
    return False

def check_for_draw(board):
    # Check if all cells are occupied
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                # If any cell is empty, the game is not a draw
                return False

    # All cells are occupied, and there is no winner, so it's a draw
    return True


def play_game(board):
    # develop code to play the game
    print("The game begins")
    # star with a call to the initialise_board(board) function to set
    initialise_board(board)
    # the board cells to all single spaces ' '
    # then draw the board
    draw_board(board)
    # then in a loop, get the player move, update and draw the board
    while True:
        player_row, player_col = get_player_move(board)
        board[player_row][player_col] = 'X'
        draw_board(board)
    # check if the player has won by calling check_for_win(board, mark),
    # if so, return 1 for the score
        if check_for_win(board, 'X'):
            print("You win!")
            return 1
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
        if check_for_draw(board):
            print("It's a draw.")
            return 0
    # if not, then call choose_computer_move(board)
    # to choose a move for the computer
        computer_row, computer_col = choose_computer_move(board)
        print("Computer plays", "row", computer_row,"Column", computer_col)
        board[computer_row][computer_col] = 'O'
    # update and draw the board
        draw_board(board)

    # check if the computer has won by calling check_for_win(board, mark),
    # if so, return -1 for the score
        # Check if the computer has won
        if check_for_win(board, 'O'):
            print("You lose!")
            return -1
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
        if check_for_draw(board):
            print("It's a draw")
            return 0
    #repeat the loop



def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program'
    print("Enter one of the following options:")
    print("    1 - Play the game")
    print("    2 - Save your score in the leaderboard")
    print("    3 - Load and display the leaderboard")
    print("    q - End the program")
    while True:
        choice = input("1, 2, 3 or q?")
        if choice in ['1','2','3','q']:
            return choice

def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    leaderboard = open("leaderboard.txt", 'r')
    leaders = json.loads(leaderboard.read())
    leaderboard.close()
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    print(type(leaders))
    print(leaders)
    return leaders


def save_score(score):
    # develop code to ask the player for their name
    player_name = input("Enter your name: ")
    # and then save the current score to the file 'leaderboard.txt'
    leaders = load_scores()
    leaders[player_name] = score
    leaderboard_file=open("leaderboard.txt", 'w')
    json.dump(leaders, leaderboard_file)
    leaderboard_file.close()
    return leaders


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    print("Leaderboard:")
    # passed in the Python dictionary parameter leader
    for player_name, score in leaders.items():
        print(f"{player_name}: {score}")


