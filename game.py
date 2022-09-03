from email import message
from numpy import True_
import pyxel
from pyxelunicode import PyxelUnicode

from pattern import *
from player import *
from apple import *
from baloon import *
from tree import *
from point import *

Win_w = 160
Win_h = 90

#font
gothic_path = "assets/misaki_ttf_2021-05-05/misaki_gothic.ttf" # ttfファイルのパス
gothic_size = 8  # このフォントが設計された大きさ(px単位)を代入する
mplus_path = "assets/misaki_ttf_2021-05-05/PixelMplus10-Regular.ttf"

message_1_1 = "フワンテに協力してもらって飛ぼう"
message_1_2 = "りんごに当たると時間が減るぞ"

class Game():
    def __init__(self):

        self.gothic = PyxelUnicode(gothic_path, gothic_size)
        self.mplus = PyxelUnicode(mplus_path, 10)

        self.time = 900 #ゲームの時間
        #関数のセット
        self.player = Stage1()
        self.tree =Background()
        self.patterns = Patterns(self.time)
        self.point = Point()
        self.time_flag = 1
        self.count = 0
        self.message_flag = 1
        self.mozi_count = 0
        self.stage_flag = 1
        self.m = 1
    def update(self):

        if self.time == 900:
            pyxel.play(0,5)

        if self.time_flag == 1:
            self.time -= 1
        #プレイヤーアップデート(x,y,w,h,is_alive)
        self.player.update(self.point.stop_time)
        if self.point.score == 0 and self.count < 90:
            self.time_flag = 0
            if self.point.stop_time >= 80:
                self.count += 1
            speed = 1
            self.message_flag = 1

        elif self.point.score < 10 and self.count >= 90:
            self.time_flag = 1
            speed = 1
            self.message_flag = 0
        elif self.point.score < 20 and self.count < 180:
            self.time_flag = 0
            if self.point.stop_time >= 80:
                self.count += 1
            speed = 1
            self.message_flag = 2
            self.stage_flag = 2
            self.m += 1
            if self.m == 60:
                pyxel.sound(5).speed=9
                pyxel.play(0,5)
                self.m += 1

        elif self.point.score < 22 and self.count >=180:
            speed = 1.5
            self.time_flag = 1
            self.message_flag = 0
        elif self.point.score < 30 and self.count < 240:
            self.time_flag = 0
            if self.point.stop_time >= 80:
                self.count += 1
            speed = 1.5
            self.message_flag = 3
            self.stage_flag = 3
            self.m += 1
            if self.m == 140:
                pyxel.sound(5).speed=6
                pyxel.play(0,5)
                self.m +=1
        else :
            speed = 2
            self.time_flag = 1
            self.message_flag = 0

        self.point.update(self.player.x,self.player.y,speed,self.time_flag)

        #木の配置　(x,y,w,h,shadow_w,shadoe_h)
        self.tree.update(self.point.stop_time,speed)
        self.patterns.update(self.point.stop_time,speed)

    def draw(self):
        
        pyxel.cls(0)
        #背景
        pyxel.rect(0, 0, 160, 120, 1) #白地面
        pyxel.rect(0, 15, 160, 120, 12) #白地面
        pyxel.rect(0, 30, 160, 120, 6) #白地面
        pyxel.circ(Win_w/2, 220,180, 7) #白地面
        
        #pattern
        self.tree.draw()
        self.patterns.draw()
        self.point.draw()
        self.player.draw(self.stage_flag,self.point.eat)

        self.gothic.text(70,2,"制限時間",9)
        self.mplus.text(110,0,f"{round(self.time/30)}",10)

        self.gothic.text(1,2,"スコア",9)
        self.mplus.text(55,0,f"{self.point.score}",10)

        if self.message_flag == 1:
            pyxel.rect(10, 38, 140, 28, 1)
            pyxel.rect(11, 39, 138, 26, 7)
            self.gothic.text(15,42,message_1_1,1)
            self.gothic.text(15,52,message_1_2,1)
            
        if self.message_flag == 2:
            pyxel.text(62,60,"Stage 2",9)
        if self.message_flag == 3:
            pyxel.text(62,60,"Stage 3",8)

Game()
