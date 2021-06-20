
# floor内の一個一個の部屋を表すクラス
class Room:
    def __init__(self):
        self.__terrain = [[0] * 10 for i in range(10)]

    @property
    def terrain(self):
        pass

    @terrain.getter
    def terrain(self):
        return self.__terrain

    @terrain.setter
    def terrain(self, terrain):
        self.__terrain = terrain

room = Room()
print(room.terrain)
