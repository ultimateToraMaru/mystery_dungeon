from dungeon.const.size import Size
import copy


class Character_manager():
    def __init__(self, character):
        self.__character = character

    # floor_managerに移した
    # def __spawn(self):
    #     pass

    # floor_managerに移した
    # def set_position(self):
    #     pass

    @property
    def character(self):
        pass

    @character.getter
    def character(self):
        return self.__character

    @character.setter
    def character(self, character):
        self.__character = character

    def set_target(self):
        pass

    def get_want_to_move_room_address_and_position(self):
        # そのまま代入すると、参照渡しになってしまうため、deepcopy
        room_address =  copy.deepcopy(self.__character.room_address)
        position = copy.deepcopy(self.__character.position)

        # 移動
        if (self.__character.direction == 'right'):

            # 次の部屋に移動するとき
            if (position[0] == Size.MAX_MASS_IN_ROOM_ONE_SIDE-1):
                room_address[0] = room_address[0]+1
                position[0] = 0

            else :
                position[0] = position[0]+1

        elif (self.__character.direction == 'left'):

            # 次の部屋に移動するとき
            if (position[0] == 0):
                room_address[0] = room_address[0]-1
                position[0] = Size.MAX_MASS_IN_ROOM_ONE_SIDE-1

            else :
                position[0] = position[0]-1

        elif (self.__character.direction == 'up'):

            # 次の部屋に移動するとき
            if (position[1] == 0):
                room_address[1] = room_address[1]-1
                position[1] = Size.MAX_MASS_IN_ROOM_ONE_SIDE-1

            else :
                position[1] = position[1]-1

        elif (self.__character.direction == 'down'):

            # 次の部屋に移動するとき
            if (position[1] == Size.MAX_MASS_IN_ROOM_ONE_SIDE-1):
                room_address[1] = room_address[1]+1
                position[1] = 0

            else :
                position[1] = position[1]+1

        return room_address, position

    def set_position(self, room_address, position):
        self.__character.room_address = room_address
        self.__character.position = position

    # def move_instruction(self, direction, floor):
    #     self.__character.set_direction(direction)
    #     if (floor.is_can_move_character(self.__character, direction)):
    #         self.__character.move(direction)

    def attack_instruction(self, targer_room_address_and_position, ):
        # targer_room_address_and_position = self.get_forward_mass(self.__character, self.__character.direction)
        print(targer_room_address_and_position)
        target_room_address = [targer_room_address_and_position[0], targer_room_address_and_position[1]]
        target_position = [targer_room_address_and_position[2], targer_room_address_and_position[3]]
        # self.__rooms[target_room_address[0]][target_room_address[1]].layers.enemy_layer.set_damage(target_position[0], target_position[1], self.__character.attack)

    def print_status(self):
        print('room_address', self.__character.room_address)
        print('position', self.__character.position)

    def checkAlive(self):
        return self.__character.alive