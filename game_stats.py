class GameStats():
    '''Stores Alien Invasion statistics.'''
    
    def __init__(self, ai_settings):
        '''Initializes statistical data.'''
        self.ai_settings = ai_settings
        self.reset_stats()

        # The maximum score should never be reset
        self.high_score = 0
        self.read_high_score()

        # Start the game in an idle state
        self.game_active = False
        
    def reset_stats(self):
        '''Initializes statistical data that may change during gameplay.'''
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        '''Read the maximum score from the score.txt file'''
        try:
            with open('score.txt', 'r') as file:
                n = int(file.readline())
                if type(n) == int:
                    self.high_score = n
        except: pass

    def write_high_score(self):
        '''Write the maximum score in the score.txt file'''
        with open('score.txt', 'w') as file:
            file.write(str(self.high_score))
