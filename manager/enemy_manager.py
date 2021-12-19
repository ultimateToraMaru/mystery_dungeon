
import random
from manager.character_manager import Character_manager


class Enemy_manager(Character_manager):
    def __init__(self, enemy):
        super().__init__(enemy)

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
        # id, name, level, max_hp, max_mp, attack, defence, exp, u, v
        self.__info_data = [
            ['0', 'スライムベス', '5', '100', '100', '100', '100', '10', '16', '64'],
            ['1', 'タイフーンドラゴン', '5', '500', '250', '300', '200', '15', '16', '96'],
            ['2', 'カッキリ閣下', '5', '200', '150', '300', '200', '20', '16', '128'],
            ['3', 'コバシ', '5', '600', '10', '100', '100', '25', '16', '160'],
            ['4', 'オオバッシー', '5', '1000', '20', '300', '300', '30', '16', '192'],
            ['5', 'マモホッパー', '5', '10', '10', '10', '10', '35', '64', '96'],
            ['6', 'マドッコ', '5', '200', '500', '100', '100', '40', '64', '128'],
            ['7', 'ナゴブラック', '5', '200', '100', '1000', '800', '45', '64', '160'],
        ]

        self.__set_status(self.__select_enemy_id())

    def __select_enemy_id(self):
        return random.randint(0, len(self.__info_data)-1)

    def __set_status(self, _id):
        enemy = super().character
        # print('_id', _id)
        enemy.id = int(self.__info_data[_id][0])
        enemy.name = self.__info_data[_id][1]
        enemy.level = int(self.__info_data[_id][2])
        enemy.hp = int(self.__info_data[_id][3])
        enemy.max_hp = int(self.__info_data[_id][3])
        enemy.mp = int(self.__info_data[_id][4])
        enemy.max_mp = int(self.__info_data[_id][4])
        enemy.attack = int(self.__info_data[_id][5])
        enemy.defense = int(self.__info_data[_id][6])
        enemy.exp = int(self.__info_data[_id][7])

        enemy.u = int(self.__info_data[_id][8])
        enemy.v = int(self.__info_data[_id][9])

    def get_input(self):
        super().character.action = 'move'
        target_address_and_pos = super().character.get_target_address_and_pos()
        self_address_and_pos = super().character.get_self_address_and_pos()
        target_pos = super().character.target.position
        self_pos = super().character.position

        willingness = random.randint(0, 100)  # やる気

        if (self.__target_room_together()):
            if (target_pos[0] == self_pos[0]+1 and super().character.direction == 'right' or
                target_pos[0] == self_pos[0]-1 and super().character.direction == 'left' or
                target_pos[1] == self_pos[1]+1 and super().character.direction == 'down' or
                target_pos[1] == self_pos[1]-1 and super().character.direction == 'up' or
                target_pos[0] == self_pos[0]-1 and target_pos[1] == self_pos[1]-1 and super().character.direction == 'up_left' or
                target_pos[0] == self_pos[0]+1 and target_pos[1] == self_pos[1]-1 and super().character.direction == 'up_right' or
                target_pos[0] == self_pos[0]-1 and target_pos[1] == self_pos[1]+1 and super().character.direction == 'down_left' or
                target_pos[0] == self_pos[0]+1 and target_pos[1] == self_pos[1]+1 and super().character.direction == 'down_right'):

                super().character.action = 'attack'
                # return

        # やる気があるときの行動
        if (willingness > 1):
            if (target_address_and_pos[0] > self_address_and_pos[0]):
                super().character.direction = 'right'
            if (target_address_and_pos[0] < self_address_and_pos[0]):
                super().character.direction = 'left'
            if (target_address_and_pos[1] > self_address_and_pos[1]):
                super().character.direction = 'down'
            if (target_address_and_pos[1] < self_address_and_pos[1]):
                super().character.direction = 'up'

            # ななめ
            if (target_address_and_pos[0] < self_address_and_pos[0]
                and target_address_and_pos[1] < self_address_and_pos[1]):
                super().character.direction = 'up_left'

            if (target_address_and_pos[0] > self_address_and_pos[0]
                and target_address_and_pos[1] < self_address_and_pos[1]):
                super().character.direction = 'up_right'

            if (target_address_and_pos[0] < self_address_and_pos[0]
                and target_address_and_pos[1] > self_address_and_pos[1]):
                super().character.direction = 'down_left'

            if (target_address_and_pos[0] > self_address_and_pos[0]
                and target_address_and_pos[1] > self_address_and_pos[1]):
                super().character.direction = 'down_right'
        else :
            com = ['right', 'left', 'down', 'up']
            r = random.randint(0, 3)
            super().character.direction = com[r]

        # if (self.__target_room_together()):
        #     if (target_pos[0] == self_pos[0]+1 or
        #         target_pos[0] == self_pos[0]-1 or
        #         target_pos[1] == self_pos[1]+1 or
        #         target_pos[1] == self_pos[1]-1):

        #         super().character.action = 'attack'
                # return

    def __target_room_together(self):
        return super().character.target.room_address[0] == super().character.room_address[0] and super().character.target.room_address[1] == super().character.room_address[1]