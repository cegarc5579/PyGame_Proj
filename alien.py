import pygame
from pygame.sprite import Sprite
#pretty  much doing the same as the ship file
#so that we import the alien pic onto the screen
class Alien(Sprite):
    
    def __init__(self,ai_game):
         #brings the alien and puts it in starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #this loads the image of the alien from where it is stored
        #and sets its rect attribute 
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()
        #this brings the alien to the top left of the screen
        #change this if you want to change the location in which it spawns
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #this sets the pic of the alien using the x axis 
        self.x = float(self.rect.x)
    def check_edges(self):
        #code to return true if alien is at edge and will move back
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <=0:
            return True

    def update(self):
        #this moves the alien to the right
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

   




       


