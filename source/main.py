from pico2d import *
import character
import background
import enemy
import game_framework
import lobby
import item
running = None
font = None
play_time = None
minute = None
second = None
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(lobby)
        else:
            character.handle_events(event)


def enter():
    global running, font, minute, second
    running = True
    font = load_font('ENCR10B.TTF', 16)
    minute, second = 0, 0
    character.enter()
    background.enter()
    enemy.enter()
    item.enter()

def exit():
    pass

def draw():
    global minute, second
    clear_canvas()
    background.draw()
    enemy.draw()
    item.draw()
    character.draw()
    font.draw(600, 450, f'{minute} : {second}', (0, 0, 0))
    update_canvas()

def update():
    global play_time, minute, second
    play_time = get_time() - lobby.play_time
    minute = int(play_time // 60)
    second = int(play_time % 60)
    background.update()
    character.update()
    enemy.update()
    item.update()
    # delay(0.016)

def pause():
    pass

def resume():
    pass
