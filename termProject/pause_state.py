import gfw
from pico2d import *

def enter():
    global image
    image = load_image('res/pause.png')

def update():
    pass
    #gfw.world.update()

def draw():
    center = get_canvas_width()//2, get_canvas_height() //2
    image.draw(*center)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

def pause():
    pass

def exit():
    pass

def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()
