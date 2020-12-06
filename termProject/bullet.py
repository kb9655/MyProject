from pico2d import *
import gfw
from gobj import *

class LaserBullet:
    SIZE = 20
    def __init__(self, x, y, speed):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = x, y
        self.dy = speed
        self.image = gfw.image.load(RES_DIR + '/bullet_single.png')
        self.power = 100
        

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y += self.dy * gfw.delta_time

        if self.y > get_canvas_height() + LaserBullet.SIZE:
            self.remove()

    def remove(self):
        gfw.world.remove(self)

    
    def get_bb(self):
        hw = self.image.w // 2
        hh = self.image.h // 2
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh


class LaserBullet_Digonal:
    SIZE = 40
    def __init__(self, x, y, speed, angle):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = x, y
        self.dx = 0
        self.dy = 0
        self.speed = speed
        self.image = gfw.image.load(RES_DIR + '/bullet_single.png')
        self.angle = angle
        self.distance = 0
        self.power = 100
        

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.distance = self.speed * gfw.delta_time
        self.dx = self.distance * math.cos(self.angle) 
        self.dy = self.distance * math.sin(self.angle)
        self.x += self.dx
        self.y += self.dy
       

        if self.y > get_canvas_height() + LaserBullet_Digonal.SIZE:
            self.remove()
        if self.x > get_canvas_width() + LaserBullet_Digonal.SIZE:
            self.remove()
        if self.x < 0 - LaserBullet_Digonal.SIZE:
            self.remove()

    def remove(self):
        gfw.world.remove(self)

    
    def get_bb(self):
        hw = self.image.w // 2
        hh = self.image.h // 2
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh



class ChargeShot:
    def __init__(self, x, y, speed):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = x, y
        self.dy = speed
        self.image = gfw.image.load(RES_DIR + '/chargeshot.png')
        self.power = 1500
        

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y += self.dy * gfw.delta_time

        if self.y > get_canvas_height() + LaserBullet.SIZE:
            self.remove()

    def remove(self):
        gfw.world.remove(self)


    def get_bb(self):
        hw = self.image.w // 2
        hh = self.image.h // 2
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh

class Bomb:
    def __init__(self):
        self.x, self.y = get_canvas_width()//2, get_canvas_height()//2
        self.power = 2000

    def draw(self):
        pass

    def update(self):
        pass

    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        hw = get_canvas_width()//2
        hh = get_canvas_height()//2
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh



    
