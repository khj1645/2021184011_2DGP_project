from pico2d import *
import character
import enemy
import background
import game_framework
import item

image = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.pop_state()


def enter():
    global image
    image = load_image('081_아이템창.png')
    pass

def exit():
    pass

def draw():
    global image
    clear_canvas()
    # main.draw()
    background.draw()
    enemy.draw()
    item.draw()
    character.draw()
    image.clip_draw(0,0,922,2048,600,450,400,800)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass

