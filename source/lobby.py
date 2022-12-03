from pico2d import *
import main
import game_framework

image = None
logo = None
play_time = None
sound = None
font = None
def handle_events():
    global sound
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            sound.stop()
            game_framework.change_state(main)


def enter():
    global image, logo, sound, font
    
    image = load_image('TitleImgFront1.png')
    logo = load_image('TitleText.png')
    font = load_font('JejuHallasan.ttf', 44)
    sound= load_music('AudioClip\\Sound_BGM10.wav')
    sound.set_volume(20)
    sound.repeat_play()
    pass

def exit():
    global image, sound, logo, font
    del image
    del sound
    del logo
    del font
    pass

def draw():
    global image, logo, font
    clear_canvas()
    image.clip_draw(0,0,720,1080,600,450,1200,900)
    logo.clip_draw(0,0,290,210,800,650,300,200)
    font.draw(500, 300, f'Space key to start', (255, 255, 255))
    update_canvas()

def update():
    global play_time
    play_time = get_time()
    pass

def pause():
    pass

def resume():
    pass

