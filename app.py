from dungeon.floor import Floor
import pyxel
from dungeon.room.room import Room


class App:
    def __init__(self):
        pyxel.init(160, 120)
        # self.room = Room()
        self.floor = Floor()
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        # self.room.room_objects.terrain.draw()
        self.floor_terrain_draw()
        

    def floor_terrain_draw(self):
        print(len(self.floor.rooms))
        x = 0
        y = 0
        for i in range(len(self.floor.rooms)):
            self.floor.rooms[i].layers.terrain_layer.draw()

if __name__ == '__main__':
    app = App()