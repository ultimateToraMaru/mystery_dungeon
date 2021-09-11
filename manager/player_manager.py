from manager.character_manager import Character_manager
import pyxel


class Player_manager(Character_manager):
    def __init__(self, player):
        super().__init__(player)

    def get_input(self):
        super().character.action = 'none'
        if pyxel.btnp(pyxel.KEY_D):
            super().character.direction = 'right'

        elif pyxel.btnp(pyxel.KEY_A):
            super().character.direction = 'left'

        elif pyxel.btnp(pyxel.KEY_W):
            super().character.direction = 'up'

        elif pyxel.btnp(pyxel.KEY_S):
            super().character.direction = 'down'

        elif pyxel.btnp(pyxel.KEY_E):
            super().character.action = 'attack'