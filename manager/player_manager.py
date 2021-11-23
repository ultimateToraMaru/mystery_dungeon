from dungeon.display import Display
from exp_machine import Exp_machine
from manager.character_manager import Character_manager
import pyxel
import pygame


class Player_manager(Character_manager):
    def __init__(self, player):
        super().__init__(player)
        self.__exp_machine = Exp_machine()

    def get_input(self):
        keys=pygame.key.get_pressed()

        super().character.action = 'move'

        if keys[pygame.K_LSHIFT]:
            super().character.action = 'none'

        if keys[pygame.K_d]:
            super().character.direction = 'right'

        elif keys[pygame.K_a]:
            super().character.direction = 'left'

        elif keys[pygame.K_w]:
            super().character.direction = 'up'

        elif keys[pygame.K_s]:
            super().character.direction = 'down'

        elif keys[pygame.K_e]:
            super().character.action = 'attack'

    def add_exp_machine(self, exp):
        plus_status = self.__exp_machine.add_exp(exp, super().character.level)

        super().character.level += plus_status[0]
        super().character.max_hp += plus_status[1]
        super().character.max_mp += plus_status[2]
        super().character.attack += plus_status[3]
        super().character.defense += plus_status[4]
        super().character.exp += exp

        if (plus_status[0] == 1):
            display = Display.get_instance()
            display.show_level_up(super().character.name,
                                    super().character.level,
                                    plus_status[1],
                                    plus_status[2],
                                    plus_status[3],
                                    plus_status[4])

        # レベルが上がった時: 1, それ以外: 0
        return plus_status[0]
