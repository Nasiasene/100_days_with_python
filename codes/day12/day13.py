from art import logo
import random

def check(user_guess, number):
    if user_guess < number:
        print("Too low.")
    elif user_guess > number:
        print("Too high.")

    
def end_game(lifes, guess, number):
    if lifes == 0 and guess != number:
        print("You've run out of guesses, you lose.")
        return True
    elif lifes == 0 and guess == number:
        print(f"You got it! The answer was {number}.")
        return True
    elif guess == number:
        print(f"You got it! The answer was {number}.")
        return True
    else:
        print("Try again.")
        return False

def game():
    while True:
        dificult = input("Choose a dificulty. Type 'easy' or 'hard': ")
        if dificult == 'easy':
            attempts = 10
            break
        elif dificult == 'hard':
            attempts = 5
            break
        else:
            print("Input a viable answer.\n")

    number = random.randint(1, 100)
    end = False
    while end == False:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts -= 1
        check(guess, number)
        end = end_game(attempts, guess, number)


print(logo, "\nWelcome to the Number Guessing game !")
while True:
    want_play = input("Do you want to play the game? (type 'y' or 'n'): ").lower()
    if want_play != 'y' and want_play != 'n':
        print("Input a viable answer.")
        continue
    elif want_play == 'n':
        print("Goodbye.")
        break
    else:
        game()