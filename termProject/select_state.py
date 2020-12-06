import gfw
from pico2d import *
import main_state

def enter():
    global image, wav_entermain
    image = load_image('res/selectbg.png')
    wav_entermain = load_wav('res/entermain.wav')

def update():
    pass
def draw():
    global right, y, tcount, display, digit_width, digit
    center = get_canvas_width()//2, get_canvas_height() //2
    image.draw(*center)


def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_x:
            wav_entermain.play()
            gfw.push(main_state)
    
def exit():
    global image, wav_entermain
    del image
    del wav_entermain

def pause():
    pass
def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()
