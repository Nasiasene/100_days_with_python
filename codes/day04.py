#PEDRA PAPEL TESOURA!

import random
images = ["rock", "paper", "scissors"]
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if choice1 != 0 and choice1 != 1 and choice1 != 2:
    print("You typed an invalid number, you lose!")
elif choice1 == 0 and computer_choice == 0:
    print('You chose: Rock')
    print(rock)
    print('Computer chose: Rock')
    print(rock)
    print("It's a draw!")
elif choice1 == 0 and computer_choice == 1:
    print('You chose: Rock')
    print(rock)
    print('Computer chose: Paper')
    print(paper)
    print("You lose!")
elif choice1 == 0 and computer_choice == 2:
    print('You chose: Rock')
    print(rock)
    print('Computer chose: Scissors')
    print(scissors)
    print("You win!")
elif choice1 == 1 and computer_choice == 0:
    print('You chose: Paper')
    print(paper)
    print('Computer chose: Rock')
    print(rock)
    print("You win!")
elif choice1 == 1 and computer_choice == 1:
    print('You chose: Paper')
    print(paper)
    print('Computer chose: Paper')
    print(paper)
    print("It's a draw!")
elif choice1 == 1 and computer_choice == 2:
    print('You chose: Paper')
    print(paper)
    print('Computer chose: Scissors')
    print(scissors)
    print("You lose!")
elif choice1 == 2 and computer_choice == 0:
    print('You chose: Scissors')
    print(scissors)
    print('Computer chose: Rock')
    print(rock)
    print("You lose!")
elif choice1 == 2 and computer_choice == 1:
    print('You chose: Scissors')
    print(scissors)
    print('Computer chose: Paper')
    print(paper)
    print("You win!")
elif choice1 == 2 and computer_choice == 2:
    print('You chose: Scissors')
    print(scissors)
    print('Computer chose: Scissors')
    print(scissors)
    print("It's a draw!")