import collections
from time import sleep
from random import shuffle

# TODO Add input checks to bets
# TODO Only print one of the dealer's cards before player has a turn
# TODO Add logic for double and split
# TODO Make dealer's hit cards print one at a time, slowly, for dramatic effect

Card = collections.namedtuple('Card', ['rank', 'suit'])
CARD_VALS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
             '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10,
             'Q': 10, 'K': 10, 'A': 11}

class Player:
    """ A class representing a player of blackjack.
        If no name or bankroll are set, __init__ retrieves
        from the console. """
    cards = []
    hand_value = 0
    bet_amount = 0

    def __init__(self, name='', bankroll=-1, is_dealer=False):
        if name != '':
            self.name = name
        else:
            self.name = self.input_name()
        if bankroll > 0:
            self.bankroll = bankroll
        else:
            self.bankroll = self.input_bankroll(self.name)
        self.is_dealer = is_dealer

    def reset(self, deck):
        self.cards = deck.get_start_cards()
        self.hand_value = self.get_hand_value()

    def adjust_bankroll(self,blackjack=False, double_down=False):
        if blackjack:
            multiplier = 2.5
        elif double_down:
            multiplier = 4
        else:
            multiplier = 2
        self.bankroll = self.bet_amount * multiplier

    def input_bet_amount(self):
        print("CURRENT BANKROLL: $%s" % self.bankroll)
        self.bet_amount = int(input("Enter your bet amount: "))
        self.bankroll -= self.bet_amount

    def input_name(self):
        """ Gets the player's name from the console. """
        return input("Hello! What is your name? ")

    def input_bankroll(self, name=''):
        """ Gets the player's bankroll from the console. """
        return int(input("What is your starting bankroll, %s? " % name))

    def get_hand_value(self):
        hand_value = 0
        aces = [c for c in self.cards if c.rank == 'A']
        for card in self.cards:
            hand_value += CARD_VALS[card.rank]
        if hand_value > 21 and len(aces):
            for card in self.cards:
                if card.rank == 'A' and hand_value > 21:
                    hand_value -= 10
        return hand_value

    def print_cards(self, hide_card=True):
        if len(self.cards) <= 2 and hide_card and self.is_dealer:
            print(self.cards[0])
            print("---*****-----*****----*****---")
        else:
            for card in self.cards:
                print(card)

    def print_name(self):
        print("-------- %s -----------\n" % self.name.upper())

    def hit(self, deck):
        """ Add a card to player cards """
        self.cards.append(deck.pop())
        self.hand_value = self.get_hand_value()

    def print_hand_value(self, hide_card=True):
        if len(self.cards) <= 2 and hide_card and self.is_dealer:
            value = "**"
        else:
            value = self.hand_value
        print("\n============%s==============\n" % value)


class Deck:
    """ A class that represents a deck of cards.
    Implements getitem, setitem, len, repr"""
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, card):
        self._cards[position] = card

    def __repr__(self):
        outstr = ''
        for card in self:
            outstr += str(card) + '\n'
        return outstr

    def pop(self):
        """ Pops off the top card in the deck """
        return self._cards.pop()

    def get_start_cards(self):
        return [self._cards.pop(), self._cards.pop()]

def print_welcome():
    print("Welcome to blackjack!")

def get_start_cards(deck):
    """ Returns a list of two cards """
    return [deck.pop(), deck.pop()]

def play_hand(player_cards, dealer_cards):
    """ Play a hand of blackjack until player busts or stays """
    pass

def print_cards(*players):
    for p in players:
        p.print_name()
        p.print_cards()
        p.print_hand_value()

def main():
    """ MAIN """
    print_welcome()
    player = Player() # Uncomment to get input from console
    #player = Player(name='Brent', bankroll=1000)
    dealer = Player(name='Dealer', bankroll=1, is_dealer=True)

    while player.bankroll > 0:
        print("\nHere we go, %s!\n" % player.name)
        deck = Deck()
        shuffle(deck)
        player.input_bet_amount()

        player.reset(deck)
        dealer.reset(deck)
        print_cards(dealer, player)

        if player.hand_value == 21:
            print("Blackjack!")
            player.win_hand(blackjack=True)
        else:
            answer = 'h'

            while answer == 'h' and player.hand_value <= 21:
                print("Your current hand value: %s" % player.hand_value)
                answer = input('Enter h for hit, d for double down, or s for stand: ')
                print("\n")
                if answer == 'h' or answer == 'd':
                    player.hit(deck)
                    print_cards(dealer, player)
                else:
                    pass

            if player.hand_value > 21:
                print("Too bad, you lose. Sorry!")
            else:
                # IMPLEMENT DEALER HITS AND STANDS
                print("It's the dealer's turn.")
                print("You have %s." % player.hand_value)
                print("Dealer has %s." % dealer.hand_value)
                print("Good luck! Dealer's turn...")
                dealer.print_cards(hide_card=False)

                while dealer.hand_value < 17:
                    sleep(2)
                    dealer.hit(deck)
                    print(dealer.cards[-1])

                sleep(1)
                dealer.print_hand_value(hide_card=False)
                sleep(2)

                if dealer.hand_value > 21 or player.hand_value > dealer.hand_value:
                    print("You win!")
                    player.win_hand()
                elif dealer.hand_value > player.hand_value:
                    print("You lose :(")
                    if answer == 'd':
                        player.bankroll -= player.bet_amount
                else:
                    print("Tie!")
                    player.bankroll += player.bet_amount

if __name__ == '__main__':
    main()
