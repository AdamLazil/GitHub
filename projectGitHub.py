motorCycles = []
motorCycles.append("Surron")
motorCycles.append("Surron L1x")
print(motorCycles)

motorCycles.insert(0, "Surron Ultra Bee")
print(motorCycles)

motorCycles.pop(1)
print(motorCycles)


import random

number = []
attempts = 0


def make_number():
    for i in range(4):
        x = random.randrange(0, 9)
        number.append(x)
    if len(number) > len(set(number)):
        number.clear()
        make_number()


def play_game():
    global attempts
    attempts += 1
    cows = 0
    bulls = 0
    print(number)
    choice = input("Please enter a 4 digit number")
    guess = []
    for i in range(4):
        guess.append(int(choice[i]))
    for i in range(4):
        for j in range(4):
            if guess[i] == number[j]:
                cows += 1
    for x in range(4):
        if guess[x] == number[x]:
            bulls += 1
    print(f"Bulls: {bulls}")
    print(f"Cows: {cows}")
    if bulls == 4:
        print(f"You won after {attempts} attempts")
    if bulls != 4:
        play_game()


make_number()
play_game()
