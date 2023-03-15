import random

def return_card():
    '''Return a random card.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    '''Calculate the score, for the machine and for the user.'''
    if sum(cards) == 21 and len(cards) == 2:
        print("you have a Blackjack. You win!")
        return True

    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    
    else:
        return sum(cards)
    
def compare_scores(user_score, computer_score):
    '''Compare the user and computer score.'''
    if user_score == computer_score:
        return "Draw"
    elif user_score == True:
        return "Win with a Blackjack"
    elif computer_score == True:
        return "You lose, the oponennt has a Blackjack"
    if user_score > 21:
         return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def game():
    user_cards = [return_card() for i in range(2)]
    computer_cards = [return_card() for i in range(2)]

    while True: 
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score == True or computer_score == True:
            print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            return print(compare_scores(user_score, computer_score))
        
        elif user_score >= 21 or computer_score >= 21:
            print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            return print(compare_scores(user_score, computer_score))

        buy_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if buy_card == 'y':
            user_cards.append(return_card())
            if computer_score != True and computer_score < 17:
                computer_cards.append(return_card())
            continue
        elif buy_card == 'n':
            if computer_score != True and computer_score <17:
                computer_cards.append(return_card())
            computer_score = calculate_score(computer_cards)
            print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            return print(compare_scores(user_score, computer_score))
        
want_play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()
while want_play == 'y':
    game()
    want_play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()