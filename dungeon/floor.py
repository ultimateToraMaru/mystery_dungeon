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
    def __init__(self):
        self.__rooms = [[Room('none')] * Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE for i in range(Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE)]    # 配列の枠組みを作っておく。下の初期化処理と併用して行う。絶対。
        # 初期化処理。要素に別々のインスタンスを入れ込んでいく
        for i in range(Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE):
            for j in range(Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE):
                self.__rooms[i][j] = Room('none')

        # ***_room_addressをいつかなくす
        self.__player_start_room_address = [0, 0]
        self.__player = Player(Color.BLACK)
        self.__steps_room_address = [0, 0]
        self.__steps = None_obj()
        self.__enemys = []
        
        self.__rooms = self.generate_room()


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
    def generate_room(self):
        min_rooms = 5
        max_rooms = 10

        room_qty = random.randint(min_rooms, max_rooms)
        rooms = [[Room('none')] * Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE for i in range(Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE)]
        for i in range(Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE):
            for j in range(Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE):
                rooms[i][j] = Room('none')
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

        print('部屋の数', room_qty)

        start_room = random.randint(0, room_qty-1)    # startする部屋をランダムで選ぶ。上からr番目みたいな感じ。
        for i in range(room_qty):
            r_x = random.randint(0, Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1) 
            r_y = random.randint(0, Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1) 
            if (i == start_room):
                rooms[r_x][r_y] = Room('normal')
                self.__player_start_room_address = [r_x, r_y]
                print('プレイヤーがいる部屋の座標', self.__player_start_room_address)
            else :
                rooms[r_x][r_y] = Room('normal')
        
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
    
    # 部屋のプレイヤーレイヤーを読み取り、オブジェクトにdrawの指示を出す
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
        player = self.__rooms[self.__player_start_room_address[0]][self.__player_start_room_address[1]].layers.player_layer.set_start_position(self.__player)
        self.__player = player
        self.__player.room_address = self.__player_start_room_address
        print('プレイヤーのいるお部屋', self.__player.room_address, '座標 :', self.__player.position)
    
    # 階段を生み出す。フロア到達時に一階だけ実行される。
    def spawn_steps(self):
        
        while (True): 
            r_x = random.randint(0, Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1)
            r_y = random.randint(0, Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1)
            if (self.__rooms[r_x][r_y].type == 'normal'):
                self.__steps_room_address = [r_x, r_y]
                self.__steps = Steps()
                break

        print('階段のあるお部屋', self.__steps_room_address[0], self.__steps_room_address[1])
        self.__rooms[r_x][r_y].generate_steps(self.__steps)
    
    # エネミーをランダムな部屋に生み出す。エネミーが生まれる部屋をランダムで決める。
    def spawn_enemys(self):
        for i in range(len(self.__rooms)):
            for j in range(len(self.__rooms)):
                is_enemy_spawn = random.randint(0, 1)
                if (is_enemy_spawn):
                    self.__enemys.extend(self.__rooms[i][j].generate_enemys(i, j))
        
        print(self.__enemys)
        self.enemy_set_target()
                    
    
    

    # プレイヤー自身の座標を受け取って、セットする
    def player_set_position(self):
        self.__rooms[self.__player.room_address[0]][self.__player.room_address[1]].layers.player_layer.set_position(self.__player)
        # self.is_player_on_steps()
    
    # エネミー自身の座標を受け取って、セットする
    def enemy_set_position(self):
        for i in range(len(self.__enemys)):
            self.__rooms[self.__enemys[i].room_address[0]][self.__enemys[i].room_address[1]].layers.enemy_layer.set_position(self.__enemys[i])

    # プレイヤーが階段の上にいるか検査する
    def is_player_on_steps(self):
        return self.__rooms[self.__steps_room_address[0]][self.__steps_room_address[1]].steps_check()

    # プレイヤーを動かす
    def player_move(self, direction):
        if (self.is_can_move_character(self.__player, direction)):
            self.__player.move(direction)
    
    # エネミーを動かす
    def enemy_move(self, direction):
        for i in range(len(self.__enemys)):
            # print('move')  
            if (self.is_can_move_character(self.__enemys[i], direction)):
                self.__enemys[i].move(direction)
        
    
    # キャラクターが行こうとしているところが、移動できるところかどうか(部屋の隅、敵じゃないか？)
    def is_can_move_character(self, character, direction):
        # 調査の結果、上の部屋に移動しようとしたときに移動先の座標がおかしい
        print('部屋の番地:', character.room_address, ' 部屋内:', character.position, character)
        if (direction == 'right'):
            character_at_end_of_the_room = character.position[0] == Size.MAX_MASS_IN_ROOM_ONE_SIDE-1
            character_at_end_of_the_floor = character.room_address[0]+1 == Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE
            if (character_at_end_of_the_room):
                if (character_at_end_of_the_floor): 
                    return False
                next_room_mass_is_noneobj = self.__rooms[character.room_address[0]+1][character.room_address[1]].layers.is_noneobj(Size.MAX_MASS_IN_ROOM_ONE_SIDE-1, character.position[1])
                this_room = self.__rooms[character.room_address[0]][character.room_address[1]]
                next_room = self.__rooms[character.room_address[0]+1][character.room_address[1]]
                next_room_position = [character.room_address[0]+1, character.room_address[1]]
                in_room_position = [-1, character.position[1]]
            else :
                forward_mass_is_noneobj = self.__rooms[character.room_address[0]][character.room_address[1]].layers.is_noneobj(character.position[0]+1, character.position[1])
                forward_is_not_corner_of_room = character.position[0]+1 < Size.MAX_MASS_IN_ROOM_ONE_SIDE
        
        elif (direction == 'left'):
            character_at_end_of_the_room = character.position[0] == 0
            character_at_end_of_the_floor = character.room_address[0]-1 == -1
            if (character_at_end_of_the_room):
                next_room_mass_is_noneobj = self.__rooms[character.room_address[0]-1][character.room_address[1]].layers.is_noneobj(Size.MAX_MASS_IN_ROOM_ONE_SIDE-1, character.position[1])
                this_room = self.__rooms[character.room_address[0]][character.room_address[1]]
                next_room = self.__rooms[character.room_address[0]-1][character.room_address[1]]
                next_room_position = [character.room_address[0]-1, character.room_address[1]]
                in_room_position = [Size.MAX_MASS_IN_ROOM_ONE_SIDE, character.position[1]]
            else :
                forward_mass_is_noneobj = self.__rooms[character.room_address[0]][character.room_address[1]].layers.is_noneobj(character.position[0]-1, character.position[1])
                forward_is_not_corner_of_room = character.position[0]-1 > -1
        
        elif (direction == 'up'):
            character_at_end_of_the_room = character.position[1] == 0
            character_at_end_of_the_floor = character.room_address[1]-1 == -1
            if (character_at_end_of_the_room):
                next_room_mass_is_noneobj = self.__rooms[character.room_address[0]][character.room_address[1]-1].layers.is_noneobj(character.position[0], Size.MAX_MASS_IN_ROOM_ONE_SIDE-1)
                this_room = self.__rooms[character.room_address[0]][character.room_address[1]]
                next_room = self.__rooms[character.room_address[0]][character.room_address[1]-1]
                next_room_position = [character.room_address[0], character.room_address[1]-1]
                in_room_position = [character.position[0], Size.MAX_MASS_IN_ROOM_ONE_SIDE]
            else :
                forward_mass_is_noneobj = self.__rooms[character.room_address[0]][character.room_address[1]].layers.is_noneobj(character.position[0], character.position[1]-1)
                forward_is_not_corner_of_room = character.position[1]-1 > -1

        elif (direction == 'down'):
            character_at_end_of_the_room = character.position[1] == Size.MAX_MASS_IN_ROOM_ONE_SIDE-1
            character_at_end_of_the_floor = character.room_address[1]+1 == Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE
            if (character_at_end_of_the_room):
                if (character_at_end_of_the_floor): 
                    return False
                next_room_mass_is_noneobj = self.__rooms[character.room_address[0]][character.room_address[1]+1].layers.is_noneobj(character.position[0], character.position[1]-1)
                this_room = self.__rooms[character.room_address[0]][character.room_address[1]]
                next_room = self.__rooms[character.room_address[0]][character.room_address[1]+1]
                next_room_position = [character.room_address[0], character.room_address[1]+1]
                in_room_position = [character.position[0], -1]
            else :
                forward_mass_is_noneobj = self.__rooms[character.room_address[0]][character.room_address[1]].layers.is_noneobj(character.position[0], character.position[1]+1)
                forward_is_not_corner_of_room = character.position[1]+1 < Size.MAX_MASS_IN_ROOM_ONE_SIDE

        # プレイヤーが部屋の端にいるとき
        if (character_at_end_of_the_room):
            # その部屋がブロックの端のとき、終了(世界の果てには移動できない)
            if (character_at_end_of_the_floor):
                return False
            # 次の部屋のマスが床のとき(障害物がないとき)
            if (next_room_mass_is_noneobj):
                # キャラクターの移動に伴って部屋を掃除する(08/12, いつか、cleanメソッドをlayerクラスに作る)
                this_room.layers.enemy_layer.clean()
                this_room.layers.player_layer.clean()
                # キャラクターを次の部屋に移す(ルームアドレスを更新)
                character.room_address = next_room_position
                # キャラクターの部屋内のポジションを更新
                character.position = in_room_position

            return True

        # キャラクターが部屋の中を移動するとき
        else :
            return (forward_is_not_corner_of_room and forward_mass_is_noneobj)
    
    def get_player_room_arounds(self):
        player_room = self.__rooms[self.__player.room_address[0]][self.__player.room_address[1]]
        player_rooms = self.__rooms # 5*5
        # room_position = [   [-1, -1], [-1, 0], [-1, +1],
        #                     [0, -1], [0, 0], [0, +1],
        #                     [+1, -1], [+1, 0], [+1, +1],
        #                 ]
        # player_around_rooms = []
        # for pos in room_position :
        #     player_around_rooms.append(self.__rooms[self.__player_room_position[0]+pos[0]][self.__player_room_position[1]+pos[1]])

        # return player_room    # 16*16
        return player_rooms    # 5*5
    
    def enemy_set_target(self):
        print('set_ready')
        for i in range(len(self.__enemys)):
            print(i, 'set!')
            self.__enemys[i].target = self.__player
    
    def enemy_mind(self):
        for i in range(len(self.__enemys)):
            self.__enemys[i].mind()