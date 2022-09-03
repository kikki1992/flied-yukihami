import pyxel
from game import *

move = 58

Win_w = 160
Win_h = 90

#Player 定数
player_x = 78
player_y = 88

#stage1
center1_img_x = 158
center1_img_y = 3
center1_w = 38
center1_h = 30
side1_img_x = 98
side1_img_y = 4
side1_w = 38
side1_h = 30

#stage2
center2_img_x = 210
center2_img_y = 3
center2_w = 38
center2_h = 30
side2_img_x = 154
side2_img_y = 56
side2_w = 38
side2_h = 30

#stage3
center3_img_x = 210
center3_img_y = 56
center3_w = 38
center3_h = 32
side3_img_x = 154
side3_img_y = 98
side3_w = 38
side3_h = 32


class Stage1:
    def __init__(self):
        
        #初期設定
        self.x = Win_w/2 + player_x/2
        self.y = player_y
        
    def update(self,time):
        self.time = time
        if self.time >= 80:
            #プレイヤーの移動
            if pyxel.btnp(pyxel.KEY_LEFT) and self.x > 30:
                self.x -= move
            if pyxel.btnp(pyxel.KEY_RIGHT) and self.x < 90: 
                self.x += move

    def draw(self,flag,eat):

        if eat == 1:
            pyxel.blt(self.x-4,
                    self.y,
                    1,
                    14,
                    92,
                    50,
                    30,
                    14)
        
        elif flag == 1 and self.x < 30:
            pyxel.blt(self.x,
                    self.y,
                    0,
                    side1_img_x,
                    side1_img_y,
                    side1_w,
                    side1_h,
                    14)

        elif flag == 1 and self.x >90:
            pyxel.blt(self.x,
                    self.y,
                    0,
                    side1_img_x,
                    side1_img_y,
                    -side1_w,
                    side1_h,
                    14)

        elif flag == 1 and (self.x > 30 and self.x <90):
            pyxel.blt(self.x,
                    self.y,
                    0,
                    center1_img_x,
                    center1_img_y,
                    center1_w,
                    center1_h,
                    14)
#stage2
        elif flag == 2 and self.x < 30:
            pyxel.blt(self.x,
                    self.y,
                    0,
                    side2_img_x,
                    side2_img_y,
                    side2_w,
                    side2_h,
                    14)

        elif flag == 2 and self.x >90:
            pyxel.blt(self.x,
                    self.y,
                    0,
                    side2_img_x,
                    side2_img_y,
                    -side2_w,
                    side2_h,
                    14)

        elif flag == 2 and (self.x > 30 and self.x <90):
            pyxel.blt(self.x,
                    self.y,
                    0,
                    center2_img_x,
                    center2_img_y,
                    center2_w,
                    center2_h,
                    14)

#stage3
        elif flag == 3 and self.x < 30:
            pyxel.blt(self.x,
                    self.y,
                    0,
                    side3_img_x,
                    side3_img_y,
                    side3_w,
                    side3_h,
                    14)

        elif flag == 3 and self.x >90:
            pyxel.blt(self.x,
                    self.y,
                    0,
                    side3_img_x,
                    side3_img_y,
                    -side3_w,
                    side3_h,
                    14)

        elif flag == 3 and (self.x > 30 and self.x <90):
            pyxel.blt(self.x,
                    self.y,
                    0,
                    center3_img_x,
                    center3_img_y,
                    center3_w,
                    center3_h,
                    14)