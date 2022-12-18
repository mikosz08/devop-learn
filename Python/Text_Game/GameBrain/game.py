
from Character.player_character import PlayerCharacter


class Game():
    
    def __init__(self) -> None:
        # Create Character
        self.player_character = PlayerCharacter().create()
        self.player_character.show_statistics()
        
        

    
        

