import pyxel
import random

w = 12
h = 2
u = 43
v = 6

class Baloon:
    def __init__(self,x,y):
        #初期設定
        self.x = x
        self.y = y
        self.is_alive = True
        self.w = w
        self.h = h
        self.u = u
        self.v = v

    def update(self,plus_x,plus_y):
        if self.h < 15:
            self.h += plus_y/2
            self.y -= plus_y/2
        else:
            self.y += plus_y
            self.x += plus_x
                
    def draw(self):
        pyxel.blt(self.x,
            self.y,
            0,
            self.u,
            self.v,
            self.w,
            self.h,
            14)
