import sys
import pygame

from settings import Settings

class AlienInvasion:

    def __init__(self):
        #this calls the background setting for the game
        pygame.init()
        self.settings = Settings()
        #this creates a screen for the game to run on 
        #1200 and 800 are th dimensions on the window
        #use self.screen so it will be available in all methods in the class
        #self.screen is a SURFACE, allows for game elements to be displayed
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #set the background color
        #red,green,blue
        self.bg_color = (self.settings.bg_color)

    
    def run_game(self):
        while True:
            #this for loop returns list of events that have happened
            #event is action performed by user 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #this calls on the color that we set in the init method
                self.screen.fill(self.bg_color)

                pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game
