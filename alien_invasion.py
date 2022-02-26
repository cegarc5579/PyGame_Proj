import sys
import pygame

from settings import Settings
from ship import Ship 



class AlienInvasion:

    def __init__(self):
        #this calls the background setting for the game
        pygame.init()
        self.settings = Settings()


        #the following code runs the game in full screen mode

        #self.screen = pygame.display.set_mode((0,0), pygame. FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        
        #this creates a screen for the game to run on 
        #1200 and 800 are th dimensions on the window
        #use self.screen so it will be available in all methods in the class
        #self.screen is a SURFACE, allows for game elements to be displayed        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

        #set the background color
        #red,green,blue
        self.bg_color = (self.settings.bg_color)

    
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            #this for loop returns list of events that have happened
            #event is action performed by user 
            #we removed the code that belongs to the notes above
            #and put it under the updata screen 
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #this elif detects a keydown event
            #and it chekcs if a key pressed triggers an actions
            #this affects the ship by a value of 1 when a key is pressed
            #these statements for when the button is being pressed
            #so the ship can move to either direction
            #true means left or right key is being pressed
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
        #these statements are for when the buttons are not being pressed
        #movement left and right is stopped 
        #false means no key press
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
  
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        #this next code is for when Q is pressed
        #when Q is pressed the game will quit
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        #this method updates the image on the screen
         #this calls on the color that we set in the init method
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
