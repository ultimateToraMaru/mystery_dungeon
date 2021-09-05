from manager.character_manager import Character_manager
import pyxel


class Player_manager(Character_manager):
    def __init__(self, player):
        super().__init__(player)

    def get_input(self):
        if pyxel.btnp(pyxel.KEY_D):
            player_direction = 'right'

        elif pyxel.btnp(pyxel.KEY_A):
            player_direction = 'left'

        elif pyxel.btnp(pyxel.KEY_W):
            player_direction = 'up'

        elif pyxel.btnp(pyxel.KEY_S):
            player_direction = 'down'

        return player_direction