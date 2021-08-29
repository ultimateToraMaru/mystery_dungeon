from dungeon.const.size import Size

# TODO: 0829HEAD floorを管理するfloor_managerを実装中
class Floor_manager():
    def __init__(self, floor) -> None:
        self.__floor = floor

    # キャラクターが行こうとしているところが、移動できるところかどうか(部屋の隅、敵じゃないか？)
    def is_can_move_character(self, character, direction):

        if (direction == 'right'):
            character_at_end_of_the_room = character.position[0] == Size.MAX_MASS_IN_ROOM_ONE_SIDE-1
            character_at_end_of_the_floor = character.room_address[0]+1 == Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE
            if (character_at_end_of_the_room):
                if (character_at_end_of_the_floor):
                    return False
                next_room_mass_is_noneobj = self.floor.rooms[character.room_address[0]+1][character.room_address[1]].is_noneobj(Size.MAX_MASS_IN_ROOM_ONE_SIDE-1, character.position[1])
                this_room = self.floor.rooms[character.room_address[0]][character.room_address[1]]
                # next_room = self.__rooms[character.room_address[0]+1][character.room_address[1]]
                next_room_position = [character.room_address[0]+1, character.room_address[1]]
                in_room_position = [-1, character.position[1]]
            else :
                forward_mass_is_noneobj = self.__rooms[character.room_address[0]][character.room_address[1]].is_noneobj(character.position[0]+1, character.position[1])
                forward_is_not_corner_of_room = character.position[0]+1 < Size.MAX_MASS_IN_ROOM_ONE_SIDE

        elif (direction == 'left'):
            character_at_end_of_the_room = character.position[0] == 0
            character_at_end_of_the_floor = character.room_address[0]-1 == -1
            if (character_at_end_of_the_room):
                next_room_mass_is_noneobj = self.__rooms[character.room_address[0]-1][character.room_address[1]].is_noneobj(Size.MAX_MASS_IN_ROOM_ONE_SIDE-1, character.position[1])
                this_room = self.__rooms[character.room_address[0]][character.room_address[1]]
                # next_room = self.__rooms[character.room_address[0]-1][character.room_address[1]]
                next_room_position = [character.room_address[0]-1, character.room_address[1]]
                in_room_position = [Size.MAX_MASS_IN_ROOM_ONE_SIDE, character.position[1]]
            else :
                forward_mass_is_noneobj = self.__rooms[character.room_address[0]][character.room_address[1]].is_noneobj(character.position[0]-1, character.position[1])
                forward_is_not_corner_of_room = character.position[0]-1 > -1

        elif (direction == 'up'):
            character_at_end_of_the_room = character.position[1] == 0
            character_at_end_of_the_floor = character.room_address[1]-1 == -1
            if (character_at_end_of_the_room):
                next_room_mass_is_noneobj = self.__rooms[character.room_address[0]][character.room_address[1]-1].is_noneobj(character.position[0], Size.MAX_MASS_IN_ROOM_ONE_SIDE-1)
                this_room = self.__rooms[character.room_address[0]][character.room_address[1]]
                # next_room = self.__rooms[character.room_address[0]][character.room_address[1]-1]
                next_room_position = [character.room_address[0], character.room_address[1]-1]
                in_room_position = [character.position[0], Size.MAX_MASS_IN_ROOM_ONE_SIDE]
            else :
                forward_mass_is_noneobj = self.__rooms[character.room_address[0]][character.room_address[1]].is_noneobj(character.position[0], character.position[1]-1)
                forward_is_not_corner_of_room = character.position[1]-1 > -1

        elif (direction == 'down'):
            character_at_end_of_the_room = character.position[1] == Size.MAX_MASS_IN_ROOM_ONE_SIDE-1
            character_at_end_of_the_floor = character.room_address[1]+1 == Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE
            if (character_at_end_of_the_room):
                if (character_at_end_of_the_floor):
                    return False
                next_room_mass_is_noneobj = self.__rooms[character.room_address[0]][character.room_address[1]+1].is_noneobj(character.position[0], character.position[1]-1)
                this_room = self.__rooms[character.room_address[0]][character.room_address[1]]
                # next_room = self.__rooms[character.room_address[0]][character.room_address[1]+1]
                next_room_position = [character.room_address[0], character.room_address[1]+1]
                in_room_position = [character.position[0], -1]
            else :
                forward_mass_is_noneobj = self.__rooms[character.room_address[0]][character.room_address[1]].is_noneobj(character.position[0], character.position[1]+1)
                forward_is_not_corner_of_room = character.position[1]+1 < Size.MAX_MASS_IN_ROOM_ONE_SIDE

        # プレイヤーが部屋の端にいるとき
        if (character_at_end_of_the_room):
            # その部屋がブロックの端のとき、終了(世界の果てには移動できない)
            if (character_at_end_of_the_floor):
                return False
            # 次の部屋のマスが床のとき(障害物がないとき)
            if (next_room_mass_is_noneobj):
                # print('次の部屋へ')
                # キャラクターの移動に伴って部屋を掃除する(08/12, いつか、cleanメソッドをlayerクラスに作る)
                # cleanがうまくいっていない!!!!!
                # print('クリーンした部屋:', this_room.room_address)
                this_room.layers.enemy_layer.clean()
                this_room.layers.player_layer.clean()
                # キャラクターを次の部屋に移す(ルームアドレスを更新)
                character.room_address = next_room_position
                # キャラクターの部屋内のポジションを更新
                character.position = in_room_position

                return True
            else:
                # print('次の部屋の入り口に障害物があって進めません')
                return False

        # キャラクターが部屋の中を移動するとき
        else :
            return (forward_is_not_corner_of_room and forward_mass_is_noneobj)

    def get_forward_mass(self, character, direction):
        pass

    def get_player_room_arounds(self):
        pass