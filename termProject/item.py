from pico2d import *
import gfw
from gobj import *


MAX_REFLECT = 5

class PowerUP:
    def __init__(self, x, y):
        self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = x, y
        self.image = gfw.image.load(RES_DIR + '/poweritem.png')
        self.fps = 6
        self.time = get_time()
        self.fcount = self.image.h // self.image.w
        self.dx=50
        self.dy=50
        self.score = 100
        self.maxx = get_canvas_width()
        self.minx = 0
        self.maxy = get_canvas_height()
        self.miny = 0
        self.speed = 2
        self.reflect = 0

 
    def draw(self):
        src_size_height = 31
        src_size_width = 41
        dst_size_height = 31
        dst_size_width = 41

        elapsed = get_time() - self.time
        self.fidx = round(elapsed * self.fps) % self.fcount
        self.image.clip_draw(0, src_size_height * self.fidx, src_size_width, src_size_height, self.x, self.y, dst_size_width, dst_size_width)
        

    def update(self):
        if self.x > self.maxx or self.x < self.minx:
            self.dx *= -1
            self.reflect += 1

        if self.y > self.maxy or self.y < self.miny:
            self.dy *= -1
            self.reflect += 1

        self.x += self.dx * gfw.delta_time * self.speed
        self.y += self.dy * gfw.delta_time * self.speed
        
        self.fidx = gfw.delta_time % self.fps

    def check_reflect(self):
        if self.reflect > MAX_REFLECT:
            self.remove()
        
        
    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        hw = 31
        hh = 21
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh

class BombUP:
    def __init__(self, x, y):
        self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = x, y
        self.image = gfw.image.load(RES_DIR + '/bombicon.png')
        self.dx=50
        self.dy=50
        self.score = 100
        self.maxx = get_canvas_width()
        self.minx = 0
        self.maxy = get_canvas_height()
        self.miny = 0
        self.speed = 2
        self.reflect = 0

 
    def draw(self):
        src_size_height = 33
        src_size_width = 39
        self.image.draw(self.x, self.y)
        

    def update(self):
        if self.x > self.maxx or self.x < self.minx:
            self.dx *= -1
            self.reflect += 1

        if self.y > self.maxy or self.y < self.miny:
            self.dy *= -1
            self.reflect += 1

        self.x += self.dx * gfw.delta_time * self.speed
        self.y += self.dy * gfw.delta_time * self.speed

    def check_reflect(self):
        if self.reflect > MAX_REFLECT:
            self.remove()
        
    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        hw = 32
        hh = 39
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh


