from dungeon.display import Display
from dungeon.room.object_layers.empty_layer import Empty_layer
from dungeon.room.object_layers.objects.enemy import Enemy
from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.room.object_layers.objects.player import Player
import math
from dungeon.const.size import Size
import random
from dungeon.room.object_layers.objects.tile import Tile
from dungeon.room.object_layers.objects.wall import Wall
from dungeon.const.color import Color

# 地形を表すクラス。地形データ__dataにWallやTile, Rockが入る
class Enemy_layer(Empty_layer):
    def __init__(self):
        super().__init__()

    def set_damage(self, p_x, p_y, damage_point, attacker_name):
        if (type(super().data[p_x][p_y]) == Enemy):
            return super().data[p_x][p_y].damage(damage_point, attacker_name)
        else :
            return -1
