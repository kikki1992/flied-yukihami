
import pyxel
#from pyxelunicode import PyxelUnicode
import PyxelUniversalFont as puf
#クリア画面

#font
#gothic_path = "assets/misaki_ttf_2021-05-05/misaki_gothic.ttf" # ttfファイルのパス
#gothic_size = 8  # このフォントが設計された大きさ(px単位)を代入する
mplus_path = "assets/misaki_ttf_2021-05-05/PixelMplus10-Regular.ttf"
message1 = "りんごを食べて満足"
message2 = "つぎは空を飛ぼう　Restart R"

class End1():
    def __init__(self):
        self.block1 = 0
        self.block2 = 0
        self.block3 = 0
        self.block4 = 0
        self.block5 = 0
        self.block6 = 0
        self.time = 0
        self.message_list = list(message1)
        self.message_list2 = list(message2)
        self.mozi = []
        self.messe1 = ""
        self.mozi2 = []
        self.messe2 = ""
        self.count = 0
        self.count2 = 0
        self.gothic = puf.Writer("misaki_gothic.ttf")
        

    def update(self):
        
        self.time += 1
        self.block1 += 9
        self.block2 += 8
        self.block3 += 7
        self.block4 += 6
        self.block5 += 5
        self.block6 += 4

    def draw(self):
        #15,93 45,115

        pyxel.rect(0, 0, self.block1, 20, 8)
        pyxel.rect(0, 20, self.block2, 20, 9)
        pyxel.rect(0, 40, self.block3, 20, 10)
        pyxel.rect(0, 60, self.block4, 20, 11)
        pyxel.rect(0, 80, self.block5, 20, 12)
        pyxel.rect(0, 100, self.block6, 20, 1)

        if self.time == 1:
            pyxel.play(0,6)
        if self.time > 80:
            pyxel.cls(7)
            pyxel.blt(20,0,0,0,140,120,110,14)

        if self.time >120 :
            pyxel.rect(20, 89, 130, 22, 1)
            pyxel.rect(21, 90, 128, 20, 7)
            self.gothic.draw(22,92,self.messe1,8)
            self.gothic.draw(22,100,self.messe2,8)

            if self.count < len(self.message_list):
                self.mozi.append(self.message_list[self.count])
                self.count += 1
                self.messe1 = ''.join(self.mozi)
                pyxel.play(0,9)

            elif self.count2 < len(self.message_list2):
                self.mozi2.append(self.message_list2[self.count2])
                self.count2 += 1
                self.messe2 = ''.join(self.mozi2)
                pyxel.play(0,9)
