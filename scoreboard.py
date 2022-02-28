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
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #prepare the initial score image
        self.prep_score() #this turns the text into an image 
    
    def prep_score(self):
        #this puts the score as an image
        #render means you pass the screen bg color and text color 
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,self.text_color, self.settings.bg_color)

        #the next line makes sure that the score lines up with the right side of the scren 
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 #20 pixels from right send of the screen 
        self.score_rect.top = 20 #sets 20 pixels from the top of the screen 
    
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)#this draws the score to the screen 