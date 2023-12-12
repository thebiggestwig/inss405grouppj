import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

# this is the code that creates an array of possible responses from the deck.
# Since the value of cards range from 2-11, with 4 of each suit. This is the
# artihmetic we chose to cover all deck card outcomes.
# - Chimdi

def deal_cards(deck, num_cards=2):
    hand = random.sample(deck, num_cards)
    return hand

# this is the code that declares the hand of the dealer and the player
# while using the function to randomize the array of deck responses. Each
# person (the dealer and player) get a designated hand
# - Chimdi

def calculate_total(hand):
    return sum(hand)

# Previously, as in Blackjack, we used 'num_cards' to declare only two cards
# per participant. This function is run here to take our 'hand' varaible and
# add up the values to generate a sum to be later set to the rules of
# the game of Blackjack.
# - Chimdi

def hit(hand):
    card = random.choice(deck)
    hand.append(card)
    return hand

# This part of the code is used to designate the effect of deciding to 'hit'
# The results are a random card being selected from the aformentioned deck
# And appended to the 'hand' that both participants have
# - Chimdi

def print_results(dealer_hand, player_hand):
    print("Dealer's hand:", dealer_hand)
    print("Your hand:", player_hand)

# This part of the code initiates the game by handling the processing and
# random selection of cards for each player in the background. Instead, upon
# Start of the code running, a message is printed letting the player see what
# Their cards are, along with the dealer's first two cards.
# - Chimdi

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

# This part of the code includes an if else statement. 
# This check to see if the total value of the player’s hand is equal to 21. If the statement is true, then they have Blackjack. 
# If they do not have a hand equal to 21, then the dealer’s hand is checked to see if they have 21. If the statement is true then the message that the dealer has Blackjack will print. 


def play_game():
    print("Welcome to the Blackjack game!\n")
    dealer_hand = deal_cards(deck, 2)
    player_hand = deal_cards(deck, 2)

# This part of the code is the start of the game with a welcome message 
# The deal_cards function is used to give two cards each to both the dealer and the player 
    
    if check_blackjack(dealer_hand, player_hand):
        return

# This part of code uses the check_blackjack function in order to check to see whether either the dealer or the player has a Blackjack
# If either has Blackjack, the game concludes 

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

# This part of code is where the game enters a loop where the player is repeatedly asked to Hit or Stand 
# If they choose to Hit, a card is added to their hand. However, if their total count in hand exceeds 21, they bust and lose the game 
# If the player chooses to Stand, the dealer will draw cards until their total is at least 17
# The results of the round are then printed based on the final total values in hand for both the player and the dealer 
# If the dealer busts, the player wins 
# If the players total is higher than the dealers, the player wins 
# If the players total is lower than the dealers, the player loses 

if __name__ == "__main__":
    play_game()
