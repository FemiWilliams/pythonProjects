# blackjack.py

from blackjack_art import logo
from random import choice
print (logo)
print("Welcome to the Blackjack Game")

cards = {"|A|":11, "|2|":2, "|3|":3, "|4|":4, "|5|":5, "|6|":6, "|7|":7, "|8|":8, "|9|":9, "|10|":10, "|J|":10, "|Q|":10, "|K|":10}

def play_game():
    """A single game of blackjack in one func"""
    
    dealer_score = 0
    player_score = 0

    dealer_score, dealer_hand = dealerplay()

    if dealer_score > 21:
        reveal_hands(dealer_score=dealer_score, dealer_hand=dealer_hand)
        return

    player_score, player_hand = playerturn()

    if player_score > 21:
        reveal_hands(player_score=player_score, player_hand=player_hand, dealer_hand=dealer_hand)
        return

    reveal_hands(player_score, player_hand, dealer_score, dealer_hand)

def reveal_hands(player_score="busted", player_hand="busted", dealer_score="busted", dealer_hand="busted"):
    """Displays the cards for each player and declares a winner of the game"""

    print("Dealer hand:")
    for card in dealer_hand:
                print(f"{card[0]}", end=" ")
    print("\n")

    if player_score == "busted":
        print(f"Dealer busts with a score of {dealer_score}! You win!")
    elif dealer_score == "busted":
        print(f"You bust with a score of {player_score}! You lose!")
    elif player_score > dealer_score:
        print("Player hand:")
        for card in player_hand:
                print(f"{card[0]}", end=" ")
        print("\n")
        print(f"Dealer has a score of {dealer_score}, you have a score of {player_score}. You win!")
    elif dealer_score > player_score:
        print("Player hand:")
        for card in player_hand:
                print(f"{card[0]}", end=" ")
        print("")
        print(f"Dealer has a score of {dealer_score}, you have a score of {player_score}. You lose!")
    else:
        print("Player hand:")
        for card in player_hand:
                print(f"{card[0]}", end=" ")
        print("")
        print(f"It's a tie! Both player and dealer have {player_score}.")



def dealerplay():
    """plays the dealer's hand"""
    dealerscore = 0
    dealer_hand = []

    while dealerscore < 17:
        dealer_hand.append(draw_card())
        dealerscore = check_score(dealer_hand)

    print("Dealer hand:")
    
    print("|X|", end=" ")


    for card in range(1, len(dealer_hand)):
       print(f"{dealer_hand[card][0]}", end=" ")



    print("")

    return dealerscore, dealer_hand

def playerturn():
    playerscore = 0
    player_hand = []
    keephitting = True

    player_hand.append(draw_card())
    player_hand.append(draw_card())

    print("")
    print("Player hand:")

    for card in player_hand:
        print(f"{card[0]}", end=" ")

    print("")

    while keephitting:
        choice = input("Would you like to hit or to stay? ").lower()
        print(choice)

        if choice == "hit":
            player_hand.append(draw_card())
            print("")
            for card in player_hand:
                print(f"{card[0]}", end=" ")
            playerscore = check_score(player_hand)
        elif choice =="stay":
            keephitting = False
            print("")
            for card in player_hand:
                print(f"{card[0]}", end=" ")
            print("")
            playerscore = check_score(player_hand)
        else:
            print("Please choose either to \"hit\" or to \"stay\".")
    
    return playerscore, player_hand

def draw_card():
    """returns a random card from the deck (cards)"""
    drawn_card = choice(list(cards.items()))
    #print(drawn_card)
    return drawn_card

def check_score(hand):
    aces = 0
    score = 0
    for key in hand:
        if key[1] == 11:
            aces += 1
        score += key[1]
    
    for ace in range(aces):
        if score > 21:
            score -= 10

    return score

def gameloop():

    # one sentinel for the inner game loop (active game), and another for the outer game loop ('continue?')
    game_over = False
    keep_playing = True

    while keep_playing:
        play_game()
        continue_game = input("Play another game? (Y/N) ").upper()

        while game_over == False:
            if continue_game == "N":
                keep_playing = False
                game_over = True
            elif continue_game == "Y":
                game_over = True
            else:
                print("Please answer yes (Y) or no (N): ")

        game_over = False

gameloop()