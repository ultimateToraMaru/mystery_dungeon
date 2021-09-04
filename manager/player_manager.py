from dungeon.const.size import Size
from manager.character_manager import Character_manager
import copy


class Player_manager():
    def __init__(self, player):
        self.__player = player

    # floor_managerに移した
    # def __spawn(self):
    #     pass

    # floor_managerに移した
    # def set_position(self):
    #     pass

    @property
    def player(self):
        pass

    @player.getter
    def player(self):
        return self.__player

    @player.setter
    def player(self, player):
        self.__player = player

    def set_target(self):
        pass

    def get_want_to_move_room_address_and_position(self, direction):
        # そのまま代入すると、参照渡し担ってしまうため、deepcopy
        room_address =  copy.deepcopy(self.__player.room_address)
        position = copy.deepcopy(self.__player.position)

        if (direction == 'right'):

            if (position[0] == Size.MAX_MASS_IN_ROOM_ONE_SIDE-1):
                room_address[0] = room_address[0] + 1
                position[0] = 0

            else :
                position[0] = position[0] + 1

            return room_address, position

    def set_position(self, room_address, position):
        self.__player.room_address = room_address
        self.__player.position = position

    # def move_instruction(self, direction, floor):
    #     self.__player.set_direction(direction)
    #     if (floor.is_can_move_character(self.__player, direction)):
    #         self.__player.move(direction)

    def attack_instruction(self, targer_room_address_and_position, ):
        # targer_room_address_and_position = self.get_forward_mass(self.__player, self.__player.direction)
        print(targer_room_address_and_position)
        target_room_address = [targer_room_address_and_position[0], targer_room_address_and_position[1]]
        target_position = [targer_room_address_and_position[2], targer_room_address_and_position[3]]
        # self.__rooms[target_room_address[0]][target_room_address[1]].layers.enemy_layer.set_damage(target_position[0], target_position[1], self.__player.attack)

    def print_status(self):
        print('room_address', self.__player.room_address)
        print('position', self.__player.position)