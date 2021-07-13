from dungeon.room.object_layers.objects.obj import Obj

class Player(Obj):
    def __init__(self, color):
        super().__init__(color)