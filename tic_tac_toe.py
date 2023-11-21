import random

print("Welcome to Tic Tac Toe")
print("----------------------")

posibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameBord = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
cols = 3


def get_gameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("", gameBord[x][y], end=" |")
    print("\n+---+---+---+")


def modiffyArray(num, turn):
    num -= 1
    if num == 0:
        gameBord[0][0] = turn
    elif num == 1:
        gameBord[0][1] = turn
    elif num == 2:
        gameBord[0][2] = turn
    elif num == 3:
        gameBord[1][0] = turn
    elif num == 4:
        gameBord[1][1] = turn
    elif num == 5:
        gameBord[1][2] = turn
    elif num == 6:
        gameBord[2][0] = turn
    elif num == 7:
        gameBord[2][1] = turn
    elif num == 8:
        gameBord[2][2] = turn


def checkForWinner(gameBord):
    #### X axis
    if gameBord[0][0] == "x" and gameBord[0][1] == "x" and gameBord[0][2] == "x":
        print("X has won!")
        return "x"
    elif gameBord[0][0] == "o" and gameBord[0][1] == "o" and gameBord[0][2] == "o":
        print("O has won!")
        return "o"

    #### Y axis
    elif gameBord[0][0] == "x" and gameBord[1][0] == "x" and gameBord[2][0] == "x":
        print("X has won!")
        return "x"
    elif gameBord[0][0] == "o" and gameBord[1][0] == "o" and gameBord[2][0] == "o":
        print("O has won!")
        return "o"
    #### Cross wins
    elif gameBord[0][0] == "x" and gameBord[1][1] == "x" and gameBord[2][2] == "x":
        print("X has won!")
        return "x"
    elif gameBord[0][0] == "o" and gameBord[1][1] == "o" and gameBord[2][2] == "o":
        print("O has won!")
        return "o"


leaveLoop = False
turnCounter = 0

while leaveLoop == False:
    if turnCounter % 2 == 1:  # player turn
        get_gameBoard()
        number_picked = int(input("\nChoose a number [1 - 9]: "))
        if number_picked >= 1 or number_picked <= 9:
            modiffyArray(number_picked, "x")
            posibleNumbers.remove(number_picked)
        else:
            print("Invalid input. Please try again")
        turnCounter += 1
    else:
        while True:
            cpu_choice = random.choice(posibleNumbers)
            print(f"\nCpu choice: {cpu_choice}")
            if cpu_choice in posibleNumbers:
                modiffyArray(cpu_choice, "o")
                turnCounter += 1
                break
