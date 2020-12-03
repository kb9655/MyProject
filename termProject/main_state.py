import gfw
from pico2d import *
from player import Player
from bullet import LaserBullet
from score import Score
import gobj
import enemy_gen
import life_gauge
from background import HorzScrollBackground
from background import VertScrollBackground
import scoreboard
from enemy_boss import Boss

canvas_width = 500
canvas_height = 800

STATE_IN_GAME, STATE_GAME_OVER = range(2)


def enter():
    gfw.world.init(['bg', 'enemy', 'bullet','player', 'ui', 'bullet_enemy'])

    center = get_canvas_width() // 2, get_canvas_height() // 2

    #background
    speed_city = 10
    bg = VertScrollBackground('bg_city.png')
    bg.speed = speed_city
    gfw.world.add(gfw.layer.bg, bg)

    speed_clouds = 20
    bg = VertScrollBackground('clouds.png')
    bg.speed = speed_clouds
    gfw.world.add(gfw.layer.bg, bg)

    global player
    player = Player()
    #player.bg=bg
    
    gfw.world.add(gfw.layer.player, player)
    
    global boss
    boss = Boss()
    gfw.world.add(gfw.layer.enemy, boss)

    global score
    score = Score(canvas_width - 20, canvas_height - 50)
    gfw.world.add(gfw.layer.ui, score)

    global font
    font = gfw.font.load(gobj.RES_DIR + '/segoeprb.ttf', 40)

    life_gauge.load()

    global player_life

   
def check_enemy(e):
    #if gobj.collides_box(player, e):
    #    print('Player Collision', e)
    #    e.remove()
    #    return

    for b in gfw.gfw.world.objects_at(gfw.layer.bullet):
        if gobj.collides_box(b, e):
            # print('Collision', e, b)
            dead = e.decrease_life(b.power)
            if dead:
                score.score += e.level * 10
                e.remove()
            b.remove()
            return

def check_player(e):
    if gobj.collides_box(player, e):
        print('Player Collision', e)
        e.remove()
        player.decrease_life()
        #player.decrease_bomb()
        player.regen()
        return


def update():
    gfw.world.update()
    enemy_gen.update()

    for e in gfw.world.objects_at(gfw.layer.enemy):
        check_enemy(e)

    for e in gfw.world.objects_at(gfw.layer.bullet_enemy):
        check_player(e)

def draw():
    gfw.world.draw()
    gobj.draw_collision_box()#colision
    
def handle_event(e):
    global player
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            return gfw.pop()
        #if e.key == SDLK_SPACE:
        #     gfw.push(scoreboard)
    

    player.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
