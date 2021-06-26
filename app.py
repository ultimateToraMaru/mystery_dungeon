from dungeon.color import Color
import pyxel
from dungeon.room import Room


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.room = Room()
        pyxel.run(self.update, self.draw)
        # print(room.terrain)

    def update(self):
        print('test')
        # room.generate_room_data()

    def draw(self):
        # for obj in room_data:
        #     obj.create()
        for i in range(10):
            for j in range(10):
                self.room.data[i][j].create(x=i, y=j)


if __name__ == '__main__':
    app = App()