from dungeon.floor import Floor
import pyxel
from dungeon.room.room import Room


class App:
    def __init__(self):
        pyxel.init(255, 255, caption="mystery_dungeon", scale=2, fps=5)
        pyxel.load("my_resource.pyxres")
        self.floor = Floor()
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        self.floor.rooms_terrain_draw()
        

if __name__ == '__main__':
    app = App()