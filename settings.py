class Settings:
    #this is used to store all settings for the game
    #allow to modify the game's appearance
    #initialize the game static settings
    def __init__(self):
        #do you take this out of the other game file if setting it here?
        # so yes, you replace the hard code in the other
        # and call self.___ whatever you need to use and put it
        # in the alien invasion file 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #bullet settings
        #this creates a dark gray bullet with a width of 3 pixels and a 
        #height of 15 pixels
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3 #this limits the number of bullets on the screen

        #this code sets how fast the ship is moving when a left/right key 
        #is pressed 
        #moves 1.5 pixels when a button is pressed instead of 1 pixel
        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 2 #this sets the number of ships the player starts with 

        #slien settings, setting speed at which they move
        self.alien_speed = 4.0
        self.fleet_drop_speed = 10 #how wuick the fleet drops down when reaches the edge
        self.fleet_direction = 1 #1 represents it will move right and -1 means the ships move left

        #how quickly the game speeds up 
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):

        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        #fleet direction, 1 means it'll move right and -1 means itll move left
        self.fleet_direction = 1
#increases everything once a new level is reached 
    def increase_speed(self):

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
