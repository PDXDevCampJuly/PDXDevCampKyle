"""
This should run a blackjack game.
"""

from itertools import product
from random import shuffle


class Game:
    """
    The overlord class that controls the game.

    Arguments:
    num_players: The number of user-controlled players.
    num_decks: The number of 52-card decks that make up the shoe.
    shoe: The Shoe object that maintains the list of Cards.
    dealer: The Dealer object - a special Player that must follow house rules.
    players: A list of user-controlled Player objects
    """

    def __init__(self, num_players, num_decks):
        self.shoe = Shoe(num_decks)
        self.dealer = Dealer("DEALER")
        self.players = []
        for x in range(num_players):
            name = input("What is Player {}'s name? >> ".format(x + 1))
            self.players.append(Player(name))

    def play(self):
        """Engine method that drives play."""
        # we track if the players want to continue playing with a flag variable
        playing = True
        while playing:
            self.deal_hand()
            for player in self.players:
                # while the player may still want to hit
                while player.status == "...":
                    self.get_player_input(player)
            # once all players have played, the dealer reveals the hole card
            self.dealer.hand[0].showing = True
            print("The Dealer is playing.")
            self.dealer.count_cards()
            while self.dealer.wants_card():
                self.dealer.hand.append(self.shoe.deal_card())
                self.dealer.count_cards()
            # if dealer stops hitting before busting
            if self.dealer.status == "...":
                self.dealer.status = "finished"
            for player in self.players:
                if player.status == "staying":
                    self.determine_winner(player)
            self.print_board()
            choice = input("Type 'y' or 'yes' to play a new hand. >> ")
            # if they don't want to keep playing, change the flag variable
            if choice.lower() not in ['y', 'yes']:
                playing = False
            else:
                self.reset_board()

    def print_board(self):
        """Displays the game status in readable format."""
        print("\n")
        print(" ".join([str(self.dealer).ljust(25)+":"] + [str(card) for card in self.dealer.hand]))
        print("-" * 50)
        for player in self.players:
            print(" ".join([str(player).ljust(25)+":"] + [str(card) for card in player.hand]))
        print("\n")

    def deal_hand(self):
        """
        Deals initial cards to all players and computes starting scores.
        """
        down_card = self.shoe.deal_card()
        down_card.showing = False
        self.dealer.hand.append(down_card)
        self.dealer.hand.append(self.shoe.deal_card())
        for player in self.players:
            player.hand.append(self.shoe.deal_card())
            player.hand.append(self.shoe.deal_card())
            player.count_cards()

    def get_player_input(self, player):
        """
        Offers the Player a chance to hit, and updates the Player's
        hand, score, and status accordingly.

        player = the Player object whose turn it is.
        """
        self.print_board()
        choice = input(
            "{}: Type 'h' or 'hit' to hit, nothing to stay. >> ".format(player.name)
        )
        if choice.lower() in ['h', 'hit']:
            player.hand.append(self.shoe.deal_card())
            # count_cards checks for blackjacks and busts
            player.count_cards()
        else:
            player.status = "staying"

    def determine_winner(self, player):
        """
        Determines whether a Player defeated the Dealer, and adjusts
        the player's status accordingly.

        player = the Player object being compared to the Dealer
        """
        if self.dealer.status == "BUSTED":
            player.status = "WINNER!"
        else:
            if player.score > self.dealer.score:
                player.status = "WINNER!"
            elif player.score < self.dealer.score:
                player.status = "loser..."
            else:
                player.status = "Push."

    def reset_board(self):
        """
        Prepares the Players and Dealer to begin a new hand.
        """
        self.dealer.hand = []
        self.dealer.score = "XX"
        self.dealer.status = "..."
        self.dealer.showing = False
        for player in self.players:
            player.hand = []
            player.status = "..."
        # if there aren't 5 cards left per player, shuffle
        if len(self.shoe.cards) < (len(self.players) + 1) * 5:
            self.shoe.shuffle()
            print("Honestly, who shuffles a shoe?!")




class Card:
    """
    An individual card.

    Arguments:
    denom = the card's denomination (e.g., Ace, Two, Three)
    suit = the card's suit (e.g., clubs)
    DENOM_VALUE = a dictionary with denominations as keys and
        score points as values
    """

    # helps convert passed denominations to starting values
    DENOM_VALUE = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11
    }

    def __init__(self, denom, suit):
        self.denom = denom
        # the card's value as it pertains to the player's hand
        self.value = Card.DENOM_VALUE[denom]
        self.suit = suit
        # whether or not the card is visible (for dealer hole card)
        self.showing = True

    def __repr__(self):
        """Returns a string to represent the Card"""
        # if the card is showing, display its denomination and suit
        if self.showing:
            return "{}{}".format(self.denom, self.suit)
        # otherwise, show the back of a card (via unicode)
        else:
            return "\U0001F0A0" # card back (longer unicode uses capital 'U')

    def demote(self):
        """
            Demotes an Ace's value from 11 to 1, returns whether or not
            the card was demoted.
        """
        # if an Ace of full value, lower the value to 1 and report success
        if self.value == 11:
            self.value = 1
            return True
        # otherwise, let the calling method know the demotion failed
        else:
            return False

class Shoe:
    """
    A collection of decks of 52 Card objects, shuffled.

    Arguments:
    num_decks = the number of 52-card decks to be shuffled together
    """

    # constants to help deck generation
    DENOMS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    SUITS = ['\u2660', '\u2663', '\u2665', '\u2666'] # suits (schd) in unicode

    def __init__(self, num_decks):
        self.num_decks = num_decks
        self.cards = []
        self.shuffle()

    def shuffle(self):
        """Resets and shuffles the shoe."""
        self.cards = []
        for deck in range(self.num_decks):
            for denom, suit in product(Shoe.DENOMS, Shoe.SUITS):
                self.cards.append(Card(denom, suit))
        shuffle(self.cards)

    def deal_card(self):
        """Takes a Card object out of the Shoe and returns it."""
        return self.cards.pop()


class Player:
    """
    Any entity that has a hand (i.e., Player or Dealer).

    Arguments:
    name = Player's name
    hand = list of Cards the Player owns
    score = computed total of Player's hand
    status = whether the Player has won, lost, or is still playing ('...')
    """

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0
        self.status = "..."

    def __str__(self):
        """Returns how to cast the Player as a string"""
        return "{} ({}, {})".format(self.name, self.score, self.status)

    def __repr__(self):
        """Returns a string to represent the Player"""
        return "<Player object: name='{}'>".format(self.name)

    def count_cards(self):
        """
        Compute the score of the hand and, if necessary, adjust the status
        of the Player.  We use return simply to leave the function.
        """
        count = 0
        for card in self.hand:
            count += card.value
        # if our count is over 21, we're going to try to discount an Ace.
        if count > 21:
            # try to demote each card
            for card in self.hand:
                # if a card successfully demotes, quit
                if card.demote():
                    break
            # if we can't successfully demote a card, we have busted
            else:
                self.status = "BUSTED"
                self.score = count
                return
            # update the count (in case of demotion)
            count = 0
            for card in self.hand:
                count += card.value
        self.score = count
        # if you got a blackjack, declare immediate victory
        if self.score == 21:
            self.status = "WINNER!"


class Dealer(Player):
    """
    The Dealer is a Player object, but must conceal their score until
    all other Players have played and then move by rule.

    Arguments: same as Player.
    """

    def __init__(self, name):
        # do all the setup for a usual Player object
        super().__init__(name)
        # overwrite showing to be False
        self.score = "XX"
        self.showing = False

    def wants_card(self):
        """Returns whether or not the Dealer must hit (bool)."""
        return self.score <= 17

if __name__ == '__main__':
    print("Welcome to blackjack!")
    num_players = int(input("How many human players? >> "))
    num_decks = int(input("How many decks would you like in the shoe? >> "))
    game = Game(num_players, num_decks)
    game.play()
