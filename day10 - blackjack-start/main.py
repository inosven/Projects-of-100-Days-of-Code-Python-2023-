from art import logo
import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    card = random.choice(cards)
    return card


def calculate_score(input_cards):
    if len(input_cards) == 2 and sum(input_cards) == 21:
        return 0
    if sum(input_cards) > 21 and 11 in input_cards:
        input_cards.remove(11)
        input_cards.append(1)
    return sum(input_cards)


def compare_results(my_scores, computer_scores):
    if my_scores > 21 and computer_scores > 21:
        return "You bust! You lose."
    elif my_scores == computer_scores:
        return "Draw."
    elif computer_scores == 0:
        return "You lose! The dealer has a blackjack."
    elif my_scores == 0:
        return "You win! Blackjack!"
    elif computer_scores > 21:
        return "You win! The dealer bust!"
    elif computer_scores < my_scores:
        return "You win!"
    else:
        return "You lose!"


continue_flag = True
while continue_flag:
    is_play = input("Do you want to play Blackjack? Type 'y' or 'n' ")
    if is_play == "n":
        continue_flag = False
    else:
        print(logo)
        my_cards = [deal_card(), deal_card()]
        computer_cards = [deal_card(), deal_card()]
        game_over = False
        while not game_over:
            my_scores = calculate_score(my_cards)
            computer_scores = calculate_score(computer_cards)
            print(
                f"Your cards are: {my_cards}, and your current score is: {my_scores}."
            )
            print(f"Computer's first card is : {computer_cards[0]}")
            if my_scores == 0 or computer_scores == 0 or my_scores > 21:
                game_over = True
            else:
                deal_more = input("Want another card? Type 'y' or 'n' ")
                if deal_more == 'y':
                    my_cards.append(deal_card())
                else:
                    game_over = True
        while computer_scores != 0 and computer_scores < 17:
            computer_cards.append(deal_card())
            computer_scores = calculate_score(computer_cards)

        print(f"Your final hand: {my_cards}, final score: {my_scores}.")
        print(
            f"Computer final hand: {computer_cards}, final score: {computer_scores}."
        )
        print(compare_results(my_scores, computer_scores))

print("Thanks for playing!")
