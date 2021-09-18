
import random
from manager.character_manager import Character_manager


class Enemy_manager(Character_manager):
    def __init__(self, enemy):
        super().__init__(enemy)

        # id, name, level, max_hp, max_mp, attack, defence, u, v
        # self.__info_data = [
        #     [0, 'スライムベス', 1, 100, 100, 100, 100, 16, 64],
        #     [1, 'タイフーンドラゴン', 5, 500, 250, 300, 200, 16, 96],
        #     [2, 'カッキリカッカ', 5, 200, 150, 300, 200, 16, 128],
        #     [3, 'コバシ', 5, 600, 10, 100, 100, 16, 160],
        #     [4, 'オオバッシー', 5, 1000, 20, 300, 300, 16, 192],
        #     [5, 'マモホッパー', 5, 10, 10, 10, 10, 64, 96],
        #     [6, 'マドッコ', 5, 200, 500, 100, 100, 64, 128],
        #     [7, 'ナゴブラック', 5, 200, 100, 1000, 800, 64, 160],
        # ]
        self.__info_data = [
            [0, 000, 1, 100, 100, 100, 100, 16, 64],
            [1, 111, 5, 500, 250, 300, 200, 16, 96],
            [2, 222, 5, 200, 150, 300, 200, 16, 128],
            [3, 333, 5, 600, 10, 100, 100, 16, 160],
            [4, 444, 5, 1000, 20, 300, 300, 16, 192],
            [5, 555, 5, 10, 10, 10, 10, 64, 96],
            [6, 666, 5, 200, 500, 100, 100, 64, 128],
            [7, 777, 5, 200, 100, 1000, 800, 64, 160],
        ]

        self.__set_status(self.__select_enemy_id())

    def __select_enemy_id(self):
        return random.randint(0, len(self.__info_data)-1)

    def __set_status(self, _id):
        enemy = super().character
        print('_id', _id)
        enemy.id = self.__info_data[_id][0]
        enemy.name = self.__info_data[_id][1]
        enemy.level = self.__info_data[_id][2]

        enemy.u = self.__info_data[_id][7]
        enemy.v = self.__info_data[_id][8]

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