import pyxel
import math
x = 30
y = 45
w = 14
h =17
u =5
v = 2

shadow_w =4
shadow_h =4

class Tree:
    def __init__(self):
        #初期設定
        #木
        self.x = x
        self.y = y
        self.w = w
        self.h = 2
        self.u = u
        self.v = v
        #木の影
        self.shadow_w = shadow_w
        self.shadow_h = shadow_h

    def update(self,time,speed):
        self.time = time
        if self.time >= 80:
            if self.h < h:
                self.x -= 0.5*speed
                self.h += 1*speed
                self.y -= 1*speed

            if self.h >= h:
                self.h = h
                self.x -= 1*speed
                self.y += 1*speed
                self.shadow_w += 0.2*speed
                self.shadow_h += 0.05*speed

class Background():
    def __init__(self):
        self.game_time = 0
        self.background = []
    
    def update(self,time,speed):
        self.game_time += 1

        if self.game_time>30 :
            self.new_tree = Tree()
            self.background.append(self.new_tree)
            self.game_time = 0
        for tree in self.background:
            tree.update(time,speed)

    def draw(self):
        for tree in self.background:

       #影  
            if tree.h >= h:
                pyxel.elli(tree.x + tree.shadow_w/2 ,
                        tree.y + tree.shadow_h + 8,
                        tree.shadow_w,
                        tree.shadow_h,
                        13)
        #木
            pyxel.blt(tree.x,
                   tree.y,
                    0,
                    tree.u,
                    tree.v,
                    tree.w,
                    tree.h,
                    14)
