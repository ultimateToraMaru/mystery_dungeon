from dungeon.room.object_layers.objects.tile import Tile
from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.const.size import Size
from dungeon.room.room import Room
import random

# dungeonのfloorを表す関数。複数のroomを持つ
class Floor:
    def __init__(self):
        self.__rooms = [[Room('none', False)] * Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE for i in range(Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE)]
        for i in range(Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE):
            for j in range(Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE):
                self.__rooms[i][j] = Room('none', False)

        self.__player_room_position = [0,0]
        self.__rooms = self.generate()
        self.__player = None_obj()

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
    def generate(self):
        r = random.randint(2, 5)    # rの範囲:2~5。お部屋の数。
        rooms = [[Room('none', False)] * Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE for i in range(Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE)]
        for i in range(Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE):
            for j in range(Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE):
                rooms[i][j] = Room('none', False)
        print('部屋の数', r)

        r_select_start_room = random.randint(0, r-1)    # startする部屋をランダムで選ぶ。上からr番目みたいな感じ。
        for i in range(r):
            r_x = random.randint(0, Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1) 
            r_y = random.randint(0, Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1) 
            # print(r_x, r_y)
            # print('i', i, 'r_start', r_select_start_room)
            if (i == r_select_start_room):
                # print('start_room:', r_x, r_y)
                # room = Room('normal', True)
                print('プレイヤーがいる部屋の座標', r_x, r_y)
                rooms[r_x][r_y] = Room('normal', True)
                self.__player_room_position = [r_x, r_y]
            else :
                # non_room = Room('normal', False)
                # print('プレイヤーがいない部屋', non_room)
                rooms[r_x][r_y] = Room('normal', False)
        
        return rooms

    # 部屋の地形データを読み取り、オブジェクトにdrawの指示を出す
    def terrain_draw(self):
        x = 0
        y = 0
        for i in range(len(self.__rooms)):
            for j in range(len(self.__rooms)):
                x = i*Size.MAX_MASS_IN_ROOM_ONE_SIDE
                y = j*Size.MAX_MASS_IN_ROOM_ONE_SIDE
                self.__rooms[i][j].layers.terrain_layer.draw(x, y)

    def player_draw(self):
        x = 0
        y = 0
        for i in range(len(self.__rooms)):
            for j in range(len(self.__rooms)):
                x = i*Size.MAX_MASS_IN_ROOM_ONE_SIDE
                y = j*Size.MAX_MASS_IN_ROOM_ONE_SIDE
                self.__rooms[i][j].layers.player_layer.draw(x, y)
        
        # print(self.__rooms)
                
    # プレイヤーを生み出す。フロア到達時に一階だけ実行される。
    def spawn_player(self):
        print('プレイヤーのいるお部屋', self.__player_room_position[0], self.__player_room_position[1],  self.__rooms[self.__player_room_position[0]][self.__player_room_position[1]])
        player = self.__rooms[self.__player_room_position[0]][self.__player_room_position[1]].layers.player_layer.set_start_position()
        self.__player = player

    # プレイヤー自身の座標を受け取って、セットする
    def player_set_position(self):
        self.__rooms[self.__player_room_position[0]][self.__player_room_position[1]].layers.player_layer.set_position()

    # プレイヤーを動かす
    def player_move(self, direction):
        if (self.is_can_move(direction)):
            self.__player.move(direction)

    
    # プレイヤーの行こうとしているところが、移動できるところかどうか(部屋の隅、敵じゃないか？)
    def is_can_move(self, direction):
        print('部屋の番地:', self.__player_room_position, ' 部屋内:', self.__player.position[0], self.__player.position[1])
        if (direction == 'right'):

            player_at_end_of_the_room = self.__player.position[0] == Size.MAX_MASS_IN_ROOM_ONE_SIDE-1
            player_at_end_of_the_floor = self.__player_room_position[0]+1 == Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE
            if (player_at_end_of_the_room):
                next_room_mass = type(self.__rooms[self.__player_room_position[0]+1][self.__player_room_position[1]].layers.terrain_layer.data[Size.MAX_MASS_IN_ROOM_ONE_SIDE-1][self.__player.position[1]])
                this_room = self.__rooms[self.__player_room_position[0]][self.__player_room_position[1]]
                next_room = self.__rooms[self.__player_room_position[0]+1][self.__player_room_position[1]]
                next_room_position = [self.__player_room_position[0]+1, self.__player_room_position[1]]
                in_room_position = [-1, self.__player.position[1]]
            else :
                forward_mass = type(self.__rooms[self.__player_room_position[0]][self.__player_room_position[1]].layers.terrain_layer.data[self.__player.position[0]+1][self.__player.position[1]])
                forward_is_not_corner_of_room = self.__player.position[0]+1 < Size.MAX_MASS_IN_ROOM_ONE_SIDE
        
        # elif (direction == 'left'):
        #     # ブロックの端ではそれ以降移動できないようにする
        #     if (self.__player.position[0] == 0 and self.__player_room_position[0]-1 == -1):
        #         return False

        #     forward_mass = type(self.__rooms[self.__player_room_position[0]][self.__player_room_position[1]].layers.terrain_layer.data[self.__player.position[0]-1][self.__player.position[1]])
        #     forward_is_not_corner_of_room = self.__player.position[0]-1 > -1
        #     if (self.__player.position[0]-1 == -1):
        #         next_room = type(self.__rooms[self.__player_room_position[0]-1][self.__player_room_position[1]].layers.terrain_layer.data[Size.MAX_MASS_IN_ROOM_ONE_SIDE-1][self.__player.position[1]])
        #         if (next_room == Tile):
        #             # プレイヤーの移動に伴って、部屋を掃除したり、次の部屋にプレイヤーを移したり
        #             self.__rooms[self.__player_room_position[0]][self.__player_room_position[1]].layers.player_layer.clean()
        #             self.__rooms[self.__player_room_position[0]-1][self.__player_room_position[1]].layers.player_layer.player = self.__player

        #             # プレイヤーの移動。ポジションもろもろ
        #             self.__player_room_position = [self.__player_room_position[0]-1, self.__player_room_position[1]]
        #             self.__player.position = [Size.MAX_MASS_IN_ROOM_ONE_SIDE-1, self.__player.position[1]]
            
        
        # elif (direction == 'up'):
        #     # ブロックの端ではそれ以降移動できないようにする
        #     if (self.__player.position[1] == 0 and self.__player_room_position[1]-1 == -1):
        #         return False

        #     forward_mass = type(self.__rooms[self.__player_room_position[0]][self.__player_room_position[1]].layers.terrain_layer.data[self.__player.position[0]][self.__player.position[1]-1])
        #     forward_is_not_corner_of_room = self.__player.position[1]-1 > -1
        #     if (self.__player.position[1]-1 == -1):
        #         next_room = type(self.__rooms[self.__player_room_position[0]][self.__player_room_position[1]-1].layers.terrain_layer.data[self.__player.position[0]][Size.MAX_MASS_IN_ROOM_ONE_SIDE-1])
        #         if (next_room == Tile):
        #             # プレイヤーの移動に伴って、部屋を掃除したり、次の部屋にプレイヤーを移したり
        #             self.__rooms[self.__player_room_position[0]][self.__player_room_position[1]].layers.player_layer.clean()
        #             self.__rooms[self.__player_room_position[0]][self.__player_room_position[1]-1].layers.player_layer.player = self.__player

        #             # プレイヤーの移動。ポジションもろもろ
        #             self.__player_room_position = [self.__player_room_position[0], self.__player_room_position[1]-1]
        #             self.__player.position = [self.__player.position[0], Size.MAX_MASS_IN_ROOM_ONE_SIDE-1]

        # elif (direction == 'down'):
        #     # ブロックの端ではそれ以降移動できないようにする
        #     if (self.__player.position[1] == Size.MAX_MASS_IN_ROOM_ONE_SIDE-1 and self.__player_room_position[1]+1 == Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE):
        #         return False

        #     if (self.__player.position[1]+1 == Size.MAX_MASS_IN_ROOM_ONE_SIDE):
                 
        #         if (self.__player_room_position[1]+1 == Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE):
        #             return False

        #         # ブロックをまたがる
        #         next_room = type(self.__rooms[self.__player_room_position[0]][self.__player_room_position[1]+1].layers.terrain_layer.data[self.__player.position[0]][self.__player.position[1]-1])
        #         if (next_room == Tile):
        #             # プレイヤーの移動に伴って、部屋を掃除したり、次の部屋にプレイヤーを移したり
        #             self.__rooms[self.__player_room_position[0]][self.__player_room_position[1]].layers.player_layer.clean()
        #             self.__rooms[self.__player_room_position[0]][self.__player_room_position[1]+1].layers.player_layer.player = self.__player

        #             # プレイヤーの移動。ポジションもろもろ
        #             self.__player_room_position = [self.__player_room_position[0], self.__player_room_position[1]+1]
        #             self.__player.position = [self.__player.position[0], -1]

        #         return True

        #     else :
        #         forward_mass = type(self.__rooms[self.__player_room_position[0]][self.__player_room_position[1]].layers.terrain_layer.data[self.__player.position[0]][self.__player.position[1]+1])
        #         forward_is_not_corner_of_room = self.__player.position[1]+1 < Size.MAX_MASS_IN_ROOM_ONE_SIDE
        

        if (player_at_end_of_the_room):
            if (player_at_end_of_the_floor): 
                return False

            if (next_room_mass == Tile):
                # プレイヤーの移動に伴って部屋を掃除する
                this_room.layers.player_layer.clean()
                # プレイヤーインスタンスを次の部屋に移す
                next_room.layers.player_layer.player = self.__player
                # プレイヤーがいる部屋のポジションを更新
                self.__player_room_position = next_room_position
                # プレイヤーの部屋内のポジションを更新
                self.__player.position = in_room_position

            return True

        else :
            return (forward_is_not_corner_of_room and (forward_mass == Tile))