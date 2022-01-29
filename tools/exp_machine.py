# 描画する部分を格納する配列を持つカメラ
import random
from dungeon.const.color import Color
from dungeon.room.object_layers.objects.player import Player
from dungeon.const.size import Size
from dungeon.room.room import Room
from dungeon.room.object_layers.objects.none_obj import None_obj
import time
import pyxel


class Exp_machine():
    def __init__(self):
        # self.__next_level_exp_base = random.randint(30, 100)  # 次のレベルまでに必要な経験値の基礎
        self.__necesarry_exp_list = self.__generate_necesarry_exp_list()

        self.__exps = 0

    def __generate_necesarry_exp_list(self):
        necesarry_exp_list = []
        for i in range(100):
            next_level_exp_base = random.randint(30, 100)  # 次のレベルまでに必要な経験値の基礎
            necesarry_exp_list.append(i*next_level_exp_base)

        return necesarry_exp_list

    def add_exp(self, exp, now_level):
        self.__exps += exp
        plus_status = []
        if (self.__necesarry_exp_list[now_level] <= self.__exps):
            plus_status = self.__level_up()

        else:
            plus_status = [0, 0, 0, 0, 0]

        return plus_status

    def __level_up(self):
        level = 1
        max_hp = random.randint(10, 50)
        max_mp = random.randint(10, 50)
        attack = random.randint(10, 50)
        defense = random.randint(10, 50)

        plus_status = [level, max_hp, max_mp, attack, defense]

        return plus_status
