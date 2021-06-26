import pyxel
from dungeon.room import Room


class App:
    def __init__(self):
        pyxel.init(160, 120)
        room = Room()
        pyxel.run(self.update, self.draw)
        # print(room.terrain)

    def update(self):
        pass
        # room.generate_room_data()

    def draw(self):
        pass


if __name__ == '__main__':
    app = App()