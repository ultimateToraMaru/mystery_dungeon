from manager.character_manager import Character_manager


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

    def move_instruction(self, direction):
        self.__player.set_direction(direction)
        if (self.is_can_move_character(self.__player, direction)):
            self.__player.move(direction)

    def attack_instruction(self, targer_room_address_and_position, ):
        # targer_room_address_and_position = self.get_forward_mass(self.__player, self.__player.direction)
        print(targer_room_address_and_position)
        target_room_address = [targer_room_address_and_position[0], targer_room_address_and_position[1]]
        target_position = [targer_room_address_and_position[2], targer_room_address_and_position[3]]
        # self.__rooms[target_room_address[0]][target_room_address[1]].layers.enemy_layer.set_damage(target_position[0], target_position[1], self.__player.attack)