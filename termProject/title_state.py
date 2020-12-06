import gfw
from pico2d import *
import select_state

def enter():
    global image, words, WORDIDX, words_time, music_bg,wav_select
    image = load_image('res/title.png')
    words = load_image('res/title2.png')
    music_bg = load_music('res/02.mp3')
    wav_select = load_wav('res/menuselect.wav')
    words_time = 1
    WORDIDX=1

    music_bg.repeat_play()

def update():
    global WORDIDX, words_time
    words_time -= gfw.delta_time
    if words_time <= 0:
        WORDIDX *= -1
        words_time = 2

def draw():
    center = get_canvas_width()//2, get_canvas_height() //2
    image.draw(*center)

    if WORDIDX == 1:
        words.draw(250, 200)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_x:
            wav_select.play()
            gfw.push(select_state)
            

#    if e.type == SDL_QUIT:
#        gfw.quit()
#    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
#        gfw.quit()
#    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
#        gfw.push(main_state)
def exit():
    global image, music_bg, wav_select
    del image
    del music_bg
    del wav_select
 
def pause():
    pass
def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()
