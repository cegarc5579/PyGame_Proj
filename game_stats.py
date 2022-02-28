class GameStats:

    def __init__(self, ai_game):
        #initialize stats
        self.settings = ai_game.settings
        self.reset_stats()

        #end game when player runs out of ships 
        self.game_active = True

    def reset_stats(self):
        #stats can change during the game
        self.ships_left = self.settings.ship_limit