import random
from dungeon.display import Display
from dungeon.room.object_layers.objects.character import Character
from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.const.color import Color
from dungeon.const.size import Size
from dungeon.room.object_layers.objects.obj import Obj
import pyxel

class Enemy(Character):
    def __init__(self, color, room_address, position):
        super().__init__(color, room_address, position)

        self.__u = 16
        self.__v = 64
        # Display.show_status(self.level, self.hp, self.MAX_HP, self.mp, self.MAX_MP, self.attack, self.defense)
        self.__target = None_obj()

    @property
    def v(self):
        pass

    @v.getter
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        self.__v = v

    @property
    def u(self):
        pass

    @u.getter
    def u(self):
        return self.__u

    @u.setter
    def u(self, u):
        self.__u = u

    @property
    def target(self):
        pass

    @target.getter
    def target(self):
        return self.__target

    @target.setter
    def target(self, target):
        self.__target = target

    def create(self, x, y):
        super().create(x, y, u=self.__u, v=self.__v)

    def mind(self):
        print('ターゲットは部屋番号', self.__target.room_address,'の', self.__target.position, 'にいます！')


    def get_target_address_and_pos(self):
        target_address_and_pos: list[int] = [0, 0]
        target_address_and_pos[0] = self.__target.room_address[0] + self.__target.position[0]
        target_address_and_pos[1] = self.__target.room_address[1] + self.__target.position[1]

        return target_address_and_pos


    def get_self_address_and_pos(self):
        self_address_and_pos: list[int] = [0, 0]
        self_address_and_pos[0] = self.room_address[0] + self.position[0]
        self_address_and_pos[1] = self.room_address[1] + self.position[1]

        return self_address_and_pos

    # def command(self):
        # direction = 'down'
        # super().action = 'none'
        # target_address_and_pos = self.__get_target_address_and_pos()
        # self_address_and_pos = self.__get_self_address_and_pos()

        # if (target_address_and_pos[0] == self_address_and_pos[0]+1 or
        #     target_address_and_pos[0] == self_address_and_pos[0]-1 or
        #     target_address_and_pos[1] == self_address_and_pos[1]+1 or
        #     target_address_and_pos[1] == self_address_and_pos[1]-1):
        #     super().action = 'attack'

        # willingness = random.randint(0, 10)  # やる気
        # if (willingness > 3):
        #     if (target_address_and_pos[0] > self_address_and_pos[0]):
        #         super().direction = 'right'
        #     if (target_address_and_pos[0] < self_address_and_pos[0]):
        #         super().direction = 'left'
        #     if (target_address_and_pos[1] > self_address_and_pos[1]):
        #         super().direction = 'down'
        #     if (target_address_and_pos[1] < self_address_and_pos[1]):
        #         super().direction = 'up'
        #     # else :
        #     #     com = ['right', 'left', 'down', 'up']
        #     #     r = random.randint(0, 3)
        #     #     direction = com[r]
        # else :
        #     com = ['right', 'left', 'down', 'up']
        #     r = random.randint(0, 3)
        #     super().direction = com[r]

        # return super().direction