import pyxel
from pyxelunicode import PyxelUnicode
import PyxelUniversalFont as puf
from start import *
from game import *
from end1 import *
from end2 import *

class App():
    def __init__(self):
        #Windowの作成(最初に設定)
        pyxel.init(160,120,title="Flying Hami")
        #imgファイルの用意(先にinitializeしないと動かない)
        pyxel.load("assets/img.pyxres")
        self.flag = 1
        self.start = Start()
        self.game = Game()
        self.end1 = End1()
        self.end2 = End2()
        pyxel.run(self.update,self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_S):
            self.flag =2
        if self.game.time < 0 and self.game.point.score <= 45:
            self.flag = 3
        if self.game.time < 0 and self.game.point.score > 45:
            self.flag = 4
        
        if pyxel.btn(pyxel.KEY_R):
            self.flag = 1
            self.game = Game()
            #self.game = Game()
            self.end1 = End1()
            self.end2 = End2()
        
        if self.flag == 1:
            self.start.update()
        elif self.flag == 2:
            self.game.update()
        elif self.flag == 3:
            self.end1.update()
        elif self.flag == 4:           
            self.end2.update()
            

    def draw(self):
        if self.flag == 1:
            self.start.draw()
        elif self.flag == 2:
            self.game.draw()
        elif self.flag == 3:
            self.end1.draw()
        elif self.flag == 4:
            self.end2.draw()


App()