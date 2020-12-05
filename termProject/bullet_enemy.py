from pico2d import *
import gfw
from gobj import *


class Bullet_enemy_1:
    SIZE = 40
    def __init__(self, x, y, speed):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = x, y
        self.dy = speed
        self.image = gfw.image.load(RES_DIR +'/bullet_round.png')
        self.power = 100
        

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= self.dy * gfw.delta_time

        if self.y > get_canvas_height() + Bullet_enemy_1.SIZE:
            self.remove()

    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        hw = self.image.w // 2
        hh = self.image.h // 2
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh


class Bullet_enemy_2:
    SIZE = 40
    def __init__(self, x, y, speed, angle):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = x, y
        self.speed = speed
        self.angle = angle
        self.image = gfw.image.load(RES_DIR +'/bullet_round.png')
        self.power = 100
        self.distance = 0
        self.dx = 0
        self.dy = 0
        

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.distance = self.speed * gfw.delta_time
        self.dx = self.distance * math.cos(self.angle) 
        self.dy = self.distance * math.sin(self.angle)
        self.x += self.dx
        self.y += self.dy
       

        if self.y > get_canvas_height() + Bullet_enemy_2.SIZE:
            self.remove()
        if self.x > get_canvas_width() + Bullet_enemy_2.SIZE:
            self.remove()
        if self.x < 0 - Bullet_enemy_2.SIZE:
            self.remove()

    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        hw = self.image.w // 2
        hh = self.image.h // 2
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh

class Bullet_enemy_3:
    SIZE = 40
    def __init__(self, x, y, speed):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = x, y
        self.speed = speed
        self.image = gfw.image.load(RES_DIR +'/bullet_round.png')
        self.power = 100
        self.distance = 0
        self.target = 0,0
        self.dx = 0
        self.dy = 0
        self.angle = 0
        self.set_target()

    def draw(self):
        self.image.draw(self.x, self.y)
    
    def update(self):
        self.distance = self.speed * gfw.delta_time
        self.dx = self.distance * math.cos(self.angle) 
        self.dy = self.distance * math.sin(self.angle)
        self.x += self.dx
        self.y += self.dy
        if self.y > get_canvas_height() + Bullet_enemy_2.SIZE:
            self.remove()
        if self.x > get_canvas_width() + Bullet_enemy_2.SIZE:
            self.remove()


    def set_target(self):
        for e in gfw.world.objects_at(gfw.layer.player):
            self.target = e.pos
            self.angle =  math.atan2(self.target[1]-self.y,self.target[0]-self.x)
               
    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        hw = self.image.w // 2
        hh = self.image.h // 2
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh
