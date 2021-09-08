from dungeon.room.object_layers.objects.steps import Steps
from dungeon.room.object_layers.objects.enemy import Enemy
from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.room.object_layers.objects.tile import Tile
import random
from dungeon.room.room import Room
from dungeon.const.size import Size

# TODO: 0829HEAD ____floorを管理するfloor_managerを実装中
class Floor_manager():
    def __init__(self, floor) -> None:
        self.__floor = floor
        self.__floor.rooms = self.__generate_rooms(self.__floor.room_numbers)
        self.__player_start_room_address = self.__select_start_room_address(self.__floor.rooms)

        self.__steps = self.__spawn_steps()

    @property
    def floor(self):
        pass

    @floor.getter
    def floor(self):
        return self.__floor

    @floor.setter
    def floor(self, floor):
        self.__floor = floor

    # キャラクターが行こうとしているところが、移動できるところかどうか(部屋の隅、敵じゃないか？)
    def is_can_move_character(self, character, direction):

        if (direction == 'right'):
            character_at_end_of_the_room = character.position[0] == Size.MAX_MASS_IN_ROOM_ONE_SIDE-1
            character_at_end_of_the_floor = character.room_address[0]+1 == Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE
            if (character_at_end_of_the_room):
                if (character_at_end_of_the_floor):
                    return False
                next_room_mass_is_noneobj = self.__floor.rooms[character.room_address[0]+1][character.room_address[1]].is_noneobj(Size.MAX_MASS_IN_ROOM_ONE_SIDE-1, character.position[1])
                this_room = self.__floor.rooms[character.room_address[0]][character.room_address[1]]
                # next_room = self.__rooms[character.room_address[0]+1][character.room_address[1]]
                next_room_position = [character.room_address[0]+1, character.room_address[1]]
                in_room_position = [-1, character.position[1]]
            else :
                forward_mass_is_noneobj = self.__floor.rooms[character.room_address[0]][character.room_address[1]].is_noneobj(character.position[0]+1, character.position[1])
                forward_is_not_corner_of_room = character.position[0]+1 < Size.MAX_MASS_IN_ROOM_ONE_SIDE

        elif (direction == 'left'):
            character_at_end_of_the_room = character.position[0] == 0
            character_at_end_of_the_floor = character.room_address[0]-1 == -1
            if (character_at_end_of_the_room):
                next_room_mass_is_noneobj = self.__floor.rooms[character.room_address[0]-1][character.room_address[1]].is_noneobj(Size.MAX_MASS_IN_ROOM_ONE_SIDE-1, character.position[1])
                this_room = self.__floor.rooms[character.room_address[0]][character.room_address[1]]
                # next_room = self.__rooms[character.room_address[0]-1][character.room_address[1]]
                next_room_position = [character.room_address[0]-1, character.room_address[1]]
                in_room_position = [Size.MAX_MASS_IN_ROOM_ONE_SIDE, character.position[1]]
            else :
                forward_mass_is_noneobj = self.__floor.rooms[character.room_address[0]][character.room_address[1]].is_noneobj(character.position[0]-1, character.position[1])
                forward_is_not_corner_of_room = character.position[0]-1 > -1

        elif (direction == 'up'):
            character_at_end_of_the_room = character.position[1] == 0
            character_at_end_of_the_floor = character.room_address[1]-1 == -1
            if (character_at_end_of_the_room):
                next_room_mass_is_noneobj = self.__floor.rooms[character.room_address[0]][character.room_address[1]-1].is_noneobj(character.position[0], Size.MAX_MASS_IN_ROOM_ONE_SIDE-1)
                this_room = self.__floor.rooms[character.room_address[0]][character.room_address[1]]
                # next_room = self.__rooms[character.room_address[0]][character.room_address[1]-1]
                next_room_position = [character.room_address[0], character.room_address[1]-1]
                in_room_position = [character.position[0], Size.MAX_MASS_IN_ROOM_ONE_SIDE]
            else :
                forward_mass_is_noneobj = self.__floor.rooms[character.room_address[0]][character.room_address[1]].is_noneobj(character.position[0], character.position[1]-1)
                forward_is_not_corner_of_room = character.position[1]-1 > -1

        elif (direction == 'down'):
            character_at_end_of_the_room = character.position[1] == Size.MAX_MASS_IN_ROOM_ONE_SIDE-1
            character_at_end_of_the_floor = character.room_address[1]+1 == Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE
            if (character_at_end_of_the_room):
                if (character_at_end_of_the_floor):
                    return False
                next_room_mass_is_noneobj = self.__floor.rooms[character.room_address[0]][character.room_address[1]+1].is_noneobj(character.position[0], character.position[1]-1)
                this_room = self.__floor.rooms[character.room_address[0]][character.room_address[1]]
                # next_room = self.__rooms[character.room_address[0]][character.room_address[1]+1]
                next_room_position = [character.room_address[0], character.room_address[1]+1]
                in_room_position = [character.position[0], -1]
            else :
                forward_mass_is_noneobj = self.__floor.rooms[character.room_address[0]][character.room_address[1]].is_noneobj(character.position[0], character.position[1]+1)
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

    # 座標を引数で与えて、そこが空いてるか(移動できる場所)どうかをture, falseで返す
    def is_can_move_neo(self, room_address, position):
        r_x = room_address[0]
        r_y = room_address[1]
        p_x = position[0]
        p_y = position[1]

        # pythonでは添え字にマイナスも指定できてしまい、indexErrorが発生しないため
        # マイナス値になったら、問答無用でFalseを返す
        if (r_x == -1 or r_y == -1):
            return False

        try:
            return (
                type(self.__floor.rooms[r_x][r_y].layers.terrain_layer.data[p_x][p_y]) == Tile and
                type(self.__floor.rooms[r_x][r_y].layers.player_layer.data[p_x][p_y]) == None_obj and
                type(self.__floor.rooms[r_x][r_y].layers.enemy_layer.data[p_x][p_y]) == None_obj
            )

        # listのIndexErrorが発生するroom_addressとpositionは、そもそも移動できない場所なので
        # try-catchでキャッチしてもらい、強制的にFalseを返す
        except IndexError as e:
            return False

    def get_forward_mass(self, character, direction):
        room_address = character.room_address
        position = character.position
        room_address_and_position = []

        if (direction == 'right'):
            # 前方マスが次の部屋だった時
            if (position[0]+1 == Size.MAX_MASS_IN_ROOM_ONE_SIDE):
                room_address_and_position = [room_address[0]+1, room_address[1], 0, position[1]]

                # 前方マスが世界の果てだった時
                if (room_address[0]+1 == Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE):
                    room_address_and_position = [-1, -1, -1, -1]
            else :
                room_address_and_position = [room_address[0], room_address[1], position[0]+1, position[1]]

        elif (direction == 'left'):
            # 前方マスが次の部屋だった時
            if (position[0]-1 == -1):
                room_address_and_position = [room_address[0]-1, room_address[1], 0, position[1]]

                # 前方マスが世界の果てだった時
                if (room_address[0]-1 == -1):
                    room_address_and_position = [-1, -1, -1, -1]
            else :
                room_address_and_position = [room_address[0], room_address[1], position[0]-1, position[1]]

        elif (direction == 'up'):
            # 前方マスが次の部屋だった時
            if (position[1]-1 == -1):
                room_address_and_position = [room_address[0], room_address[1]-1, position[0], 0]

                # 前方マスが世界の果てだった時
                if (room_address[1]-1 == -1):
                    room_address_and_position = [-1, -1, -1, -1]
            else :
                room_address_and_position = [room_address[0], room_address[1], position[0], position[1]-1]

        elif (direction == 'down'):
            # 前方マスが次の部屋だった時
            if (position[1]+1 == Size.MAX_MASS_IN_ROOM_ONE_SIDE):
                room_address_and_position = [room_address[0], room_address[1]+1, position[0], 0]

                # 前方マスが世界の果てだった時
                if (room_address[1]+1 == Size.MAX_MASS_IN_ROOM_ONE_SIDE):
                    room_address_and_position = [-1, -1, -1, -1]
            else :
                room_address_and_position = [room_address[0], room_address[1], position[0], position[1]+1]

        return room_address_and_position

    def get_player_room_arounds(self, player_room_address):
        if (Size.MASS_HEIGHT == 5 and Size.MASS_WIDTH == 5):
            player_rooms = self.__floor.rooms
            return player_rooms
        elif (Size.MASS_HEIGHT == 16 and Size.MASS_WIDTH == 16):
            player_room = self.__floor.rooms[player_room_address[0]][player_room_address[1]]
            return player_room

    def __generate_rooms(self, room_numbers):
        rooms = [[Room(_type='none', room_address=[-1, -1])] * Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE for i in range(Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE)]
        for r_x in range(Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE):
            for r_y in range(Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE):
                rooms[r_x][r_y] = Room(_type='none', room_address=[r_x, r_y])

                # フロアの端の部屋は行き止まりになる通路がない部屋を生成する
                # if (j == 0) :
                #     rooms[i][j] = Room('top_end', False)
                #     print('top')

                # elif (j == Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1) :
                #     rooms[i][j] = Room('bottom_end', False)

                # if (i == 0) :
                #     rooms[i][j] = Room('top_end', False)
                    # if (j == 0) :
                    #     rooms[i][j] = Room('top_left_corner', False)
                    # elif (j == Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1):
                    #     rooms[i][j] = Room('bottom_left_corner', False)
                    # else :
                    #     rooms[i][j] = Room('left_end', False)

                ################ xが4の部屋に横から移動しようとしたときに落ちる

                # elif (i == Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1) :
                #     rooms[i][j] = Room('bottom_end', False)
                #     if (j == 0) :
                #         rooms[i][j] = Room('top_right_corner', False)
                #     elif (j == Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1):
                #         rooms[i][j] = Room('bottom_right_corner', False)
                #     else :
                #         rooms[i][j] = Room('right_end', False)
                # else :
                #     rooms[i][j] = Room('none', False)

        # 部屋をランダムな場所に生成
        for not_use_index in range(room_numbers):
            r_x = random.randint(0, Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1)
            r_y = random.randint(0, Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1)

            rooms[r_x][r_y] = Room('normal', [r_x, r_y])

        # print('部屋の数', room_numbers)
        return rooms

    # スタートする部屋のアドレスをランダムで決める
    def __select_start_room_address(self, rooms):
        while (True):
            r_x = random.randint(0, Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1)
            r_y = random.randint(0, Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1)
            if (rooms[r_x][r_y]._type == 'normal'):
                print('スタート部屋のアドレス', r_x, r_y)
                return [r_x, r_y]

    def spawn_player(self):
        return self.__floor.rooms[self.__player_start_room_address[0]][self.__player_start_room_address[1]].generate_player(self.__player_start_room_address[0], self.__player_start_room_address[1])

    def spawn_enemys(self):
        enemys: list[Enemy] = []
        for r_x in range(len(self.__floor.rooms)):
            for r_y in range(len(self.__floor.rooms)):
                is_enemy_spawn = random.randint(0, 1)
                if (is_enemy_spawn):
                    enemys.extend(self.__floor.rooms[r_x][r_y].generate_enemys())

        return enemys

    def __spawn_steps(self):
        steps: Steps
        while (True):
            r_x = random.randint(0, Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1)
            r_y = random.randint(0, Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1)
            if (self.__floor.rooms[r_x][r_y]._type == 'normal'):
                steps = self.__floor.rooms[r_x][r_y].generate_steps(r_x, r_y)
                break

        print('階段のあるお部屋', steps.room_address)
        return steps

    def set_layer_player(self, player):
        self.__floor.rooms[player.room_address[0]][player.room_address[1]].layers.player_layer.set_position(player)

    def set_layer_enemy(self, enemy):
        self.__floor.rooms[enemy.room_address[0]][enemy.room_address[1]].layers.enemy_layer.set_position(enemy)

    # def enemy_set_position(self, enemys):
    #     for i in range(len(enemys)):
    #         self.__floor.rooms[enemys[i].room_address[0]][enemys[i].room_address[1]].layers.enemy_layer.set_position(enemys[i])

    def is_player_on_steps(self, player):
        if (player.room_address == self.__steps.room_address and
            player.position == self.__steps.position):
            return True

        return False

    def clean_floor(self):
        for i in range(len(self.__floor.rooms)):
            for j in range(len(self.__floor.rooms)):
                self.__floor.rooms[i][j].layers.enemy_layer.clean()
                self.__floor.rooms[i][j].layers.player_layer.clean()

    def get_player_room_arounds(self, player):
        if (Size.MASS_HEIGHT == 5 and Size.MASS_WIDTH == 5):
            player_rooms = self.__floor.rooms
            return player_rooms

        elif (Size.MASS_HEIGHT == 16 and Size.MASS_WIDTH == 16):
            player_room = self.__floor.rooms[player.room_address[0]][player.room_address[1]]
            return player_room

    def attack(self, target_room_address, target_position, character):
        self.__floor.rooms[target_room_address[0]][target_room_address[1]].layers.enemy_layer.set_damage(target_position[0], target_position[1], character.attack)
