import pyxel

u = 0
v = 24
w =3
h =1

u2 = 0
v2 = 26
w2 =3
h2 =2

u3 = 0
v3 = 29
w3 =5
h3 =2

l = [8,28,48,68,88,108,128,148]
m = [10,40,80,10,40,80,10,40]

class Pattern:
    def __init__(self,x):
        #imgファイルの用意
        #pyxel.load("assets/img.pyxres")
        #初期設定
        self.x = x
        self.y = 15
        self.u =0
        self.v = 0
        self.w = 3
        self.h = 1
        
    def update(self,x,plus_x,time,speed):
        self.stop_time = time
        if self.stop_time < 80:
            self.y += 0
            self.x += 0
        else:
            self.y += 1*speed
            self.x += plus_x*speed

        if self.y >=48:
            self.u =u2
            self.v = v2
            self.w = w2
            self.h = h2
        if self.y >= 80:
            self.u =u3
            self.v = v3
            self.w = w3
            self.h = h3
        if self.y >= 120:
            self.x = x
            self.y = 45
            self.u =0
            self.v = 0
            self.w = 3
            self.h = 1

class Patterns:
    def __init__(self,time) :
        self.patterns = []
        self.pattern_count = len(l)
        for i in range(self.pattern_count):
            new_pattern = Pattern(l[i])
            new_pattern.y += m[i]
            if l[i] >= 80:
                plus_x = l[i]-80
            else:
                plus_x = -(80-l[i])
            new_pattern.update(l[i],plus_x*0.01,time,1)
            self.patterns.append(new_pattern)

    def update(self,time,speed):
        #模様
        self.pattern_count = len(self.patterns)
        for i in range(self.pattern_count):
            if l[i] >= 80:
                plus_x = l[i]-80
            else:
                plus_x = -(80-l[i])
            self.patterns[i].update(l[i],plus_x*0.01,time,speed)

    def draw(self):
        self.pattern_count = len(self.patterns)
        for i in range(self.pattern_count):
            pyxel.blt(self.patterns[i].x,
                    self.patterns[i].y,
                    0,
                    self.patterns[i].u,
                    self.patterns[i].v,
                    self.patterns[i].w,
                    self.patterns[i].h,
                    14)
       