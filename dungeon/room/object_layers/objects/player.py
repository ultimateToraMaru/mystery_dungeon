from dungeon.room.object_layers.objects.obj import Obj

class Player(Obj):
    def __init__(self, color):
        super().__init__(color)
        self.__position = [0, 0]
    
    @property
    def position(self):
        pass

    @position.getter
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position