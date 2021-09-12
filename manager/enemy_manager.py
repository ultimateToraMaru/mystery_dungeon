
import random
from manager.character_manager import Character_manager


class Enemy_manager(Character_manager):
    def __init__(self, enemy):
        super().__init__(enemy)

    def get_input(self):
        super().character.action = 'move'
        target_address_and_pos = super().character.get_target_address_and_pos()
        self_address_and_pos = super().character.get_self_address_and_pos()

        # if (target_address_and_pos[0] == self_address_and_pos[0]+1 or
        #     target_address_and_pos[0] == self_address_and_pos[0]-1 or
        #     target_address_and_pos[1] == self_address_and_pos[1]+1 or
        #     target_address_and_pos[1] == self_address_and_pos[1]-1):
        #     super().character.action = 'attack'
        #     return

        willingness = random.randint(0, 10)  # やる気
        if (willingness > 3):
            if (target_address_and_pos[0] > self_address_and_pos[0]):
                super().character.direction = 'right'
            if (target_address_and_pos[0] < self_address_and_pos[0]):
                super().character.direction = 'left'
            if (target_address_and_pos[1] > self_address_and_pos[1]):
                super().character.direction = 'down'
            if (target_address_and_pos[1] < self_address_and_pos[1]):
                super().character.direction = 'up'
            # else :
            #     com = ['right', 'left', 'down', 'up']
            #     r = random.randint(0, 3)
            #     direction = com[r]
        else :
            com = ['right', 'left', 'down', 'up']
            r = random.randint(0, 3)
            super().character.direction = com[r]

        return super().character.direction