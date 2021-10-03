from dungeon.const.size import Size
from dungeon.room.object_layers.objects.obj import Obj
import pyxel
import time


class Character(Obj):
    def __init__(self, color, room_address, position, name='hoge', level=1, max_hp=1000, max_mp=100, attack=100, defence=100):
        super().__init__(color, room_address, position)

        self.__tmp_position = [0, 0]    # 移動するオブジェクト(キャラクター)のみが持つ。
        self.__direction = 'down'
        self.__action = 'none'

        # ステータス
        self.__name = name
        self.__level = level
        self.__hp: int = max_hp
        self.__MAX_HP: int = max_hp
        self.__mp: int = max_mp
        self.__MAX_MP: int = max_mp
        self.__attack: int = attack
        self.__defense: int = defence

        self.__alive: bool = True

        self.__loop_index = 0 # 0~2の範囲で描画(create)されるたびに値が変わるindex. loop_animationで使用。
        # self.

    @property
    def tmp_position(self):
        pass

    @tmp_position.getter
    def tmp_position(self):
        return self.__tmp_position

    @tmp_position.setter
    def tmp_position(self, tmp_position):
        self.__tmp_position = tmp_position

    @property
    def direction(self):
        pass

    @direction.getter
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        self.__direction = direction

    @property
    def action(self):
        pass

    @action.getter
    def action(self):
        return self.__action

    @action.setter
    def action(self, action):
        self.__action = action

    @property
    def name(self):
        pass

    @name.getter
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def level(self):
        pass

    @level.getter
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        self.__level = level

    @property
    def hp(self):
        pass

    @hp.getter
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp):
        self.__hp = hp

    @property
    def MAX_HP(self):
        pass

    @MAX_HP.getter
    def MAX_HP(self):
        return self.__MAX_HP

    @MAX_HP.setter
    def MAX_HP(self, MAX_HP):
        self.__MAX_HP = MAX_HP

    @property
    def mp(self):
        pass

    @mp.getter
    def mp(self):
        return self.__mp

    @mp.setter
    def mp(self, mp):
        self.__mp = mp

    @property
    def MAX_MP(self):
        pass

    @MAX_MP.getter
    def MAX_MP(self):
        return self.__MAX_MP

    @MAX_MP.setter
    def MAX_MP(self, MAX_MP):
        self.__MAX_MP = MAX_MP

    @property
    def attack(self):
        pass

    @attack.getter
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, attack):
        self.__attack = attack

    @property
    def defense(self):
        pass

    @defense.getter
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, defense):
        self.__defense = defense

    @property
    def alive(self):
        pass

    @alive.getter
    def alive(self):
        return self.__alive

    @alive.setter
    def defense(self, alive):
        self.__alive = alive

    # TODO: create()内で呼べれている攻撃エフェクトの描画を、objectクラスを継承したattack_effect()を作成するべきだ
    def create(self, x, y, u, v):

        w = Size.MASS_WIDTH
        h = Size.MASS_HEIGHT

        if (Size.MASS_HEIGHT == 5):
            # pyxel.rect(x*w, y*h, w, h, Color.CLOUDBLUE)    # 仮の色を渡しておく
            pyxel.blt(x*w, y*h, img=1, u=0, v=0, w=5, h=5)    # 5*5
        elif (Size.MASS_HEIGHT == 10):
            pyxel.blt(x*w, y*h, img=1, u=8, v=0, w=10, h=10, colkey=0)    # 10*10
        elif (Size.MASS_HEIGHT == 16):
            if (self.__direction == 'right'):
                pyxel.blt(x*w, y*h, img=1, u=u+16, v=v, w=16, h=16, colkey=0)
            elif (self.__direction == 'left'):
                pyxel.blt(x*w, y*h, img=1, u=u-16, v=v, w=16, h=16, colkey=0)
            elif (self.__direction == 'up'):
                pyxel.blt(x*w, y*h, img=1, u=u, v=v-16, w=16, h=16, colkey=0)
            elif (self.__direction == 'down'):
                pyxel.blt(x*w, y*h, img=1, u=u, v=v, w=16, h=16, colkey=0)

            # if (self.__action == 'attack'):
            #     if (self.__direction == 'right'):
            #         if (self.__loop_index == 0):
            #             pyxel.blt(x*w+16, y*h, img=0, u=16, v=32, w=16, h=16, colkey=0)
            #         elif (self.__loop_index == 1):
            #             pyxel.blt(x*w+16, y*h, img=0, u=32, v=32, w=16, h=16, colkey=0)
            #         elif (self.__loop_index == 2):
            #             pyxel.blt(x*w+16, y*h, img=0, u=48, v=32, w=16, h=16, colkey=0)
            #     elif (self.__direction == 'left'):
            #         pyxel.blt(x*w-16, y*h, img=0, u=16, v=32, w=16, h=16, colkey=0)
            #     elif (self.__direction == 'up'):
            #         pyxel.blt(x*w, y*h-16, img=0, u=16, v=32, w=16, h=16, colkey=0)
            #     elif (self.__direction == 'down'):
            #         pyxel.blt(x*w, y*h+16, img=0, u=16, v=32, w=16, h=16, colkey=0)

            # elif (self.__direction == 'attack'):
            #     pyxel.blt(x*w, y*h, img=1, u=u+16, v=v+32, w=16, h=16, colkey=0)    # 10*10

    def set_direction(self, direction):
        self.__direction = direction

    def move(self, direction):
        # # print('move')
        self.__direction = direction
        if (self.__action == 'move'):
            if (direction == 'right'):
                self.position[0] = self.position[0]+1

            elif (direction == 'left'):
                self.position[0] = self.position[0]-1

            elif (direction == 'up'):
                self.position[1] = self.position[1]-1

            elif (direction == 'down'):
                self.position[1] = self.position[1]+1

    # def attack(self):
    #     return self.attack
    #     if (direction == 'right'):

    #     elif (direction == 'left'):

    #     elif (direction == 'up'):

    #     elif (direction == 'down'):

    def damage(self, damage_point):
        self.__hp = self.__hp - damage_point
        print(self.name, 'に', damage_point, 'のダメージ！')
        if (self.__hp <= 0):
            self.__destroy()

    def __destroy(self):
        print(self.name, 'は倒れた')
        self.__alive = False
    #     del self

    # def __del__(self):
    #     print('destractor')