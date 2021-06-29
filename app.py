import pyxel
from dungeon.room.room import Room


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.room = Room()
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        self.room.room_objects.terrain.draw()


if __name__ == '__main__':
    app = App()