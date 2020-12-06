import gfw
from pico2d import *
from player import Player
from bullet import LaserBullet
from score import Score
import pause_state
import gobj
import enemy_generator
import life_gauge
from background import HorzScrollBackground
from background import VertScrollBackground
from enemy_boss import Boss
from item import *
import random
import title_state


canvas_width = 500
canvas_height = 800  #720

STATE_IN_GAME, STATE_GAME_OVER, STATE_GAME_WIN = range(3)

ITEM_PROB_P = 30
ITEM_PROB_B = 10


def end_game():
    global state
    state = STATE_GAME_OVER
    music_bg.stop()


def enter():
    gfw.world.init(['bg', 'enemy', 'bullet','player', 'ui', 'bullet_enemy','item'])

    center = get_canvas_width() // 2, get_canvas_height() // 2

    #background
    speed_city = 20
    bg = VertScrollBackground('bg_city.png')
    bg.speed = speed_city
    gfw.world.add(gfw.layer.bg, bg)

    speed_clouds = 30
    bg = VertScrollBackground('clouds.png')
    bg.speed = speed_clouds
    gfw.world.add(gfw.layer.bg, bg)

    global player
    player = Player()
    #player.bg=bg
    
    gfw.world.add(gfw.layer.player, player)
    
    global boss

    global score
    score = Score(canvas_width - 20, canvas_height - 50)
    gfw.world.add(gfw.layer.ui, score)

    global font
    font = gfw.font.load(gobj.RES_DIR + '/segoeprb.ttf', 40)

    life_gauge.load()

    global music_bg, wav_item, wav_enemydead, wav_enemyhit, wav_playerhit, game_over_image
    music_bg = load_music('res/04.mp3')
    wav_item = load_wav('res/item.wav')
    wav_enemydead = load_wav('res/enemydead.wav')
    wav_enemyhit = load_wav('res/enemyhit.wav')
    wav_playerhit = load_wav('res/playerhit.wav')
    game_over_image = gfw.image.load('res/game_over.png')

    global player_life

    global item

    music_bg.repeat_play()

    global state
    state = STATE_IN_GAME

    

    #item = PowerUP(250,400)
    #gfw.world.add(gfw.layer.item, item)

   
def check_enemy(e):
    #if gobj.collides_box(player, e):
    #    print('Player Collision', e)
    #    e.remove()
    #    return

    for b in gfw.gfw.world.objects_at(gfw.layer.bullet):
        if gobj.collides_box(b, e):
            wav_enemyhit.play()
            # print('Collision', e, b)
            dead = e.decrease_life(b.power)
            if dead:
                wav_enemydead.play()
                score.score += e.score
                e.remove()
                if ITEM_PROB_P > random.randint(1,100):
                    item = PowerUP(e.x, e.y)
                    gfw.world.add(gfw.layer.item, item)

                #if ITEM_PROB_B > random.randint(1,100):
                #    itemb = BombUP(e.x, e.y)
                #    gfw.world.add(gfw.layer.item, itemb)
            b.remove()
            return

def check_player(e):
    if gobj.collides_box(player, e):
        wav_playerhit.play()
        e.remove()
        if player.decrease_life():
            player.reset_powerlevel()
            item = PowerUP(e.x, e.y)
            gfw.world.add(gfw.layer.item, item)
            player.regen()
        else:
            end_game()
        
        

def check_item(e):
    if gobj.collides_box(player, e):
        wav_item.play()
        e.remove()
        if player.increase_power():
            score.score += 100

def update():
    gfw.world.update()
    enemy_generator.update()

    for e in gfw.world.objects_at(gfw.layer.enemy):
        check_enemy(e)

    for e in gfw.world.objects_at(gfw.layer.bullet_enemy):
        check_player(e)

    for e in gfw.world.objects_at(gfw.layer.item):
        check_item(e)
        e.check_reflect()

def draw():
    gfw.world.draw()
    #gobj.draw_collision_box()#colision

    if state == STATE_GAME_OVER:
        center = get_canvas_width() // 2, get_canvas_height() * 2 // 3
        game_over_image.draw(*center)
    
def handle_event(e):
    global player, state
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            if state == STATE_GAME_OVER:
                gfw.change(title_state)
    
    
    player.handle_event(e)

def pause():
    pass

def resume():
    pass

def exit():
    global music_bg, wav_item
    del music_bg
    del wav_item


if __name__ == '__main__':
    gfw.run_main()
