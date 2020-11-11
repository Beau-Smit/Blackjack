import tkinter as tk
from abc import ABC, abstractmethod
from deck import Deck
from hand import Hand
from card import Card


class GameGUI(ABC):

    def __init__(self, window):
        self._window = window
        self._canvas_width = 1024
        self._canvas_height = 400
        self._canvas = tk.Canvas(window, width=self._canvas_width, height=self._canvas_height)
        self._canvas.pack()
        window.bind("<Key>", self._keyboard_event)

    def _keyboard_event(self, event):
        key = str(event.char)

        if key == 'h':
            self.player_hit()
        elif key == 's':
            self.player_stand()
        elif key == 'r':
            self.reset()

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def player_hit(self):
        pass

    @abstractmethod
    def player_stand(self):
        pass


class BlackJack(GameGUI):
    '''
    This is the game of Blackjack (with simplified rules). This class 
    inherits from GameGUI.

    Attributes
    ----------
    _player_wins - number of times the player has beat the dealer
    _dealer_wins - number of times the player has lost to the dealer
    _game_status - states whether the game is ongoing or the result of the game
    deck - the cards used to play the game
    _player_hand - the cards dealt to the player
    _dealer_hand - the cards dealt to the dealer
    '''


    def __init__(self, window):
        '''Constructor for the BlackJack class, which inherits from the 
        GameGUI class
        '''
        super().__init__(window)

        self._player_wins = 0
        self._dealer_wins = 0
        self._game_status = "In Progress..."

        # initialize Deck and shuffle to begin
        self.deck = Deck()
        self.deck.shuffle()

        # initialize hands
        self._player_hand = Hand()
        self._dealer_hand = Hand()

        Card.load_images()
        self.reset()


    def update_GUI(self):
        '''This method clears the canvas, updates the text on the screen and 
        draws the new hand. Call this every time you want to make an update to
        the GUI.
        '''

        # clear the entire canvas
        self._canvas.delete(tk.ALL)

        my_font = "Helvetica 15 bold"
        if self._game_status == "In Progress...":
            text_color = "green"
        else:
            text_color = "red"
        
        self._canvas.create_text(512, 200,anchor=tk.CENTER, fill=text_color, 
            font=my_font, text=f'Game Status:{self._game_status}')
        
        self._canvas.create_text(0, 25,anchor=tk.W,  font=my_font,
            text=f'Player Hand Total:{self._player_hand.total}')
        
        self._canvas.create_text(0, 200, anchor=tk.W, font=my_font,
            text=f'Dealer Hand Total:{self._dealer_hand.total}')
        
        self._canvas.create_text(0, 370,anchor=tk.W,  font=my_font,
            text=f'Dealer Wins:{self._dealer_wins}')
        
        self._canvas.create_text(0, 390,anchor=tk.W,  font=my_font,
            text=f'Player Wins:{self._player_wins}')

        # draw the new hand
        self._player_hand.draw(self._canvas, 25, 50, self._canvas_width, self._canvas_height)
        self._dealer_hand.draw(self._canvas, 25, 215, self._canvas_width, self._canvas_height)


    def reset(self):
        '''
        This method restarts the game. This method is automatically called 
        whenever the user hits the “r” key. 
        '''

        # add each hand to the discard, then reset hands
        self.deck.discard += self._player_hand
        self.deck.discard += self._dealer_hand
        self._player_hand.reset()
        self._dealer_hand.reset()

        self._game_status = "In Progress..."

        # deal 2 cards to player
        self._player_hand.add(self.deck.deal())
        self._player_hand.add(self.deck.deal())

        # deal 2 cards to dealer
        self._dealer_hand.add(self.deck.deal())
        self._dealer_hand.add(self.deck.deal())

        self.update_GUI()


    def player_hit(self):
        '''
        This method is automatically called whenever the user hits the “h“ key. 
        The user is requesting to perform a hit on their hand. This method 
        draws a card from the deck and adds it to the player’s hand. Then,
            1. If the player’s hand is over 21 (i.e., a bust) then the player 
            loses.
            2. If the player’s hand is under 21, then the game needs to update 
            the GUI. The dealt card should be shown and the player’s hand total 
            should be updated.
        '''

        # only allow hits if player is under 21
        if self._game_status == "In Progress...":
            self._player_hand.add(self.deck.deal())
            self.update_GUI()

            if self._player_hand.total > 21:
                self._game_status = "Dealer WINS... Press 'r' to start a new game"
                self._dealer_wins += 1
                self.update_GUI()

        
    def player_stand(self):
        '''
        This method is automatically called whenever the user hits the “s“ key.
        The user is requesting to perform a stand on their hand. The method 
        will continuously add cards to the dealer’s hand until their hand is 
        greater than or equal to 17.
        '''

        if self._game_status == "In Progress...":
            while self._dealer_hand.total < 17:
                self._dealer_hand.add(self.deck.deal())
            if self._dealer_hand.total > 21:
                # dealer bust
                self._player_wins += 1
                self._game_status = "Player WINS... Press 'r' to start a new game"
            else:
                if self._player_hand.total > self._dealer_hand.total:
                    self._game_status = "Player WINS... Press 'r' to start a new game"
                    self._player_wins += 1

                elif self._player_hand.total < self._dealer_hand.total:
                    self._game_status = "Dealer WINS... Press 'r' to start a new game"
                    self._dealer_wins += 1

                else:
                    self._game_status = "TIE Game...Press 'r' to start a new game"

            self.update_GUI()


def main():
    window = tk.Tk()
    window.title("Blackjack")
    game = BlackJack(window)
    window.mainloop()


if __name__ == "__main__":
    main()
