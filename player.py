import math
import random

class player:
    def __init__(self, letter):
        #letter is x or 0
        self.letter = letter

    #we want all player to get their next move or given a game
    def get_move(self, game):
        pass

class randomcomputerplayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self,game):
        pass

class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self,game):
        pass

