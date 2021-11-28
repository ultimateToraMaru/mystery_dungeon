from dungeon.display import Display
from dungeon.room.object_layers.empty_layer import Empty_layer
from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.room.object_layers.objects.player import Player
import math
from dungeon.const.size import Size
import random
from dungeon.room.object_layers.objects.tile import Tile
from dungeon.room.object_layers.objects.wall import Wall
from dungeon.const.color import Color

# 地形を表すクラス。地形データ__dataにWallやTile, Rockが入る
class Player_layer(Empty_layer):
    def __init__(self):
        super().__init__()

    def set_damage(self, p_x, p_y, damage_point, attacker_name):
        if (type(super().data[p_x][p_y]) == Player):
            super().data[p_x][p_y].damage(damage_point, attacker_name)
        else :
            display = Display.get_instance()
            display.show_fool_battle_message(attacker_name)

    def get_player_position(self):
        player_position = []
        for p_x in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
            for p_y in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
                if (type(super().data[p_x][p_y]) == Player):
                    player_position = [p_x, p_y]

        return player_position
