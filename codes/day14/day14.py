import random
import art
from data import data

def random_person():
    return random.choice(data)

def print_famous(person):
    return(f"{person['name']}, a {person['description']}, from {person['country']}.")

def compare_followers(data1, data2):
    followers1 = data1['follower_count']
    followers2 = data2['follower_count']
    if followers1 > followers2:
        return 1
    else:
        return 0
    
def game():
    score = 0
    person_1 = random_person()
    while True:
        person_2 = random_person()
        while person_2 == person_1:
            person_2 = random_person()
        print(f"\nCompare A: {print_famous(person_1)}")
        print(art.vs)
        print(f"\nCompare B: {print_famous(person_2)}")
        while True:
            choice = input("Who has more followers on Instagram? Type'A' or 'B': ").upper()
            if choice == 'B':
                choice = 0
                break
            elif choice == 'A':
                choice = 1
                break
            else:
                print("Insert a valid option! ")
                continue

        if compare_followers(person_1, person_2) == choice:
            score += 1
            print(f"\nYou're right! Current score: {score}\n")
            person_1 = person_2
        else:
            print(f"Sorry, that's wrong. Final score: {score}\n")
            break


print(art.logo)
while True:
    want_play = input("Welcome to the Higher Lower Game!\nDo you want to play this game? Type 'Y' or 'N': ").upper()
    if want_play == 'Y':
        print("Let's go! ")
        game()
    elif want_play == 'N':
        print("Goodbye.")
        break
    else:
        print("Insert a valid option! ")
        continue