import random
import hm_art as art #from hm_art import stages, logo
import hm_word as words #from hm_word import word_list

word_list = words.word_list
chosen_word = random.choice(word_list)
used_letter = []
display = []
lives = 6
wor_length = len(chosen_word)

print(art.logo)
print('\n'*3)
print(f'Welcome to Hangman Game. The word is  {str(wor_length)} letters long.')
print('\n', '~-'*20)
print(art.stages[0])
print('~-'*20, '\n'*2)

for i in chosen_word:
    display.append('_')
#preenchendo a lista com "_"

while '_' in display:
    guess = input('Guess a letter: ').lower() 
    #enquanto a lista ainda tiver "_" e a vida for maior que 0 isso irá se repetir.

    if guess in used_letter:
        print(f'You already guessed "{guess}". Try again')

    elif guess not in used_letter:
        for position in range(wor_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
            
        if guess not in chosen_word:
            lives -= 1
            print(f'"{guess}" is not in the word. You lose a life.')
            print(art.stages[lives])
        if lives == 0:
            print('You lose.')
            break
    used_letter.append(guess)
    print(display)
    

if lives != 0:
    print('You win.')

print('The word was: ' + chosen_word)
