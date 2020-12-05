from pico2d import *
import gfw
from gobj import *
import life_gauge
from bullet_enemy import *

PI=3.14

class Boss:
    SIZE = 96
    def __init__(self):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = 250, get_canvas_height() - Boss.SIZE
        self.dx, self.dy = 50, 0
        self.level = 10
        self.max_life = 1000
        self.life = self.max_life
        self.image = gfw.image.load(RES_DIR + '/boss.png')
        self.fidx = 0
        self.src_width = self.image.w #//8
        self.src_height = self.image.h
        self.time = 0

        #self.half=image
        self.minx = 0
        self.maxx = get_canvas_width()

        self.fire_time = 0

        self.fire_interval = 1.0

    def draw(self):
        self.image.draw(self.x, self.y)
        
        #rate = self.life / self.max_life
        #life_gauge.draw(self.x, gy, Boss.SIZE - 10, rate)

    def update(self):
        self.time += gfw.delta_time
        self.fidx = int(self.time * 10 + 0.5) % 8        
        if self.x > self.maxx:
            self.dx *= -1
        elif self.x < self.minx:
            self.dx *= -1
        self.x += self.dx * gfw.delta_time
        self.y += self.dy * gfw.delta_time

        #if self.y < -Boss.SIZE:
        #    self.remove()

        self.fire_time += gfw.delta_time

        if self.fire_time >= self.fire_interval:
            self.fire()
       
    def remove(self):
        gfw.world.remove(self)

    def decrease_life(self, amount):
        self.life -= amount
        return self.life <= 0

    def score(self):
        return self.max_life

    def fire(self):
        self.fire_time = 0
        bullet_enemy1 = Bullet_enemy_2(self.x, self.y, 400, 5/6*PI*2)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy1)
        
        bullet_enemy2 = Bullet_enemy_2(self.x, self.y, 400, 4/6*PI*2)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy2)
        
        bullet_enemy2 = Bullet_enemy_2(self.x, self.y, 400, 4.5/6*PI*2)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy2)
        

    def get_bb(self):
        half = Boss.SIZE // 2 - 5
        return self.x - half, self.y - half, self.x + half, self.y + half
