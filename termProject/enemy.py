from pico2d import *
import gfw
from gobj import *
import life_gauge
from bullet_enemy import *
from player import Player

class Enemy1:
    SIZE = 58
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.dx, self.dy = 0, -150
        self.max_life = 100
        self.life = self.max_life
        self.image = gfw.image.load(RES_DIR + '/enemy2.png')
        self.fidx = 0
        self.src_width = self.image.w // 8
        self.src_height = self.image.h
        self.time = 0
        self.fire_time = 0
        self.fire_interval = 1.5
        self.score = 10
        
    def draw(self):
        self.image.draw(self.x, self.y)
        gy = self.y - Enemy2.SIZE // 2
        rate = self.life / self.max_life
        life_gauge.draw(self.x, gy, Enemy2.SIZE - 10, rate)

    def update(self):
        self.y += self.dy * gfw.delta_time

        if self.y < -Enemy2.SIZE:
            self.remove()

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

    def set_target(self, target):
        self.target = target
        

    def fire(self):
        self.fire_time = 0
        bullet_enemy = Bullet_enemy_1(self.x, self.y, 300)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy)


    def get_bb(self):
        half = Enemy2.SIZE // 2 - 5
        return self.x - half, self.y - half, self.x + half, self.y + half

class Enemy2:
    SIZE = 58
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.dx, self.dy = 0, -100
        self.max_life = 500
        self.life = self.max_life
        self.image = gfw.image.load(RES_DIR + '/enemy1.png')
        self.fidx = 0
        self.src_width = self.image.w // 8
        self.src_height = self.image.h
        self.time = 0
        self.fire_time = 0
        self.fire_interval = 2.0
        self.score = 10
        
    def draw(self):
        self.image.draw(self.x, self.y)
        gy = self.y - Enemy2.SIZE // 2
        rate = self.life / self.max_life
        life_gauge.draw(self.x, gy, Enemy2.SIZE - 10, rate)

    def update(self):
        self.y += self.dy * gfw.delta_time

        if self.y < -Enemy2.SIZE:
            self.remove()

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

    def set_target(self, target):
        self.target = target
        

    def fire(self):
        self.fire_time = 0
        bullet_enemy = Bullet_enemy_3(self.x, self.y, 200)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy)


    def get_bb(self):
        half = Enemy2.SIZE // 2 - 5
        return self.x - half, self.y - half, self.x + half, self.y + half

class Enemy3:
    SIZE = 58
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.dx, self.dy = -100, 30
        self.max_life = 1500
        self.life = self.max_life
        self.image = gfw.image.load(RES_DIR + '/enemy3.png')
        self.fidx = 0
        self.src_width = self.image.w // 8
        self.src_height = self.image.h
        self.time = 0
        self.fire_time = 0
        self.fire_interval = 1.0
        self.score = 10
        
    def draw(self):
        self.image.draw(self.x, self.y)
        gy = self.y - Enemy2.SIZE // 2
        rate = self.life / self.max_life
        life_gauge.draw(self.x, gy, Enemy2.SIZE - 10, rate)

    def update(self):
        if self.x < 150:
            self.dx = 0
            self.dy = 50
        self.x += self.dx * gfw.delta_time
        self.y += self.dy * gfw.delta_time

        

        if self.y < -Enemy2.SIZE:
            self.remove()

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

    def set_target(self, target):
        self.target = target
        

    def fire(self):
        self.fire_time = 0
        bullet_enemy3 = Bullet_enemy_3(self.x, self.y, 400)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy3)


    def get_bb(self):
        half = Enemy2.SIZE // 2 - 5
        return self.x - half, self.y - half, self.x + half, self.y + half

class Enemy4:
    SIZE = 58
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.dx, self.dy = 0, -20
        self.max_life = 1000
        self.life = self.max_life
        self.image = gfw.image.load(RES_DIR + '/eg1.png')
        self.fidx = 0
        self.src_width = self.image.w // 8
        self.src_height = self.image.h
        self.time = 0
        self.fire_time = 0
        self.fire_interval = 2.0
        self.score = 10
        
    def draw(self):
        self.image.draw(self.x, self.y)
        gy = self.y - Enemy2.SIZE // 2
        rate = self.life / self.max_life
        life_gauge.draw(self.x, gy, Enemy2.SIZE - 10, rate)

    def update(self):
        self.y += self.dy * gfw.delta_time

        if self.y < -Enemy2.SIZE:
            self.remove()

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

    def set_target(self, target):
        self.target = target
        

    def fire(self):
        self.fire_time = 0
        bullet_enemy = Bullet_enemy_3(self.x, self.y, 200)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy)


    def get_bb(self):
        half = Enemy2.SIZE // 2 - 5
        return self.x - half, self.y - half, self.x + half, self.y + half

class Enemy5:
    SIZE = 58
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.dx, self.dy = 0, -20
        self.max_life = 300
        self.life = self.max_life
        self.image = gfw.image.load(RES_DIR + '/eg2.png')
        self.fidx = 0
        self.src_width = self.image.w // 8
        self.src_height = self.image.h
        self.time = 0
        self.fire_time = 0
        self.fire_interval = 1.0
        self.score = 10
        
    def draw(self):
        self.image.draw(self.x, self.y)
        gy = self.y - Enemy2.SIZE // 2
        rate = self.life / self.max_life
        life_gauge.draw(self.x, gy, Enemy2.SIZE - 10, rate)

    def update(self):
        self.y += self.dy * gfw.delta_time

        if self.y < -Enemy2.SIZE:
            self.remove()

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

    def set_target(self, target):
        self.target = target
        

    def fire(self):
        self.fire_time = 0
        bullet_enemy = Bullet_enemy_1(self.x+10, self.y, 400)
        bullet_enemy = Bullet_enemy_1(self.x-10, self.y, 400)
        gfw.world.add(gfw.layer.bullet_enemy, bullet_enemy)


    def get_bb(self):
        half = Enemy2.SIZE // 2 - 5
        return self.x - half, self.y - half, self.x + half, self.y + half


