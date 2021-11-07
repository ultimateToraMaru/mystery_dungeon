import pygame

# pygameウィンドウにログを表示するシングルトンクラス
class Display():
    __instance = None

    @staticmethod
    def get_instance():
        if Display.__instance == None:
            Display()

        return Display.__instance

    def __init__(self):
        if Display.__instance != None:
            raise Exception('Display class is Singleton ! You should use Display.get_instance() method ! by 2021/10/31 HappyHaloweeen!')

        else :
            # pygame初期化処理
            pygame.display.set_caption("Console Window")        # タイトルバーに表示する文字
            self.__screen = pygame.display.set_mode((400, 300)) # 大きさ400*300の画面を生成
            self.__screen.fill((0,0,0))                         # 画面を黒色(#000000)に塗りつぶし]
            self.__font_size = 20
            self.__font = pygame.font.SysFont('yugothicyugothicuilight', self.__font_size)
            self.__log = []

            Display.__instance = self


    def show_status(self, level, hp, max_hp, mp, max_mp, attack, difense):
        print('**********')
        print('Level:', level)
        print('HP:', hp, '/', max_hp)
        print('MP:', mp, '/', max_mp)
        print('Attack:', attack)
        print('Difense', difense)
        print('**********')

        # text = self.__font.render('***********', True, (255,0,0))
        # self.__screen.blit(text, (0,0))

        # self.__log.append(['**********',
        #                     'Level: '+str(level),
        #                     'HP: '+str(hp)+'/'+str(max_hp),
        #                     'MP: '+str(mp)+'/'+str(max_mp),
        #                     'Attack: '+str(attack),
        #                     'Difense: '+str(difense),
        #                     '**********'])
        # self.__log.append(['testtest', 'testtesttest'])
        self.set_screen_log(['**********',
                            'Level: '+str(level),
                            'HP: '+str(hp)+'/'+str(max_hp),
                            'MP: '+str(mp)+'/'+str(max_mp),
                            'Attack: '+str(attack),
                            'Difense: '+str(difense),
                            '**********'])

    def show_number_of_floors(self, num):
        print(num, '階')

    def show_attack_message(self, attack_chara_name):
        self.set_screen_log([str(attack_chara_name)+'の攻撃！'])

    def show_defence_message(self, target_chara_name, damage):
        self.set_screen_log([str(target_chara_name)+'に'+str(damage)+'のダメージ！'])

    # def test(self):
    #     text = self.__font.render('警告', True, (255,0,0))
    #     self.__screen.blit(text, (0,0))

        # pygame.display.update()     # 画面を更新

    # TODO: self.__logにメッセージをセットする処理とself.__screenにログをセットする処理は分けたほうがいいのか？取り合えず、今はまとめている
    def set_screen_log(self, message_log):
        self.__log.append(message_log)

        i = 0
        self.__screen.fill((0,0,0))  #画面を黒で塗りつぶす
        for one_log in reversed(self.__log):
            for log in one_log:
                text = self.__font.render(log, True, (255,255,255))
                # print(self.__font_size*i)
                self.__screen.blit(text, (0,self.__font_size*i))

                i+=1