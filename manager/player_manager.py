from tools.display import Display
from dungeon.room.object_layers.objects.pocket import Pocket
from tools.exp_machine import Exp_machine
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

        elif keys[pygame.K_q]:
            super().character.direction = 'up_left'

        elif keys[pygame.K_e]:
            super().character.direction = 'up_right'

        elif keys[pygame.K_z]:
            super().character.direction = 'down_left'

        elif keys[pygame.K_c]:
            super().character.direction = 'down_right'

        elif keys[pygame.K_r]:
            super().character.action = 'attack'

        # if pyxel.btnp(pyxel.KEY_KP_D):
        #     super().character.direction = 'right'

    def add_exp_machine(self, exp):
        """経験値マシンに経験値を追加

        Args:
            exp (int): 経験値

        Returns:
            status: レベルが上がった時: 1, それ以外: 0
        """
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

    def look_pocket(self):
        item_list: list = super().character.pocket.show()
        return item_list

    def pick_up(self, item):
        super().character.pocket.add_item(item)

        # 拾い上げる時の効果音
        pyxel.play(0, 32, loop=False)

    def check_satiation(self):
        # 満腹度を減らす
        super().character.satiation -= 1
