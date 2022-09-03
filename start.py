from email import message
import pyxel
from pyxelunicode import PyxelUnicode

#font
gothic_path = "assets/misaki_ttf_2021-05-05/misaki_gothic.ttf" # ttfファイルのパス
gothic_size = 8  # このフォントが設計された大きさ(px単位)を代入する
mplus_path = "assets/misaki_ttf_2021-05-05/PixelMplus10-Regular.ttf"
message1 = "空飛びたい・・"

class Start():
    def __init__(self):
        self.animetime = 0
        self.x = -40
        self.y = 60
        self.w = 35
        self.h = 30
        self.img_y = 90
        self.message_list = list(message1)
        self.mozi = []
        self.count = 0
        self.gothic = PyxelUnicode(gothic_path, gothic_size)
        self.mplus = PyxelUnicode(mplus_path, 10)

    def update(self):
        self.animetime += 1
        if self.animetime < 100 and self.animetime % 10 == 1:
            self.x += 6
            pyxel.play(0,7)
        if self.animetime == 150:
            self.w += 10
            self.y -= 10
            self.img_y -= 10
            self.h += 10
            pyxel.play(0,3)
        if self.animetime == 180:
            self.w += 80
            self.y -= 40
            self.img_y -= 40
            self.h += 40
            pyxel.play(0,3)
    def draw(self):
        #15,93 45,115
        pyxel.cls(7)
        #移動時のゆきはみ
        pyxel.blt(self.x,self.y,0,15,self.img_y,self.w,self.h,14)
        #考え中のゆきはみ
        if self.animetime >230 :
            if self.animetime % 10 == 9 and self.count < len(self.message_list):
                self.mozi.append(self.message_list[self.count])
                self.count += 1
                pyxel.play(0,9)
            self.gothic.text(22,92,self.mozi,1)

        if self.animetime > 330:
            pyxel.text(22,105,"Game Start Skey",8)