from tools.display import Display
from dungeon.dungeon import Dungeon
from tools.camera import Camera
from dungeon.room.object_layers.objects.player import Player
from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.floor import Floor
import pyxel
import pygame
from dungeon.room.room import Room
import subprocess
# import os
# import sys

# def resource_path(relative):
#     if hasattr(sys, "_MEIPASS"):
#         return os.path.join(sys._MEIPASS, relative)
#     return os.path.join(relative)


class App:
    def __init__(self):

        # pygame初期化処理
        pygame.init()
        pygame.mouse.set_visible(True)

        # スタート画面
        self.start_disp()

        # pyxel初期化処理
        # pyxel.init(255, 255, caption="mystery_dungeon", scale=3, fps=5)   # 5*5
        # pyxel.init(200, 200, caption="mystery_dungeon", scale=2, fps=5)     # 10*10
        # pyxel.init(255, 255, caption="Mystery_Dungeon", scale=3, fps=10)     # 16*16

        pyxel.init(200, 200, title="Mystery_Dungeon", fps=10)     # 16*16
        pyxel.mouse(False)
        pyxel.load("my_resource.pyxres")

        # bgm再生
        pyxel.playm(1, loop=True)

        # ダンジョンを生成してゲームを始める
        self.dungeon = Dungeon(_id=0)
        self.dungeon.start_turn()

        pyxel.run(self.update, self.draw)

    # スタート画面を表示する
    def start_disp(self):
        pygame.display.set_caption('Start_Mystery_Dungeon')
        screen = pygame.display.set_mode((600, 600))
        screen.fill((100, 100, 100))

        # font_title = pygame.font.SysFont('couriernew', 60, bold=True)
        # title = font_title.render('Mystery Dungeon', True, (255,255,255))
        # screen.blit(title, (30,100))

        # font_sub_title = pygame.font.SysFont('couriernew', 30, bold=True)
        # title = font_sub_title.render("It's a Small trip!", True, (0,50,60))
        # screen.blit(title, (30,170))

        title = pygame.image.load("assets/title8.png").convert()
        scale = 1
        title = pygame.transform.scale(title, (1000*scale, 700*scale)) #200 * 130に画像を縮小
        screen.blit(title, (-200, 0))

        img1 = pygame.image.load("assets/img1.jpg").convert()
        img1 = pygame.transform.scale(img1, (350, 200)) #200 * 130に画像を縮小
        screen.blit(img1, (400, 400))

        # colorkey = img1.get_at((0,0))
        # img1.set_colorkey(colorkey, pygame.RLEACCEL)

        font_message = pygame.font.SysFont('couriernew', 25, bold=True)
        message = font_message.render('~Press Space Button~', True, (255,255,255, 1))
        screen.blit(message, (50,500))

        # スペースボタンが押されたらゲーム画面に遷移
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
        # if pyxel.btnp(pyxel.KEY_Q):
        #     pyxel.quit()

    # 描画処理の更新
    def draw(self):
        # ゲーム画面を更新
        self.dungeon.camera_show()

        # ダンジョンログ画面を更新
        pygame.display.update()

if __name__ == '__main__':
    app = App()
