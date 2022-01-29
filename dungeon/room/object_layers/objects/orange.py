from dungeon.const.color import Color
from dungeon.const.size import Size
from dungeon.room.object_layers.objects.food import Food
from dungeon.room.object_layers.objects.item import Item
from dungeon.room.object_layers.objects.obj import Obj
import pyxel
from tools.display import Display

class Orange(Food):
    def __init__(self, color=Color.WHITE):
        super().__init__(color)
        self.__recovery_point = 200
        self.__name = 'オレンジ'

    @property
    def recovery_point(self):
        pass

    @recovery_point.getter
    def recovery_point(self):
        return self.__recovery_point

    @recovery_point.setter
    def recovery_point(self, recovery_point):
        self.__recovery_point = recovery_point

    def create(self, x, y, size):
        w = size
        h = size

        if (size == 5):
            super().create(x, y, 16, 10, size)
        elif (size == 16):
            super().create(x, y, 16, 0, size)

    def eat(self, status):
        """
        回復ポイント分回復して、
        もし最大HPよりも多く回復してしまったら、最大HPを返す
        """
        hp: int = status.hp
        hp += self.__recovery_point

        status.hp = min(hp, status.max_hp)

        display = Display.get_instance()
        display.set_log([
            status.name
            + 'は、' + self.__name + 'を食べてHPを',
            str(self.__recovery_point)
            + 'ポイント回復した！'])

        return status
