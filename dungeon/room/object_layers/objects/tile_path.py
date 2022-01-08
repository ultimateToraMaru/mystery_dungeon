from dungeon.const.color import Color
from dungeon.const.size import Size
from dungeon.room.object_layers.objects.tile import Tile
import pyxel
from dungeon.room.object_layers.objects.obj import Obj

class Tile_path(Tile):
    def __init__(self):
        super().__init__()