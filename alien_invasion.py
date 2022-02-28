import sys
from time import sleep 


import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship 
from bullet import Bullet
from alien import Alien



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
        #create an instance of game stats
        self.stats = GameStats(self)
        #creates an instance to store game stats and create a scoreboard 
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        #this creates a group to hold the fleet of aliens
        self._create_fleet()
        #this code makes the play button 
        self.play_button = Button(self, "Play")

        #set the background color
        #red,green,blue
        self.bg_color = (self.settings.bg_color)

    
    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets() #this updates position of bullet while true
                self._update_aliens()
            
            
            self._update_screen()
         
         
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
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self,mouse_pos):
        #start a new game when player click play code
        #the next two lines of code allow for the play button to not be clicked on
        #even when it isn't visible on the screen
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #this code resets the game settings
            self.settings.initialize_dynamic_settings()
            #this hides the mouse cursor
            pygame.mouse.set_visible(False)

            #reset game stats
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            #get rid of anything else
            self.aliens.empty()
            self.bullets.empty()

            #create a new fleet and center the new ship
            self._create_fleet()
            self.ship.center_ship()
  
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        #this next code is for when Q is pressed
        #when Q is pressed the game will quit
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        #creates a new bullet and adds it to the bullets group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
#update_screen redraws the screen on each pass through the main loop

    def _update_bullets(self):
        #gets rid of bullets that have disappeared
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
                #print(len(self.bullets))

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        #this checks to see if bullets and aliens have collided
        #groupcollide compares rects to see if they have collided
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
#this is to repopulate the fleet if the screen is empty
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            self.stats.level += 1
            self.sb.prep_level()


    def _update_aliens(self):
        #updates the position of the aliens in the fleet
        #checks if the fleet is at an edge, then update positions of all aliens in the fleet 
        self._check_fleet_edges()
        self.aliens.update()

        #this is for when aliens crash into the ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        #this is for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    def _create_fleet(self):
        #this makes an alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        #creating a fleet of aliens
        alien_width = alien.rect.width
        #this is the width available minus two alien widths
        available_space_x = self.settings.screen_width - (2*alien_width)
        #this puts the number of aliens on screen by calculating 
        #the available space * two times width of an alien
        #floor division (//) gives you a whole integer
        number_aliens_x = available_space_x // (2*alien_width)
        #this is to find out how many rows of aliens fit on the game screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3*alien_height)- ship_height)
        number_rows = available_space_y // (2*alien_height)

        #creates rows of aliens
        for row_number in range(number_rows):
        #creates the first row of aliens
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
    
    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        #why is alien_height appearing blacked out? 
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 *alien.rect.height * row_number
        self.aliens.add(alien)

    #this checks to see if alien has reached the edge
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
#following code changes direction of fleet when edge is hit 
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
            #this moves the aliens left because of the -1
        self.settings.fleet_direction *= - 1

    def _ship_hit(self):
        #decreases number of ships left when hit 
        if self.stats.ships_left>0:
            self.stats.ships_left -= 1
            self.sb.prep_ships() #this decrements ship s left and updates the scoreboard
        #deletes any remaining aliens and bullets 
            self.aliens.empty()
            self.bullets.empty()
        #resets the game and creates a new fleet and centers the ship 
            self._create_fleet()
            self.ship.center_ship()
    #pause in between the games 
            sleep(0.5)
        else:
            self.stats.game_active = False
            #this next line causes cursor to reappear when game is over
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

        

    def _update_screen(self):
        #this method updates the image on the screen
         #this calls on the color that we set in the init method
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #this updates the screen and adds the alien
        self.aliens.draw(self.screen)
        
        #this updates the sceen and draws the scoreboard onto the screen
        self.sb.show_score()

        #draw the play button is game isn't active
        if not self.stats.game_active:
            self.play_button.draw_button()


        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
