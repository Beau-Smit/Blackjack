import tkinter as tk
import os
import re


class Card:
    '''
    This class represents a card It can be one of 4 suits and 13 faces.

    Class attributes
    ----------
    CLUBS, DIAMONDS, HEARTS, SPADES - all hold the string representations of that
    particular suit.
    card_images - holds a collection of tk.PhotoImage

    Attributes
    ----------
    suit - the card's suit
    value - between 2-11 representing the score the card is worth
    _id - between 1-13 representing the numeric value for file read in
    face - the number or character representation of cards, i.e. "A", "4", "Q"
    '''

    CLUBS = "clubs"
    DIAMONDS = "diamonds"
    HEARTS = "hearts"
    SPADES = "spades"
    ALL_SUITS = [CLUBS, DIAMONDS, HEARTS, SPADES]
    card_images = {}

    def __init__(self, suit, value, _id, face):
        '''Constructor for the Card class
        '''
        self.suit = suit
        self._value = value
        self._id = _id
        self.face = face
    

    @classmethod
    def load_images(cls):
        '''
        This classmethod is used to load all the images into the Blackjack
        module so we can update the GUI with card images.
        '''
        for fname in os.listdir(os.path.join(os.getcwd(), 'images')):
            if fname.endswith('.gif') and ('joker' not in fname):
                img_obj = tk.PhotoImage(file=os.path.join(os.getcwd(), 'images', fname))
                expr = re.match(r'(?P<id>\d+)_of_(?P<suit>[a-z]+).gif', fname)
                card_id = f"{expr.group('id')}{expr.group('suit')}"
                cls.card_images[card_id] = img_obj
        
        
    @property
    def value(self):
        '''
        This a getter property that returns the card value. This property does 
        not have a setter.
        '''
        if self._id == 1:
            self._value = 11
        elif self._id < 11:
            self._value = int(self._id)
        else:
            self._value = 10
        return self._value


    @property
    def image(self):
        '''
        This property returns the tk.PhotoImage object from the card_images 
        data structure that represents the Card instance.
        '''
        return self.card_images[f'{self._id}{self.suit}']


    def __repr__(self):
        '''Print statement for Card
        '''
        return f'{self.face}{self.suit[0].upper()}'
        
