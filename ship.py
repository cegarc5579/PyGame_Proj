import pygame
#pygame treats all game elements like rectangles

class Ship:
    #class manages the ship bmp pile that we are uploading
    def __init__(self, ai_game):
        #this puts the ship picture in its starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        #the following code gets the image from the file 
        # that we saved it in
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
    #this puts every new ship at the bottom center of the screen 
    #midbottom spares you from doing any of the calculations 
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        #draws the ship at its current location?
        #what does this mean?
        #this draws the image to the screen at the position specificed by
        #self.rect, which is midbottom
        self.screen.blit(self.image,self.rect)