from dungeon.room.object_layers.empty_layer import Empty_layer
from dungeon.room.object_layers.objects.none_obj import None_obj
import math
from dungeon.const.size import Size
import random
from dungeon.room.object_layers.objects.tile import Tile
from dungeon.room.object_layers.objects.wall import Wall
from dungeon.const.color import Color

# 階段を表すクラス。地形データ__dataにWallやTile, Rockが入る
class Steps_layer(Empty_layer):
    def __init__(self):
        super().__init__()
