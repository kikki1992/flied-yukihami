from asyncio import selector_events
import pyxel
import random
from apple import *
from baloon import *

#0 空白、１：Apple、２：Balloon
l = [
    [0,1,2], #0
    [0,2,1], #1
    [1,0,2], #2
    [1,2,0], #3
    [2,0,1], #4
    [2,1,0], #5
    [1,1,2], #6
    [1,2,1], #7
    [2,1,1], #8
]
x_pos = [54,74,94]
x_plus = [-1,0,1]

class Point():
    def __init__(self):
        self.game_time = 0
        #出現
        self.y = 40
        self.count = 0
        self.points = []
        self.apples = []
        self.baloons = []
        self.apple_x_plus = []
        self.baloon_x_plus = []
        self.stop_time = 150
        self.score = 0
        self.eat = 0
           
    def update(self,p_x,p_y,speed,flag):
        self.stop_time += 1
        #イベント出現条件 stage1
        if flag == 1:
            if self.score < 10:
                if self.game_time >10 :
                    self.num = pyxel.rndi(0,8)
                    self.points.append(l[self.num])
                    for j in range(3): #りんご、風船、何もなしの３つのパターンで場合分け
                        if self.points[self.count][j] == 1: #りんごの場合
                            self.new_apple = Apple(x_pos[j],self.y)
                            self.apples.append(self.new_apple)
                            if x_pos[j] == x_pos[0]:
                                self.apple_x_plus.append(x_plus[0])
                            elif x_pos[j] == x_pos[1]:
                                self.apple_x_plus.append(x_plus[1])
                            elif x_pos[j] == x_pos[2]:
                                self.apple_x_plus.append(x_plus[2])
                        elif self.points[self.count][j] == 2: # 風船の場合
                            self.new_baloon = Baloon(x_pos[j],self.y)
                            self.baloons.append(self.new_baloon)
                            if x_pos[j] == x_pos[0]:
                                self.baloon_x_plus.append(x_plus[0])
                            elif x_pos[j] == x_pos[1]:
                                self.baloon_x_plus.append(x_plus[1])
                            elif x_pos[j] == x_pos[2]:
                                self.baloon_x_plus.append(x_plus[2])
                    self.count += 1 #イベントのナンバー
                    self.game_time = 0 #イベントタイムリセット

            # stage2
            elif self.score <20:
                if self.game_time >6 :
                    self.num = pyxel.rndi(0,8)
                    self.points.append(l[self.num])
                    for j in range(3): #りんご、風船、何もなしの３つのパターンで場合分け
                        if self.points[self.count][j] == 1: #りんごの場合
                            self.new_apple = Apple(x_pos[j],self.y)
                            self.apples.append(self.new_apple)
                            if x_pos[j] == x_pos[0]:
                                self.apple_x_plus.append(x_plus[0])
                            elif x_pos[j] == x_pos[1]:
                                self.apple_x_plus.append(x_plus[1])
                            elif x_pos[j] == x_pos[2]:
                                self.apple_x_plus.append(x_plus[2])
                        elif self.points[self.count][j] == 2: # 風船の場合
                            self.new_baloon = Baloon(x_pos[j],self.y)
                            self.baloons.append(self.new_baloon)
                            if x_pos[j] == x_pos[0]:
                                self.baloon_x_plus.append(x_plus[0])
                            elif x_pos[j] == x_pos[1]:
                                self.baloon_x_plus.append(x_plus[1])
                            elif x_pos[j] == x_pos[2]:
                                self.baloon_x_plus.append(x_plus[2])
                    self.count += 1 #イベントのナンバー
                    self.game_time = 0 #イベントタイムリセット

            #stage3
            else:
                if self.game_time >4 :
                    self.num = pyxel.rndi(0,8)
                    self.points.append(l[self.num])
                    for j in range(3): #りんご、風船、何もなしの３つのパターンで場合分け
                        if self.points[self.count][j] == 1: #りんごの場合
                            self.new_apple = Apple(x_pos[j],self.y)
                            self.apples.append(self.new_apple)
                            if x_pos[j] == x_pos[0]:
                                self.apple_x_plus.append(x_plus[0])
                            elif x_pos[j] == x_pos[1]:
                                self.apple_x_plus.append(x_plus[1])
                            elif x_pos[j] == x_pos[2]:
                                self.apple_x_plus.append(x_plus[2])
                        elif self.points[self.count][j] == 2: # 風船の場合
                            self.new_baloon = Baloon(x_pos[j],self.y)
                            self.baloons.append(self.new_baloon)
                            if x_pos[j] == x_pos[0]:
                                self.baloon_x_plus.append(x_plus[0])
                            elif x_pos[j] == x_pos[1]:
                                self.baloon_x_plus.append(x_plus[1])
                            elif x_pos[j] == x_pos[2]:
                                self.baloon_x_plus.append(x_plus[2])
                    self.count += 1 #イベントのナンバー
                    self.game_time = 0 #イベントタイムリセット
            
        self.apples_count = len(self.apples) #りんごの数
        self.baloons_count = len(self.baloons) #風船の数

        if self.stop_time>= 80:
            self.eat = 0
            self.game_time += pyxel.frame_count % 2
            for i in range (self.apples_count):
                self.apples[i].update(self.apple_x_plus[i]*speed,2*speed) 
 
            for i in range (self.baloons_count):
                self.baloons[i].update(self.baloon_x_plus[i]*speed,2*speed) 

        #りんご当たり判定
        for i in range(self.apples_count):
            if ((p_x-5 <= self.apples[i].x)
                and (self.apples[i].x <= p_x + 20)
                and (p_y +2 <= self.apples[i].y)
                and (self.apples[i].y <= p_y +12)
                and self.apples[i].is_alive == True):
                self.apples[i].is_alive = False
                self.stop_time = 0
                self.eat = 1
                pyxel.play(0,1)

        #風船当たり判定
        for i in range(self.baloons_count):
            if ((p_x-5 <= self.baloons[i].x)
                and (self.baloons[i].x <= p_x + 20)
                and (p_y +2 <= self.baloons[i].y)
                and (self.baloons[i].y <= p_y +12)
                and self.baloons[i].is_alive == True):
                self.baloons[i].is_alive = False
                self.score += 1
                pyxel.play(0,0)
        
    def draw(self):
        for apple in self.apples:
            if apple.is_alive ==True:
                pyxel.blt(apple.x,
                        apple.y,
                        0,
                        apple.u,
                        apple.v,
                        apple.w,
                        apple.h,
                        14)

        for baloon in self.baloons:
            if baloon.is_alive ==True:
                pyxel.blt(baloon.x,
                        baloon.y,
                        0,
                        baloon.u,
                        baloon.v,
                        baloon.w,
                        baloon.h,
                        14)