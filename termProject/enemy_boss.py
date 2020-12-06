from pico2d import *
import gfw
from gobj import *
import life_gauge
from bullet_enemy import *

PI=3.14
SIZE_W = 515
SIZE_H = 164

class Boss:

    def __init__(self):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = 250, get_canvas_height() + SIZE_H//2
        self.dx, self.dy = 100, -50
        self.level = 10
        self.max_life = 20000
        self.life = self.max_life
        self.image = gfw.image.load(RES_DIR + '/boss.png')
        self.fidx = 0

        self.src_width = self.image.w #//8
        self.src_height = self.image.h
        self.time = 0
        self.score = 100

        #self.half=image
        self.minx = 0
        self.maxx = get_canvas_width()

        self.fire_time = 0
        self.fire_time_r = 0
        self.fire_time_l = 0.75

        self.fire_interval = 2.0
        self.fire_interval_l = 1.5
        self.fire_interval_r = 1.5

    def draw(self):
        self.image.draw(self.x, self.y)
        
        #rate = self.life / self.max_life
        #life_gauge.draw(self.x, gy, Boss.SIZE - 10, rate)

    def update(self):
        self.time += gfw.delta_time

        if self.y < get_canvas_height() - SIZE_H//2:
            self.dy = 0

        if self.x > self.maxx-100:
            self.x = self.maxx-100
            self.dx *= -1

        elif self.x < self.minx+100:
            self.x = self.minx+100
            self.dx *= -1

        self.x += self.dx * gfw.delta_time
        self.y += self.dy * gfw.delta_time
        

        #if self.y < -Boss.SIZE:
        #    self.remove()

        self.fire_time += gfw.delta_time
        self.fire_time_l += gfw.delta_time
        self.fire_time_r += gfw.delta_time

        if self.fire_time >= self.fire_interval:
            self.fire_middle()
            self.fire_roundshape()

        if self.fire_time_l >= self.fire_interval_l:
            self.fire_left()

        if self.fire_time_r >= self.fire_interval_r:   
            self.fire_right()
            
    def remove(self):
        gfw.world.remove(self)

    def decrease_life(self, amount):
        self.life -= amount
        return self.life <= 0

    def fire_left(self):
        self.fire_time_l = 0
        bullet_enemy1 = Bullet_enemy_2(self.x-100, self.y, 200, 5/6*PI*2)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy1)
        
        bullet_enemy2 = Bullet_enemy_2(self.x-100, self.y, 200, 4/6*PI*2)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy2)
        
        bullet_enemy3 = Bullet_enemy_2(self.x-100, self.y, 200, 4.5/6*PI*2)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy3)

    def fire_right(self):
        self.fire_time_r = 0
        bullet_enemy1 = Bullet_enemy_2(self.x+100, self.y, 200, 5/6*PI*2)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy1)
        
        bullet_enemy2 = Bullet_enemy_2(self.x+100, self.y, 200, 4/6*PI*2)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy2)
        
        bullet_enemy3 = Bullet_enemy_2(self.x+100, self.y, 200, 4.5/6*PI*2)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy3)

    def fire_middle(self):
        self.fire_time = 0
        bullet_enemy3 = Bullet_enemy_3(self.x, self.y, 400)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy3)

    def fire_roundshape(self):
        self.fire_time = 0
        bullet_enemy1 = Bullet_enemy_2(self.x, self.y, 300, 1/8*PI*2)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy1)
        bullet_enemy2 = Bullet_enemy_2(self.x, self.y, 300, 2/8*PI*2)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy2)
        bullet_enemy3 = Bullet_enemy_2(self.x, self.y, 300, 3/8*PI*2)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy3)
        bullet_enemy4 = Bullet_enemy_2(self.x, self.y, 300, 4/8*PI*2)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy4)
        bullet_enemy5 = Bullet_enemy_2(self.x, self.y, 300, 5/8*PI*2)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy5)
        bullet_enemy6 = Bullet_enemy_2(self.x, self.y, 300, 6/8*PI*2)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy6)
        bullet_enemy7 = Bullet_enemy_2(self.x, self.y, 300, 7/8*PI*2)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy7)
        bullet_enemy8 = Bullet_enemy_2(self.x, self.y, 300, 8/8*PI*2)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy8)
     
        

    def get_bb(self):
        half_w = SIZE_W//2
        half_h = SIZE_H//2
        return self.x - half_w, self.y - half_h, self.x + half_w, self.y + half_h
