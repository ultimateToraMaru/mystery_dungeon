import pygame
import time

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
            self.__screen = pygame.display.set_mode((900, 700)) # ウィンドウの大きさ
            self.__screen.fill((0,0,0))                         # 背景色

            self.__font_size = 20
            self.__font = pygame.font.SysFont('yugothicyugothicuilight', self.__font_size)
            self.__log = []

            Display.__instance = self


    def show_status(self, name, level, hp, max_hp, mp, max_mp, attack, difense, exp):
        self.set_screen_log(['**********************',
                            'Name: '+str(name),
                            'Level: '+str(level),
                            'HP: '+str(hp)+'/'+str(max_hp),
                            'MP: '+str(mp)+'/'+str(max_mp),
                            'Attack: '+str(attack),
                            'Difense: '+str(difense),
                            'Exp: '+str(exp),
                            '**********************'])

    def show_number_of_floors(self, num):
        self.set_screen_log([str(num)+'階'])

    def show_battle_message(self, attacker_name, defenser_name, damage):
        self.set_screen_log([str(attacker_name)+'の攻撃！',
                            str(defenser_name)+'に'+str(damage)+'のダメージ！'])

    def show_fool_battle_message(self, attacker_name):
        self.set_screen_log([str(attacker_name)+'の攻撃！',
                            'しかし、攻撃は空ぶった！'])

    def show_destroy_message(self, attacker_name, defenser_name, exp):
        self.set_screen_log([str(defenser_name)+'は倒れた！',
                            str(attacker_name)+'は'+str(exp)+'の経験値を手に入れた！'])

    def show_level_up(self, name, new_level, max_hp, max_mp, attack, defense):
        self.set_screen_log([str(name)+'のレベルが上がった！',
                            'やったね！！！',
                            'level: '+str(new_level),
                            'max_hp: +'+str(max_hp),
                            'max_mp: +'+str(max_mp),
                            'attack: +'+str(attack),
                            'defense: +'+str(defense),
                            ])

    def show_game_over(self, player_name, dungeon_name):
        self.set_screen_log([str(player_name)+'は、'+str(dungeon_name)+'の攻略中に',
                            '力尽きた...'])

    def show_game_clear(self, player_name, dungeon_name):
        self.set_screen_log([str(player_name)+'は、'+str(dungeon_name)+'の攻略に成功した！',
                            'おめでとう！'])

    # TODO: self.__logにメッセージをセットする処理とself.__screenにログをセットする処理は分けたほうがいいのか？取り合えず、今はまとめている
    def set_screen_log(self, message_log):
        self.__log.append(message_log)

        row_index = 0

        # 画面を黒で塗りつぶす
        self.__screen.fill((0,0,0))

        # ひとまとまりのログを取り出す
        for one_log in reversed(self.__log):
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

            # time.sleep(0.1)