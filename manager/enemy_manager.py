
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
        # print('_id', _id)
        enemy.id = self.__info_data[_id][0]
        enemy.name = self.__info_data[_id][1]
        enemy.level = self.__info_data[_id][2]
        enemy.hp = self.__info_data[_id][3]
        enemy.max_hp = self.__info_data[_id][3]
        enemy.mp = self.__info_data[_id][4]
        enemy.max_mp = self.__info_data[_id][4]
        enemy.attack = self.__info_data[_id][5]
        enemy.defense = self.__info_data[_id][6]

        enemy.u = self.__info_data[_id][7]
        enemy.v = self.__info_data[_id][8]

    def get_input(self):
        super().character.action = 'move'
        target_address_and_pos = super().character.get_target_address_and_pos()
        self_address_and_pos = super().character.get_self_address_and_pos()
        target_pos = super().character.target.position
        self_pos = super().character.position

        if (self.__target_room_together()):
            if (target_pos[0] == self_pos[0]+1 or
                target_pos[0] == self_pos[0]-1 or
                target_pos[1] == self_pos[1]+1 or
                target_pos[1] == self_pos[1]-1):

                super().character.action = 'attack'
                return

        willingness = random.randint(0, 100)  # やる気
        if (willingness > 1):
            if (target_address_and_pos[0] > self_address_and_pos[0]):
                super().character.direction = 'right'
            if (target_address_and_pos[0] < self_address_and_pos[0]):
                super().character.direction = 'left'
            if (target_address_and_pos[1] > self_address_and_pos[1]):
                super().character.direction = 'down'
            if (target_address_and_pos[1] < self_address_and_pos[1]):
                super().character.direction = 'up'
        else :
            com = ['right', 'left', 'down', 'up']
            r = random.randint(0, 3)
            super().character.direction = com[r]


    def __target_room_together(self):
        return super().character.target.room_address[0] == super().character.room_address[0] and super().character.target.room_address[1] == super().character.room_address[1]