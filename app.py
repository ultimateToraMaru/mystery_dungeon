from dungeon.display import Display
from dungeon.dungeon import Dungeon
from dungeon.camera import Camera
from dungeon.room.object_layers.objects.player import Player
from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.floor import Floor
import pyxel
import pygame
from dungeon.room.room import Room


class App:
    def __init__(self):

        # pygame初期化処理
        pygame.init()
        pygame.mouse.set_visible(True)


        # pyxel初期化処理
        # pyxel.init(255, 255, caption="mystery_dungeon", scale=3, fps=5)   # 5*5
        # pyxel.init(200, 200, caption="mystery_dungeon", scale=2, fps=5)     # 10*10
        pyxel.init(255, 255, caption="Mystery_Dungeon", scale=3, fps=10)     # 16*16
        pyxel.mouse(False)
        pyxel.load("my_resource.pyxres")

        # スタート画面
        self.start_disp()

        # ダンジョンを生成してゲームを始める
        self.dungeon = Dungeon(_id=0)
        self.dungeon.start_turn()

        pyxel.run(self.update, self.draw)

    # スタート画面
    def start_disp(self):
        pygame.display.set_caption('Start_Mystery_Dungeon')
        screen = pygame.display.set_mode((600, 600))

        # タイトルとメッセージ
        screen.fill((0, 0, 0))

        font_title = pygame.font.SysFont('yugothicyugothicuilight', 50, bold=True)
        title = font_title.render('ちょっと', True, (255,255,255))
        screen.blit(title, (50,100))

        title = font_title.render('不思議なダンジョン', True, (255,255,255))
        screen.blit(title, (50,150))

        font_message = pygame.font.SysFont('yugothicyugothicui', 30, bold=True)
        message = font_message.render('～Press Space Button～', True, (255,255,255, 1))
        screen.blit(message, (50,250))

        # bgm再生
        pyxel.playm(1, loop=True)

        spaceBtnPressed = False
        while (not spaceBtnPressed):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    pygame.sys.exit()

                if event.type == pygame.KEYDOWN:
                    # スペースボタンを押したらループから抜ける
                    if event.key == pygame.K_SPACE:
                        spaceBtnPressed = True
                        break

                    elif event.key == pygame.K_Q:
                        pygame.quit()
                        pygame.sys.exit()

                    else:
                        print("pressedKey = " + pygame.key.name(event.key))

                pygame.display.update()

    # ゲーム処理の更新
    def update(self):
        self.dungeon.forward_turn()

        # Qキーでゲームを終了
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    # 描画処理の更新
    def draw(self):
        # ゲーム画面を更新
        self.dungeon.camera_show()

        # ダンジョンログ画面を更新
        pygame.display.update()

if __name__ == '__main__':
    app = App()