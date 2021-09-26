from manager.character_manager import Character_manager
import pyxel
import pygame


class Player_manager(Character_manager):
    def __init__(self, player):
        super().__init__(player)

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