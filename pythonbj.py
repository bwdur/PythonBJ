from random import randint

class Player:
    def __init__(self, name, bankroll=100):
        self.bankroll = bankroll
        self.name = name

class Card:
    def __init__(self, suit, rank, deckorder=0):
        self.suit = suit
        self.rank = rank
        self.deckorder = deckorder

class Deck:
    def __init__(self):
        self.suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        self.ranks = list(range(1, 14))
        self.deck = []

        card_num = 1
        for s_index, suit in enumerate(self.suits, start=1):
            for r_index, rank in enumerate(self.ranks, start=1):
                self.deck.append(Card(suit, rank, card_num))
                card_num += 1
    
    def __str__(self):
        str = ''
        for card in self.deck:
            str += "%s -- %s : %s\n" % (card.deckorder, card.suit, card.rank)
        return str

    def shuffle(self):
        lst = list(range(1,53))
        for card in self.deck:
            random_order = randint(0, len(lst)-1)
            card.deckorder = lst[random_order]
            lst.remove(lst[random_order])

    def getTopCard(self):
        pass

def main():
    player = Player("Brent", 1000)
    print(player.bankroll)
    deck = Deck()

    print(deck)

    deck.shuffle()

    print(deck)

    

if __name__ == '__main__':
    main()
