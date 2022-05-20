########################################################## Blackjack ###########################################################
#

################################################################################################################################

import random
import time

suits = ("Spades ♠", "Clubs ♣", "Hearts ♥", "Diamonds ♦")
ranks = (
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K",
    "A",
)
values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}

playing = True

# CLASS DEFINTIONS:


class cards:
    def _init_(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def _str_(self):
        return self.rank + " of " + self.suit


class Deck:
    def _init_(self):
        self.deck = []  # Start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(cards(suit, rank))

    def _str_(self):
        deck_comp = ""  # Start with an empty string
        for cards in self.deck:
            deck_comp += "\n " + cards._str_()  # Add each card object's print string
        return "The deck has:" + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_cards = self.deck.pop()
        return single_cards


class Hand:
    def _init_(self):
        self.cardz = []  # Start with an empty list as we did in the Deck class
        self.value = 0  # Start with zero value
        self.aces = 0  # Add an attribute to keep track of aces

    def add_cards(self, cards):
        self.cardz.append(cards)
        self.value += values[cards.rank]
        if cards.rank == "A":
            self.aces += 1  # Add to self.aces

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# FUNCTION DEFINITIONS:


def hit(deck, hand):
    hand.add_cards(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("\nWould you like to Hit or Stand? Enter [h/s] ")

        if x[0].lower() == "h":
            hit(deck, hand)  # hit() function defined above

        elif x[0].lower() == "s":
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, Invalid Input. Please enter [h/s].")
            continue
        break


def show_some(player, dealer):
    print("\nPlayer's Hand:", *player.cardz, sep="\n ")
    print("Player's Hand =", player.value)
    print("\nDealer's Hand:")
    print(" 'Cards Hidden' ")
    print("", dealer.cardz[1])


def show_all(player, dealer):
    print("\nPlayer's Hand:", *player.cardz, sep="\n ")
    print("Player's Hand =", player.value)
    print("\nDealer's Hand:", *dealer.cardz, sep="\n ")
    print("Dealer's Hand =", dealer.value)


def player_busts(player, dealer):
    print("\n--- Player Busts! ---")


def player_wins(player, dealer):
    print("\n--- Player has blackjack! You win! ---")


def dealer_busts(player, dealer):
    print("\n--- Dealer Busts! You WIN! ---")


def dealer_wins(player, dealer):
    print("\n--- Dealer wins! ---")


def push(player, dealer):
    print("\n TIE!")


# GAMEPLAY!

while True:
    print("\n----------------------------------------------------------------")
    print("                ♠♣♥♦ WELCOME TO BLACKJACK! ♠♣♥♦")
    print("                          Lets Play!")
    print("----------------------------------------------------------------")
    print(
        "Game Rules:  Get as close to 21 as you can without going over!\n\
        Dealer hits until the dealer reaches 17.\n\
        Aces count as 1 or 11."
    )

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_cards(deck.deal())
    player_hand.add_cards(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_cards(deck.deal())
    dealer_hand.add_cards(deck.deal())

    # Show the cards:
    show_some(player_hand, dealer_hand)

    while playing:  # Recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand)
            break

    # If Player hasn't busted, play Dealer's hand
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        time.sleep(1)
        print("\n----------------------------------------------------------------")
        print("                     ★ Final Results ★")
        print("----------------------------------------------------------------")

        show_all(player_hand, dealer_hand)

        # Test different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand)

        else:
            push(player_hand, dealer_hand)

    # Ask to play again
    new_game = input("\nPlay another hand? [Y/N] ")
    while new_game.lower() not in ["Y", "N"]:
        new_game = input("Invalid Input. Please enter Y or N ")
    if new_game[0].lower() == 'Y':
        playing = True
        continue
    else:
        print("\n------------------------Thanks for playing!---------------------\n")
        break
