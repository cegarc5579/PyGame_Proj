class Settings:
    #this is used to store all settings for the game
    #allow to modify the game's appearance
    def __init__(self):
        #do you take this out of the other game file if setting it here?
        # so yes, you replace the hard code in the other
        # and call self.___ whatever you need to use and put it
        # in the alien invasion file 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #this code sets how fast the ship is moving when a left/right key 
        #is pressed 
        #moves 1.5 pixels when a button is pressed instead of 1 pixel
        self.ship_speed = 1.5