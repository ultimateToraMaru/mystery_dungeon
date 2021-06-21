
# floor内の一個一個の部屋を表すクラス
class Room:
    def __init__(self):
        print('a')
        self.__MAXMASS = 10
        self.__terrain = [[0] * self.__MAXMASS for i in range(self.__MAXMASS)]

        self.__terrain = self.generate_terrain(self.__MAXMASS, self.__terrain)
        print(self.__terrain)

    @property
    def terrain(self):
        pass

    @terrain.getter
    def terrain(self):
        return self.__terrain

    @terrain.setter
    def terrain(self, terrain):
        self.__terrain = terrain

    def generate_terrain(self, MAXMASS, terrain):
        for i in range(MAXMASS):
            terrain[0][i] = 1
            terrain[i][0] = 1
            terrain[MAXMASS-1][i] = 1
            terrain[i][MAXMASS-1] = 1

        return terrain