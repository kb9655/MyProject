import random
from pico2d import *
import gfw
from gobj import *
from bullet import *

class Player:
    KEY_MAP_MOVE = {
        (SDL_KEYDOWN, SDLK_LEFT):  (-1,  0),
        (SDL_KEYDOWN, SDLK_RIGHT): ( 1,  0),
        (SDL_KEYDOWN, SDLK_DOWN):  ( 0, -1),
        (SDL_KEYDOWN, SDLK_UP):    ( 0,  1),
        (SDL_KEYUP, SDLK_LEFT):    ( 1,  0),
        (SDL_KEYUP, SDLK_RIGHT):   (-1,  0),
        (SDL_KEYUP, SDLK_DOWN):    ( 0,  1),
        (SDL_KEYUP, SDLK_UP):      ( 0, -1),
    }

    KEY_MAP_ATTACK = {
        (SDL_KEYUP, SDLK_x):       -1,
        (SDL_KEYDOWN, SDLK_x):     1,
    }
    
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
  
    LASER_INTERVAL = 0.15
    SPARK_INTERVAL = 0.03
    IMAGE_RECTS = [
        (  8, 0, 42, 80),
        ( 76, 0, 42, 80),
        (140, 0, 50, 80),
        (205, 0, 56, 80),
        (270, 0, 62, 80),
        (334, 0, 70, 80),
        (406, 0, 62, 80),
        (477, 0, 56, 80),
        (549, 0, 48, 80),
        (621, 0, 42, 80),
        (689, 0, 42, 80),
    ]
    MAX_ROLL = 0.4
    SPARK_OFFSET = 28

    #constructor
    def __init__(self):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.pos = 250, 80
        self.delta = 0, 0
        self.speed = 320
        self.image = gfw.image.load(RES_DIR + '/fighters.png')
        self.spark = gfw.image.load(RES_DIR + '/laser_0.png')
        self.src_rect = Player.IMAGE_RECTS[5]
        half = self.src_rect[2] // 2
        self.minx = half
        self.maxx = get_canvas_width() - half
        self.laser_time = 0
        self.roll_time = 0
        self.fireidx = 0


    def fire(self):
        self.laser_time = 0
        bullet = LaserBullet(self.pos[0], self.pos[1] + Player.SPARK_OFFSET, 400)
        gfw.world.add(gfw.layer.bullet, bullet)
        # print('bullets = ', len(LaserBullet.bullets))

    def draw(self):
        self.image.clip_draw(*self.src_rect, self.pos[0], self.pos[1])
        # if self.laser_time < Player.SPARK_INTERVAL:
        #     self.spark.draw(self.x, self.y + Player.SPARK_OFFSET)

    def update(self):
        x,y = self.pos  
        dx,dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time
        x = clamp(self.minx, x, self.maxx)
        self.pos= x,y

        #self.pos[0] += self.delta[0] * self.speed * gfw.delta_time
        #self.pos[1] += self.delta[1] * self.speed * gfw.delta_time

        self.laser_time += gfw.delta_time        
        self.update_roll()

        
        #if self.laser_time >= Player.LASER_INTERVAL:
        #    self.fire()     #발사

    def update_roll(self):
        dx = self.delta[0]
        if dx == 0:
            if self.roll_time > 0:
                dx = -1
            elif self.roll_time < 0:
                dx = 1
        self.roll_time += dx * gfw.delta_time
        if self.pos[0] == 0:
            if dx < 0 and self.roll_time < 0:
                self.roll_time = 0
            if dx > 0 and self.roll_time > 0:
                self.roll_time = 0

        self.roll_time = clamp(-Player.MAX_ROLL, self.roll_time, Player.MAX_ROLL)

        # if self.roll_time
        roll = int(self.roll_time * 5 / Player.MAX_ROLL)
        self.src_rect = Player.IMAGE_RECTS[roll + 5]

        # if self.src_rect != self.prev_rect:
        #     print(roll, self.src_rect)
        #     self.prev_rect = self.src_rect

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP_MOVE:
            #self.dx += Player.KEY_MAP[pair]
            self.delta = point_add(self.delta, Player.KEY_MAP_MOVE[pair])

        pair_attack =(e.type, e.key)
        if pair_attack in Player.KEY_MAP_ATTACK:
            self.fireidx += Player.KEY_MAP_ATTACK[pair_attack]
            print(self.fireidx)
        if self.fireidx > 0:
            self.fire()
        
    def get_bb(self):
        hw = self.src_rect[2] / 2
        hh = self.src_rect[3] / 2
        return self.pos[0] - hw, self.pos[1] - hh, self.pos[0] + hw, self.pos[1] + hh

if __name__ == "__main__":
    for (l,t,r,b) in Player.IMAGE_RECTS:
        l *= 2
        t *= 2
        r *= 2
        b *= 2
        l -= 1
        r += 2
        print('(%3d, %d, %d, %d),' % (l,t,r,b))
