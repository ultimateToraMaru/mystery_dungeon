from dungeon.room.object_layers.objects.player import Player
from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.floor import Floor
import pyxel
from dungeon.room.room import Room


class App:
    def __init__(self):
        pyxel.init(255, 255, caption="mystery_dungeon", scale=2, fps=5)
        pyxel.load("my_resource.pyxres")
        self.floor = Floor()

        self.floor.spawn_player()

        # array = [[None_obj()]*2 for i in range(2)] 
        # for i in range(2):
        #     for j in range(2):
        #         array[i][j] = None_obj()

        # array = [[None_obj()]*2 for i in range(2)] 
        # すごいことが分かった。
        # あのfor文でinstance化すると*をした部分は
        # 同じinstanceがコピーされていた！！
        # 調べてみたらアドレスが一致した
        # array[0][0] = 
        # print(array)


        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        self.floor.terrain_draw()
        self.floor.player_move('right')
        self.floor.player_set_position()
        self.floor.player_draw()

if __name__ == '__main__':
    app = App()