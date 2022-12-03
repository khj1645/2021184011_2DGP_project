from pico2d import *
import main
import game_framework
import game_world
import character
import lobby
import attack

big_font = None
mid_font = None
small_font = None
sound = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_world.clear()
            sound.stop()
            game_framework.change_state(lobby)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.pop_state()



def enter():
    global big_font, mid_font, small_font, sound
    big_font = load_font('JejuHallasan.ttf', 100)
    mid_font = load_font('JejuHallasan.ttf', 50)
    small_font = load_font('JejuHallasan.ttf', 30)

    sound= load_music('AudioClip\\Sound_UI3.wav')
    sound.set_volume(20)
    sound.repeat_play()
    pass

def exit():
    global big_font, mid_font, small_font, sound
    del big_font
    del mid_font
    del small_font
    del sound
    pass

def draw():
    global big_font, mid_font, small_font
    clear_canvas()
    # main.draw()
    back = load_image('Sheet_AbilityCh.png')
    for game_object in game_world.all_objects():
        game_object.draw()
    back.clip_draw(0,0,220,300,600, 450, 1000, 800)
    big_font.draw(500, 770, f'Death', (255, 255, 255))
    mid_font.draw(150, 570, f'Time : {main.minute} : {main.second}', (255, 255, 255))
    mid_font.draw(150, 370, f'Level : {character.hero.lv}', (255, 255, 255))
    small_font.draw(150, 170, f'Esc to lobby', (255, 255, 255))
    #mid_font.draw(500, 770, f'Level : {character.hero.lv}', (255, 255, 255))

    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass

