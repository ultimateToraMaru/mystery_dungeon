from tools.display import Display
from dungeon.room.object_layers.objects.character import Character
from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.const.color import Color
from dungeon.const.size import Size
from dungeon.room.object_layers.objects.obj import Obj
import pyxel

class Player(Character):
    def __init__(self, color, room_address, position):
        super().__init__(color, room_address, position)

        # TODO: 満腹度
        self.__satiation = 100

    @property
    def satiation(self):
        pass

    @satiation.getter
    def satiation(self):
        return self.__satiation

    @satiation.setter
    def satiation(self, satiation):
        self.__satiation = satiation

    def create(self, x, y, size):
        super().create(x, y, u=16, v=32, size=size)

    def set_status(self, name, level, hp, max_hp, mp, max_mp, attack, defense, exp, pocket):
        self.name = name
        self.level = level
        self.hp = hp
        self.max_hp = max_hp
        self.mp = mp
        self.max_mp= max_mp
        self.attack = attack
        self.defense = defense
        self.exp = exp
        self.pocket = pocket

        # Display.show_status(self.level, self.hp, self.max_hp, self.mp, self.max_mp, self.attack, self.defense)