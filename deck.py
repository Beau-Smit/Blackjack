from random import shuffle as r_shuf
from card import Card


class Deck:
    '''
    Each of the 4 suits has cards with values 2-9 and 11 (Ace card), and 4 
    cards with the value 10 (i.e. 10 card, Jack, Queen, and King). This means 
    each suit has 13 cards.

    Attributes
    ----------
    cards - the cards that remain undealt
    discard - the cards that have already been used during the game

    Properties
    ----------
    size - number of cards remaining in deck
    '''


    def __init__(self):
        '''Constructor for the Deck class. Builds a deck of 52 cards.
        '''
        self.cards = []
        self.discard = []

        faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in Card.ALL_SUITS:
            for i in range(1, len(faces) + 1):
                if faces[i-1] == 'A':
                    self.cards.append(Card(suit, 11, i, faces[i-1]))
                elif faces[i-1] in ['J', 'Q', 'K']:
                    self.cards.append(Card(suit, 10, i, faces[i-1]))
                else:
                    self.cards.append(Card(suit, i, i, faces[i-1]))
        

    def deal(self):
        '''
        This method removes the top card on the deck and returns it.
        '''
        if self.size <= 13:
            self.shuffle()

        return self.cards.pop()


    def shuffle(self):
        '''
        This method randomly shuffles all the already dealt cards and places 
        them at the bottom of the deck. It returns
        '''
        r_shuf(self.discard)
        # I pop from the right side of cards so preserve top card
        self.cards = self.discard + self.cards
        self.discard = []


    @property
    def size(self):
        '''
        Returns the number of cards left in the deck.
        '''
        return len(self.cards)

