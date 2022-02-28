import pygame.font

class Scoreboard:
    #this is for scoring purposes

    def __init__(self, ai_game):
        #initializes the attributes
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #this is to initialize the font settings 
        #for the scoreboard we are making
        self.text_color(30,30,30)
        self.font = pygame.font.SysFont(None,48)