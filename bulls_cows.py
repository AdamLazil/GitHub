"""
projekt_2.py: druhy projekt do Engeto Online Python Akademie - Bulls and Cows

author: Lizal Adam
email: lizaladam@seznam.cz
discord: Adam_L



"""


import random
import time


def get_introduction():
    line = "-" * 50
    prompt = f"Hi there! \n {line}"
    prompt += f"\n I' have generated a random 4 digit number for you. \n Let's play a bulls and cows game. \n {line}"
    print(prompt)


def make_secret_number(length: int = 4) -> list:
    """
    This function is makeing random length number without duplicates
    Use parametr length for setting up how many number you wish for
    Default value is 4 digit number
    """
    secret_num = []
    while len(secret_num) < length:
        new_digit = str(random.randint(1, 9))
        if new_digit not in secret_num:
            secret_num.append(new_digit)
    return "".join(secret_num)


def guess_number(length):
    """
    Except number from user and check if the number is valid.
    If is number not valid print why
    """
    while True:
        try:
            n = user_guess = input(f"Enter a number: ")
            n = int(n)
            if len(user_guess) != length:  # or not user_guess.isdigit():
                print(f" Enter a {length} digit number")
                continue
            if len(set(user_guess)) != length:
                print("Enter a number with different digits")
                continue
            if user_guess[0] == "0":
                print("You can't begin with 0")
                continue

        except ValueError:
            print("Input you entered is not a number")
        else:
            return user_guess


def get_bulls_cows(secret_num, user_guess):
    bulls = 0
    cows = 0
    for x in range(len(secret_num)):
        if user_guess[x] == secret_num[x]:
            bulls += 1
    for x in range(len(secret_num)):
        if user_guess[x] in secret_num and user_guess[x] != secret_num[x]:
            cows += 1
    return bulls, cows


def main(secret_num_len):
    st = time.time()
    attempts = 0
    get_introduction()
    secret_number = make_secret_number(secret_num_len)
    line = "-" * 50
    print(f"{secret_number}")

    while True:
        input_number = guess_number(secret_num_len)
        attempts += 1
        print(line)

        bulls, cows = get_bulls_cows(secret_number, input_number)

        if bulls == len(secret_number):
            print(f" You won in {attempts} attempts")
            print(f"It tooked you {finish} s")
            if attempts < 5:
                score = "Amazing"
            if attempts > 5 and attempts < 10:
                score = "Good"
            if attempts > 10:
                score = "not so gooood"
            print(f"{line} \n That's {score} result")
            break

        if bulls <= 1 and cows <= 1:
            print(f"Bull: {bulls} \n Cow: {cows}")
        elif bulls > 1 and cows <= 1:
            print(f"Bulls: {bulls} \n Cow: {cows}")
        else:
            print(f"Bulls: {bulls} \n Cows: {cows}")
        et = time.time()
        finish = et - st


if __name__ == "__main__":
    secret_number_length = 4
    main(secret_number_length)
