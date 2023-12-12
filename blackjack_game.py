import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4


def deal_cards(deck, num_cards=2):
    hand = random.sample(deck, num_cards)
    return hand


def calculate_total(hand):
    return sum(hand)


def hit(hand):
    card = random.choice(deck)
    hand.append(card)
    return hand


def print_results(dealer_hand, player_hand):
    print("Dealer's hand:", dealer_hand)
    print("Your hand:", player_hand)


def check_blackjack(dealer_hand, player_hand):
    if calculate_total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congratulations! You have a Blackjack!\n")
        return True
    elif calculate_total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you lose. The dealer has a Blackjack.\n")
        return True
    return False


def play_game():
    print("Welcome to the Blackjack game!\n")
    dealer_hand = deal_cards(deck, 2)
    player_hand = deal_cards(deck, 2)
    if check_blackjack(dealer_hand, player_hand):
        return

    while True:
        print_results(dealer_hand, player_hand)
        choice = input("Do you want to [H]it or [S]tand? ").lower()

        if choice == "h":
            hit(player_hand)
            if calculate_total(player_hand) > 21:
                print_results(dealer_hand, player_hand)
                print("Sorry, you busted. You lose.\n")
                return
        elif choice == "s":
            while calculate_total(dealer_hand) < 17:
                hit(dealer_hand)
            print_results(dealer_hand, player_hand)
            if calculate_total(dealer_hand) > 21:
                print("Dealer busts. You win!\n")
            elif calculate_total(player_hand) > calculate_total(dealer_hand):
                print("Congratulations, your score is higher than the dealer. You win!\n")
            elif calculate_total(player_hand) < calculate_total(dealer_hand):
                print("Sorry, your score is lower than the dealer. You lose.\n")
            else:
                print("It's a tie!\n")
            return


if __name__ == "__main__":
    play_game()