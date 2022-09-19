import random 
board = ["1","2","3",
         "4","5","6",
         "7","8","9"
        ]

turns = ["X", "O"]
currentPlayer = random.choice(turns)
winner = None
playGame = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("- - - - - ")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("- - - - - ")
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerChoice(board):
    print("Please enter a number between 1-9:")
    choice = int(input())
    if(choice >= 1 and choice <= 9):
        if(board[choice - 1] != "X" and board[choice - 1] != "O"):
            board[choice - 1] = currentPlayer
        else:
            if(board[choice - 1] == "X"):
                print("X is already in this spot!")
                playerChoice(board)
            else:
                if(board[choice - 1] == "O"):
                    print("O is already in this spot!")
                    playerChoice(board)
    else:
        print("Number is invalid. Please try again!")
        playerChoice(board)

def horizontalWin(board):
    global winner
    if(board[0] == board[1] and board[1] == board[2] and (board[1] == "X" or board[1] == "O")):
        winner = board[0]
        return True
    elif(board[3] == board[4] and board[4] == board[5] and (board[4] == "X" or board[4] == "O")):
        winner = board[3]
        return True
    elif(board[6] == board[7] and board[7] == board[8] and (board[7] == "X" or board[7] == "O")):
        winner = board[6]
        return True

def verticalWin(board):
    global winner
    if(board[0] == board[3] and board[3] == board[6] and (board[3] == "X" or board[3] == "O")):
        winner = board[0]
        return True
    elif(board[1] == board[4] and board[4] == board[7] and (board[4] == "X" or board[4] == "O")):
        winner = board[1]
        return True
    elif(board[2] == board[5] and board[5] == board[8] and (board[5] == "X" or board[5] == "O")):
        winner = board[2]
        return True

def diagonalWin(board):
    global winner
    if(board[0] == board[4] and board[4] == board[8] and (board[4] == "X" or board[4] == "O")):
        winner = board[0]
        return True
    elif(board[2] == board[4] and board[4] == board[6] and (board[4] == "X" or board[4] == "O")):
        winner = board[2]
        return True

def playGame(board):
    global winner
    global currentPlayer
    print("Welcome to Tic Tac Toe!")
    while(True):
        print(currentPlayer + "'s turn!")
        printBoard(board)
        playerChoice(board)
        if(verticalWin(board) or horizontalWin(board) or diagonalWin(board)):
            print("The winner is " + winner + "!")
            return False
        elif(board[0] != "1" and board [1] != "2" and board[2] != "3"
            and board[3] != "4" and board[4] != "5" and board[5] != "6"
            and board[6] != "7" and board[7] != "8" and board[8] != "9"):
                print("It's a tie!")
                return False

        if(currentPlayer == "X"):
            currentPlayer = "O"
        else:
            currentPlayer = "X"

playGame(board)

