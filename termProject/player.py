import random
from pico2d import *
import gfw
from gobj import *
from bullet import *

MAX_LIFE = 3
MAX_BOMB = 3
MIN_BOMB = 0
MAX_POWERLEVEL = 2
PI = 3.141592

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

    KEYDOWN_z  = (SDL_KEYDOWN, SDLK_z)
    KEYDOWN_x = (SDL_KEYDOWN, SDLK_x)
    KEYUP_x   = (SDL_KEYUP,   SDLK_x)
    KEYDOWN_c  = (SDL_KEYDOWN, SDLK_c)


    #KEY_MAP_ATTACK = {
    #    (SDL_KEYUP, SDLK_x):       -1,
    #    (SDL_KEYDOWN, SDLK_x):     1,
    #}
  
    LASER_INTERVAL = 0.15
    SPARK_INTERVAL = 0.03
    IMAGE_RECTS = [
        (  8, 0, 42, 80),
        ( 76, 0, 42, 80),
        (140, 0, 50, 80),
        (205, 0, 56, 80),
        (270, 0, 62, 80),
        (334, 0, 70, 80),#중앙
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
        #플레이어 이동
        self.pos_start = 250, 80
        self.delta = 0, 0
        self.speed = 320
        self.pos = self.pos_start
        
        #이미지 로드
        self.image = gfw.image.load(RES_DIR + '/fighters.png')
        self.spark = gfw.image.load(RES_DIR + '/laser_0.png')
        self.heart_red = gfw.image.load('res/heart_red.png')
        self.heart_white = gfw.image.load('res/heart_white.png')
        self.explosion = gfw.image.load('res/explosion.jpg')
        self.image_bomb = gfw.image.load('res/bomb.png')
        self.image_bomb_clear = gfw.image.load('res/clear.png')
 
        self.life = MAX_LIFE
        self.bomb = 2

        self.src_rect = Player.IMAGE_RECTS[5]
        half = self.src_rect[2] // 2
        half_height = self.src_rect[3] // 2
        

        self.minx = half
        self.maxx = get_canvas_width() - half
        self.miny = half_height
        self.maxy = get_canvas_height() - half_height
        
        
        self.laser_time = 0
        self.roll_time = 0
        self.fireidx = 0

        self.check_attack = 0
        self.check_charge = 0

        self.powerlevel = 2

    def regen(self):
        self.pos = self.pos_start
        
    def decrease_life(self):
        self.life -= 1
        return self.life <= 0

    def decrease_bomb(self):
        if self.bomb <= 0:
            return
        else:
            self.bomb -= 1
        
    def increase_bomb(self):
        if self.bomb >= MAX_BOMB:
            return True
        self.bomb += 1
        return False


    def fire(self):
        pl=self.powerlevel
        self.laser_time = 0
        angle1 = 3.141592 * 70 / 360
        
        
        if pl == 0:
            bullet = LaserBullet(self.pos[0], self.pos[1] + Player.SPARK_OFFSET, 400)
            gfw.world.add(gfw.layer.bullet, bullet)
            # print('bullets = ', len(LaserBullet.bullets))
        elif pl == 1:
            bullet_1 = LaserBullet(self.pos[0] + 10, self.pos[1] + Player.SPARK_OFFSET, 400)
            gfw.world.add(gfw.layer.bullet, bullet_1)

            bullet_2 = LaserBullet(self.pos[0] -10, self.pos[1] + Player.SPARK_OFFSET, 400)
            gfw.world.add(gfw.layer.bullet, bullet_2)
            # print('bullets = ', len(LaserBullet.bullets))
        elif pl == 2:
            bullet_1 = LaserBullet(self.pos[0] + 10, self.pos[1] + Player.SPARK_OFFSET, 400)
            gfw.world.add(gfw.layer.bullet, bullet_1)

            bullet_2 = LaserBullet(self.pos[0] -10, self.pos[1] + Player.SPARK_OFFSET, 400)
            gfw.world.add(gfw.layer.bullet, bullet_2)

            bullet_3 = LaserBullet_Digonal(self.pos[0] + 15, self.pos[1] + Player.SPARK_OFFSET, 400, PI * 80/180)
            gfw.world.add(gfw.layer.bullet, bullet_3)

            bullet_4 = LaserBullet_Digonal(self.pos[0] -15, self.pos[1] + Player.SPARK_OFFSET, 400,PI * 100/180)
            gfw.world.add(gfw.layer.bullet, bullet_4)

    def draw(self):
        self.image.clip_draw(*self.src_rect, self.pos[0], self.pos[1])
        # if self.laser_time < Player.SPARK_INTERVAL:
        #     self.spark.draw(self.x, self.y + Player.SPARK_OFFSET)

        x_life,y_life = 0+30, get_canvas_height()-30
        for i in range(MAX_LIFE):
            heart = self.heart_red if i <self.life else self.heart_white
            heart.draw(x_life, y_life)
            x_life += heart.w

        x_bomb,y_bomb = 0+30, get_canvas_height()-y_life
        for i in range(MAX_BOMB):
            bomb = self.image_bomb if i <self.bomb else self.image_bomb_clear
            bomb.draw(x_bomb, y_bomb)
            x_bomb += bomb.w    

    def update(self):
        x,y = self.pos  
        dx,dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time
        
        x = clamp(self.minx, x, self.maxx)
        y = clamp(self.miny, y, self.maxy)
        
        self.pos= x,y
        POS=self.pos
        if self.check_attack == 1:
            self.check_charge += gfw.delta_time

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
        elif pair == Player.KEYDOWN_x:
            self.check_attack = 1
            self.fire()
    
        elif pair == Player.KEYUP_x:
             self.check_attack = 0
             print(self.check_charge)
             if self.check_charge > 1:
                 print("chargeshot")
             self.check_charge=0
                        
        elif pair == Player.KEYDOWN_z:
            #bomb = self.image_bomb if i <self.life else self.image_bomb_clear
            self.decrease_bomb()
            print("bomb")
            print(self.bomb)
        elif pair == Player.KEYDOWN_c:
            self.increase_bomb() 


        #elif pair_attack in Player.KEY_MAP_ATTACK:
        #    self.fireidx += Player.KEY_MAP_ATTACK[pair_attack]
        #    #print(self.fireidx)
        #elif self.fireidx > 0:
        #    self.fire()
        
    def get_bb(self):
        hw = self.src_rect[2] / 6
        hh = self.src_rect[3] / 6
        return self.pos[0] - hw, self.pos[1] - hh, self.pos[0] + hw, self.pos[1] + hh

    def out_pos(self):
        player_pos=self.pos

        return player_pos
        
    
if __name__ == "__main__":
    for (l,t,r,b) in Player.IMAGE_RECTS:
        l *= 2
        t *= 2
        r *= 2
        b *= 2
        l -= 1
        r += 2
        print('(%3d, %d, %d, %d),' % (l,t,r,b))
