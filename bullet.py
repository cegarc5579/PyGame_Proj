import pygame
from pygame.sprite import Sprite
#Sprite allows you to group related eleemtns in a your game
#and all elements act all at once

class Bullet(Sprite):
    #this class manages the bullets that are fired
    def __init__(self,ai_game):
        #this cretaes a bullet where the ship currently is
        #call on super to inherit properly from sprite 
        super().__init__()
        self.screen = ai_game.screen
        #calling these from settings file
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        #creates the bulleet at 0,0 and puts it in the right position
        self.rect = pygame.Rect(0,0,self.settings.bullet_width, self.settings.bullet_height)
        #this makes the bullet on top of the ship 
        self.rect.midtop = ai_game.ship.rect.midtop
    #this stores the bullets position as a decimal value on the y axis
        self.y = float(self.rect.y)
    
    def update(self):
        #this moves the bullet up the screen
        #calling bullet speed from settings file
        #moves on the Y axis
        self.y -= self.settings.bullet_speed
        #updates the rect position
        self.rect.y = self.y 

    def draw_bullet(self):
        #calling on things that were creted inthis file but were called form another file
        pygame.draw.rect(self.screen, self.color, self.rect)
