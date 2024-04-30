import random

def level():
    while True:
        level = input("Level: ")
        if level.isdigit() and int(level) > 0:
            return int(level)
        else:
            print("Please enter a positive integer.")

def guess():
    while True:
        guess = input("Guess: ")
        if guess.isdigit() and int(guess) > 0:
            return int(guess)
        else:
            print("Please enter a positive integer.")

def game():
    level = prompt_level()
    target = random.randint(1, level)

    while True:
        guess = prompt_guess()
        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break

play_game()
