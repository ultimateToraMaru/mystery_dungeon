class Set_room_objects:
    def __init__(self):
        self.__room_data
        pass

    # room_dataのプロパティ
    @property
    def room_data(self):
        pass

    @room_data.getter
    def color(self):
        return self.__room_data

    def create_objects(self, room_data):
        # for文でroom_dataを回して、objectのcreate()メソッドを読んでcreateしていく。
        # pyxelをインポートする必要があるのでは。このクラスには。

        x=0
        y=0
        for x in range(10):
            for y in range(10):
                print(room_data[x][y])
                room_data[x][y].create(x, y)