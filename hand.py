from card import Card
import tkinter as tk


class Hand:
    '''
    This class represents a hand for Blackjack. Notice both the player and the 
    dealer have their own hands.

    Attributes
    ----------
    cards : a collection of Card objects that make up the hand
    '''


    def __init__(self):
        '''Constructor for the Hand class
        '''
        self.cards = []


    @property
    def total(self):
        '''
        Sums the values of the cards in hand.
        '''
        return sum([c.value for c in self.cards])


    def reset(self):
        '''
        Clears your collection of cards.
        '''
        self.cards = []


    def add(self, card):
        '''
        Adds the given card to the collection of cards.
        
        Input:
            card (Card object) - the Card object that shall be added to hand.
        '''
        self.cards.append(card)


    def draw(self, canvas, start_x, start_y, canvas_width, canvas_height):
        '''
        This method draws the hand of cards on to the canvas starting at the 
        location specified (i.e., start_x and start_y). Draw the cards 
        horizontally along the x-axis.

        Input:
            canvas (tk.Canvas object) - the object we will be drawing on
            start_x (int) - where to start on the x axis
            start_y (int) - where to start on the y axis
            canvas_width (int) - canvas's width
            canvas_height (int) - canvas's height
        '''
        horiz = start_x
        imgs = [c.image for c in self.cards]
        for img in imgs:
            canvas.create_image(horiz, start_y, anchor=tk.NW, image=img)
            horiz += 105


    def __repr__(self):
        '''Print statement for Hand
        '''
        return f'{self.cards}'


    def __iter__(self):
        '''make Hand iterable
        '''
        yield from self.cards

