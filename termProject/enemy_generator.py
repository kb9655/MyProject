import random
import gfw
from pico2d import *
from enemy import *
from enemy_boss import Boss

next_wave = 0
wave_idx = 0
enemy_gen_info ={}

def generate():
    global data, next_wave,wave_idx
    with open(('stage.json')) as f:
        data = json.load(f)
        for d in data:

            if d['type'] == 0:
                if d['t'] == wave_idx:
                    e = Boss()
                    gfw.world.add(gfw.layer.enemy, e)
            elif d['type'] == 1:
                if d['t'] == wave_idx:
                    e = Enemy1(d['x'], d['y'])
                    gfw.world.add(gfw.layer.enemy, e)
            elif d['type'] == 2:
                if d['t'] == wave_idx:
                    e = Enemy2(d['x'], d['y'])
                    gfw.world.add(gfw.layer.enemy, e)

            elif d['type'] == 3:
                if d['t'] == wave_idx:
                    e = Enemy3(d['x'], d['y'])
                    gfw.world.add(gfw.layer.enemy, e)

            elif d['type'] == 4:
                if d['t'] == wave_idx:
                    e = Enemy4(d['x'], d['y'])
                    gfw.world.add(gfw.layer.enemy, e)

            elif d['type'] == 5:
                if d['t'] == wave_idx:
                    e = Enemy5(d['x'], d['y'])
                    gfw.world.add(gfw.layer.enemy, e)



    next_wave = 1
    wave_idx += 1
    print(wave_idx)

def update():
    global next_wave
    next_wave -= gfw.delta_time
    if next_wave < 0:
        generate()
