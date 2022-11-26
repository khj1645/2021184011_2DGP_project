from pico2d import *
import main
import game_framework

image = None
logo = None
play_time = None
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(main)


def enter():
    global image, logo
    
    image = load_image('TitleImgFront1.png')
    logo = load_image('TitleText.png')
    pass

def exit():
    global image
    del image
    pass

def draw():
    global image, logo
    clear_canvas()
    image.clip_draw(0,0,720,1080,600,450,1200,900)
    logo.clip_draw(0,0,290,210,800,650,300,200)
    update_canvas()

def update():
    global play_time
    play_time = get_time()
    pass

def pause():
    pass

def resume():
    pass

