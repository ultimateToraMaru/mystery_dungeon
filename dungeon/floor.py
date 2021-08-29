from dungeon.room.object_layers.objects.character import Character
from dungeon.room.object_layers.objects.obj import Obj
from dungeon.const.color import Color
from dungeon.room.object_layers.objects.player import Player
from dungeon.room.object_layers.objects.enemy import Enemy
from dungeon.room.object_layers.objects.steps import Steps
from dungeon.room.object_layers.objects.tile import Tile
from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.const.size import Size
from dungeon.room.room import Room
import random

# dungeonのfloorを表す関数。複数のroomを持つ
class Floor:
    def __init__(self, _id):
        self.__id: int = _id
        # self.__rooms = [[Room('none')] * Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE for i in range(Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE)]    # 配列の枠組みを作っておく。下の初期化処理と併用して行う。絶対。
        # # 初期化処理。要素に別々のインスタンスを入れ込んでいく
        # for i in range(Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE):
        #     for j in range(Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE):
        #         self.__rooms[i][j] = Room('none')
        self.__room_numbers: int = random.randint(5, 10)
        self.__rooms: list[Room] = self.__generate_rooms(self.__room_numbers)

        # TODO: playerはdungeonクラスが持つべきでは？まあ、いつか直そう
        # TODO: playerとenemyのメソッドが多くなりすぎた。Character_controllerクラスを作って、Player_controllerとかにメソッドを移したほうがいいかも
        self.__player_start_room_address = self.__select_start_room_address(self.__rooms)
        self.__player: Player = self.__spawn_player(self.__player_start_room_address)
        print('プレイヤーのいるお部屋', self.__player.room_address, '座標 :', self.__player.position)
        # self.__steps_room_address = [0, 0]
        self.__steps: Steps = self.__spawn_steps()
        self.__enemys: list[Enemy] = self.__spawn_enemys()


    @property
    def rooms(self):
        pass

    @rooms.getter
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, rooms):
        self.__rooms = rooms

    # ランダムな場所に部屋を生成
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

    # プレイヤーを生み出す。フロア到達時に一階だけ実行される。
    def __spawn_player(self, player_start_room_address):
        # 下の関数の引数。配列をそのまま渡してもいいのでは？
        return self.__rooms[player_start_room_address[0]][player_start_room_address[1]].generate_player(player_start_room_address[0], player_start_room_address[1])

    # 階段を生み出す。フロア到達時に一階だけ実行される。
    def __spawn_steps(self):
        steps: Steps
        while (True):
            r_x = random.randint(0, Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1)
            r_y = random.randint(0, Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1)
            if (self.__rooms[r_x][r_y]._type == 'normal'):
                steps = self.__rooms[r_x][r_y].generate_steps(r_x, r_y)
                break

        print('階段のあるお部屋', steps.room_address)
        return steps

    # エネミーをランダムな部屋に生み出す。エネミーが生まれる部屋をランダムで決める。
    def __spawn_enemys(self):
        # 一個目の部屋の中心にエネミーを生成
        enemys: list[Enemy] = []
        # enemys.extend(self.__rooms[0][0].generate_enemys(0, 0))

        enemys: list[Enemy] = []
        for r_x in range(len(self.__rooms)):
            for r_y in range(len(self.__rooms)):
                is_enemy_spawn = random.randint(0, 1)
                if (is_enemy_spawn):
                    enemys.extend(self.__rooms[r_x][r_y].generate_enemys(r_x, r_y))

        self.enemy_set_target(enemys)
        return enemys

    # ??? プレイヤー自身の座標を受け取って、セットする
    def player_set_position(self):
        self.__rooms[self.__player.room_address[0]][self.__player.room_address[1]].layers.player_layer.set_position(self.__player)

    # ??? エネミー自身の座標を受け取って、セットする
    def enemy_set_position(self):
        for i in range(len(self.__enemys)):
            self.__rooms[self.__enemys[i].room_address[0]][self.__enemys[i].room_address[1]].layers.enemy_layer.set_position(self.__enemys[i])

    # プレイヤーが階段の上にいるか検査する
    def is_player_on_steps(self):
        # return self.__rooms[self.__steps.room_address[0]][self.__steps.room_address[1]].steps_check()
        if (self.__player.room_address == self.__steps.room_address and
            self.__player.position == self.__steps.position):
            return True

        return False

    # プレイヤーを動かす
    def player_move(self, direction):
        self.__player.set_direction(direction)
        if (self.is_can_move_character(self.__player, direction)):
            self.__player.move(direction)

    def player_attack(self):
        targer_room_address_and_position = self.get_forward_mass(self.__player, self.__player.direction)
        print(targer_room_address_and_position)
        target_room_address = [targer_room_address_and_position[0], targer_room_address_and_position[1]]
        target_position = [targer_room_address_and_position[2], targer_room_address_and_position[3]]
        self.__rooms[target_room_address[0]][target_room_address[1]].layers.enemy_layer.set_damage(target_position[0], target_position[1], self.__player.attack)

    # エネミーを動かす
    def enemy_move(self):
        for i in range(len(self.__enemys)):
            direction = self.__enemys[i].command()
            # 行き止まりに行こうとしたら、考えを改めてもらう
            while(not(self.is_can_move_character(self.__enemys[i], direction))):
                direction = self.__enemys[i].command()
                self.__enemys[i].set_direction(direction)
            if (self.is_can_move_character(self.__enemys[i], direction)):
                self.__enemys[i].move(direction)

    # ??? エネミーのターゲットの位置を報告してもらう
    # def __enemy_mind(self, enemy):
    #     return enemy.command()

    # キャラクターが行こうとしているところが、移動できるところかどうか(部屋の隅、敵じゃないか？)
    def is_can_move_character(self, character, direction):
        # 調査の結果、上の部屋に移動しようとしたときに移動先の座標がおかしい
        # print('部屋の番地:', character.room_address, ' 部屋内:', character.position, character)
        if (direction == 'right'):
            character_at_end_of_the_room = character.position[0] == Size.MAX_MASS_IN_ROOM_ONE_SIDE-1
            character_at_end_of_the_floor = character.room_address[0]+1 == Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE
            if (character_at_end_of_the_room):
                if (character_at_end_of_the_floor):
                    return False
                next_room_mass_is_noneobj = self.__rooms[character.room_address[0]+1][character.room_address[1]].is_noneobj(Size.MAX_MASS_IN_ROOM_ONE_SIDE-1, character.position[1])
                this_room = self.__rooms[character.room_address[0]][character.room_address[1]]
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


    def get_player_room_arounds(self):
        if (Size.MASS_HEIGHT == 5 and Size.MASS_WIDTH == 5):
            player_rooms = self.__rooms
            return player_rooms
        elif (Size.MASS_HEIGHT == 16 and Size.MASS_WIDTH == 16):
            player_room = self.__rooms[self.__player.room_address[0]][self.__player.room_address[1]]
            return player_room

        # room_position = [   [-1, -1], [-1, 0], [-1, +1],
        #                     [0, -1], [0, 0], [0, +1],
        #                     [+1, -1], [+1, 0], [+1, +1],
        #                 ]
        # player_around_rooms = []
        # for pos in room_position :
        #     player_around_rooms.append(self.__rooms[self.__player_room_position[0]+pos[0]][self.__player_room_position[1]+pos[1]])


    # ??? エネミーにターゲットをセットする
    def enemy_set_target(self, enemys):
        for i in range(len(enemys)):
            enemys[i].target = self.__player



    # def player_get_command(self):
    #     self.__player.command()

    # def enemy_get_command(self):
    #     for i in range(len(self.__enemys)):
    #         self.__enemys[i].command()