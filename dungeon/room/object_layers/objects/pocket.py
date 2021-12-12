from dungeon.room.object_layers.objects.none_obj import None_obj


class Pocket():
    def __init__(self):
        self.__size = 5
        self.__contents = []

    def get_item(self, index):
        """
        index番目のアイテムを取得する
        """
        return self.__contents[index]

    def add_item(self, item):
        self.__contents.append(item)

    def show(self):
        return self.__contents