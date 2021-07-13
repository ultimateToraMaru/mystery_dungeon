from dungeon.floor import Floor
import pyxel
from dungeon.room.room import Room


class App:
    def __init__(self):
        pyxel.init(255, 255, caption="mystery_dungeon", scale=2, fps=5)
        self.floor = Floor()
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        self.floor.rooms_terrain_draw()
        

    # def floor_terrain_draw(self):
    #     # print(len(self.floor.rooms))
    #     for i in range(len(self.floor.rooms)):
    #         for j in range(len(self.floor.rooms)):
    #             self.floor.rooms[i][j].layers.terrain_layer.draw(i*10, j*10)

if __name__ == '__main__':
    app = App()