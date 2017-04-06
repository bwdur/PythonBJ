import collections
from random import randint

Card = collections.namedtuple('Card',['rank','suit'])

class Player:
    def __init__(self, name, bankroll=100):
        self.bankroll = bankroll
        self.name = name

class Deck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

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

def main():
    player = Player("Brent", 1000)
    print(player.bankroll)
    deck = Deck()

    print(deck)

if __name__ == '__main__':
    main()
