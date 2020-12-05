from pico2d import *
import gfw
from gobj import *

MOVE_PPS = 120

class PowerUP:
    
    SIZE = 40
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

        if self.y > self.maxy or self.y < self.miny:
            self.dy *= -1

        self.x += self.dx * gfw.delta_time
        self.y += self.dy * gfw.delta_time
        
        self.fidx = gfw.delta_time % self.fps
        
    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        hw = 31
        hh = 21
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh

