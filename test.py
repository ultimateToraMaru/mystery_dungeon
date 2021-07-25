import pyxel



class App:
    def __init__(self):
        pyxel.init(160, 120, caption="mystery_dungeon", scale=5, fps=5)
        pyxel.load("my_resource.pyxres")


        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.blt(0, 0, img=1, u=0, v=0, w=5, h=5)

if __name__ == '__main__':
    app = App()