import random


def generate_new_digit_not_in(lst):
    """Generate a random digit not in `lst`."""
    while True:
        d = str(random.randint(0, 9))
        if d not in lst:
            return d


def generate_secret_number(length):
    """Generate secret number with `length` digits and no duplicates."""
    digits = []
    for _ in range(length):
        digits.append(generate_new_digit_not_in(digits))
    return "".join(digits)


def compute_cows_and_bulls(player_guess, secret_number):
    """Return the tuple (cows, bulls) for player_guess."""
    bulls = sum(p == s for p, s in zip(player_guess, secret_number))
    cows = sum(p in secret_number for p in player_guess)
    return cows - bulls, bulls


def get_user_guess(length):
    """Get user guess and validate length."""
    while True:
        player_guess = input("Please enter your guess: ")
        if len(player_guess) == length:
            return player_guess
        print(f"Your guess must be {length} digits long.")


def play_game(secret_number_len, nb_guesses):
    secret_number = generate_secret_number(secret_number_len)
    print(f"For testing. Secret number is: {secret_number}")
    print(f"Guess my number. It contains {secret_number_len} unique digits from 0-9")

    for t in range(nb_guesses):
        player_guess = get_user_guess(secret_number_len)

        # Main game logic
        if player_guess == secret_number:
            print("Yay, you guessed it!")
            return
        cows, bulls = compute_cows_and_bulls(player_guess, secret_number)
        print(f"Bulls: {bulls}")
        print(f"Cows: {cows}")
    print("You lost the game.")


def unit_test_compute_cows_and_bulls():
    assert compute_cows_and_bulls("10", "23") == (0, 0)
    assert compute_cows_and_bulls("10", "13") == (0, 1)
    assert compute_cows_and_bulls("10", "31") == (1, 0)
    assert compute_cows_and_bulls("10", "01") == (2, 0)
    assert compute_cows_and_bulls("10", "10") == (0, 2)


if __name__ == "__main__":
    SECRET_NUMBER_SIZE = 2
    MAX_GUESSES = 50
    play_game(SECRET_NUMBER_SIZE, MAX_GUESSES)
