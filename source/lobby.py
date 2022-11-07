from pico2d import *
import main
import game_framework


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
    pass

def exit():
    pass

def draw():
    clear_canvas()
    image = load_image('TitleImgFront1.png')
    image.clip_draw(0,0,720,1080,600,450,1200,900)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass

