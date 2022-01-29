
import pygame
import time
import asyncio

# pygameウィンドウにログを表示するシングルトンクラス
# get_instanceメソッドでインスタンスを取得
class Display():
    __instance = None

    @staticmethod
    def get_instance():
        if Display.__instance == None:
            Display()

        return Display.__instance

    # 直接インスタンスを生成しようとするとエラー
    def __init__(self):
        if Display.__instance != None:
            raise Exception('Display class is Singleton ! You should use Display.get_instance() method ! by 2021/10/31 HappyHaloweeen!')

        else :
            # pygame初期化処理
            pygame.display.set_caption('Dungeon Log')
            self.__screen = pygame.display.set_mode((900, 200)) # ウィンドウの大きさ
            self.__screen.fill((0,0,0))                         # 背景色

            self.__font_size = 15
            self.__font = pygame.font.SysFont('yugothicyugothicuilight', self.__font_size)
            self.__log_queue = []

            Display.__instance = self


    def show_status(self, name, level, hp, max_hp, mp, max_mp, attack, difense, exp):
        """ステータスを表示

        Args:
            name ([type]): [description]
            level ([type]): [description]
            hp ([type]): [description]
            max_hp ([type]): [description]
            mp ([type]): [description]
            max_mp ([type]): [description]
            attack ([type]): [description]
            difense ([type]): [description]
            exp ([type]): [description]
        """

        self.set_log(['**********************',
                            'Name: '+str(name),
                            'Level: '+str(level),
                            'HP: '+str(hp)+'/'+str(max_hp),
                            'MP: '+str(mp)+'/'+str(max_mp),
                            'Attack: '+str(attack),
                            'Difense: '+str(difense),
                            'Exp: '+str(exp),
                            '**********************'])

    def show_number_of_floors(self, num):
        self.set_log([str(num)+'階'])

    def show_battle_message(self, attacker_name, defenser_name, damage):
        self.set_log([str(attacker_name)+'の攻撃！',
                            str(defenser_name)+'に'+str(damage)+'のダメージ！'])

    def show_fool_battle_message(self, attacker_name):
        self.set_log([str(attacker_name)+'の攻撃！',
                            'しかし、攻撃は空ぶった！'])

    def show_destroy_message(self, attacker_name, defenser_name, exp):
        self.set_log([str(defenser_name)+'は倒れた！',
                            str(attacker_name)+'は'+str(exp)+'の経験値を手に入れた！'])

    def show_level_up(self, name, new_level, max_hp, max_mp, attack, defense):
        self.set_log([str(name)+'のレベルが上がった！',
                            'やったね！！！',
                            'level: '+str(new_level),
                            'max_hp: +'+str(max_hp),
                            'max_mp: +'+str(max_mp),
                            'attack: +'+str(attack),
                            'defense: +'+str(defense),
                            ])

    def show_game_over(self, player_name, dungeon_name):
        self.set_log([str(player_name)+'は、'+str(dungeon_name)+'の攻略中に',
                            '力尽きた...'])

    def show_game_clear(self, player_name, dungeon_name):
        self.set_log([str(player_name)+'は、'+str(dungeon_name)+'の攻略に成功した！',
                            'おめでとう！'])

    def set_log(self, message):
        """キューにメッセージをセット

        Args:
            message (str): メッセージ
        """

        self.__log_queue.append(message)


    def out_log(self):
        """キューにたまったログを出力
        """

        row_index = 0

        # 画面を黒で塗りつぶす
        self.__screen.fill((0,0,0))

        # ひとまとまりのログを取り出す
        for one_log in reversed(self.__log_queue):
            for log in one_log:
                text = self.__font.render(log, True, (255,255,255))
                x = 610
                margin = 10
                self.__screen.blit(text, (x ,self.__font_size*row_index + margin))

                row_index+=1

            # 区切り線をセットする
            text_line = self.__font.render('-----------------------------------------------', True, (255,255,255))

            # 行単位でログを表示する
            self.__screen.blit(text_line, (x ,self.__font_size*row_index + margin))

            row_index+=1

#         # 非同期で実行
#         loop = asyncio.get_event_loop()
#         loop.run_until_complete(sleeping(0.5))

# async def sleeping(sec):
#     loop = asyncio.get_event_loop()
#     # print(f'start:  {sec}秒待つよ')
#     await loop.run_in_executor(None, time.sleep, sec)
#     # print(f'finish: {sec}秒待つよ')