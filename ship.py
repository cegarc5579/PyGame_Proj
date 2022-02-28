import pygame
#pygame treats all game elements like rectangles
from pygame.sprite import Sprite

class Ship(Sprite):
    #class manages the ship bmp pile that we are uploading
    def __init__(self, ai_game):
        super().__init__()
        #this puts the ship picture in its starting position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        #the following code gets the image from the file 
        # that we saved it in
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
    #this puts every new ship at the bottom center of the screen 
    #midbottom spares you from doing any of the calculations 
        self.rect.midbottom = self.screen_rect.midbottom
#this stores a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
#this is a movement flag
#we add this moving_right here because the Ship file controls everything
#related to the manipulation of the ship image
#movement flags
        self.moving_right = False 
        self.moving_left = False
#this is a method that controls the movement of the ship 
#LOOK AT PAGE 242 TO UNDERSTAND WHAT THIS MEANS
    def update(self):
        #the additions to the if statements prevent the ship from 
        #moving outside the screen it is in 
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
#this controls the position of the ship 
#so when it moves it updates self.rect.x
        self.rect.x = self.x
    
    def blitme(self):
        #draws the ship at its current location?
        #what does this mean?
        #this draws the image to the screen at the position specificed by
        #self.rect, which is midbottom
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)