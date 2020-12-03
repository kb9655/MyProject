import gfw
from pico2d import *
import main_state

def enter():
    global image
    image = load_image('res/title.png')

def update():
    pass

def draw():
    center = get_canvas_width()//2, get_canvas_height() //2
    image.draw(*center)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_SPACE:
            gfw.push(main_state)

#    if e.type == SDL_QUIT:
#        gfw.quit()
#    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
#        gfw.quit()
#    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
#        gfw.push(main_state)
def exit():
    global image
    del image

def pause():
    pass
def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()
