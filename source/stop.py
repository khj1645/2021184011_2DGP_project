from pico2d import *
import character
import enemy
import background
import game_framework
import game_world
import item
import lobby
import attack

big_font = None
mid_font = None
small_font = None
resume_image = None
exit_image = None


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            x, y = event.x, 900 - 1 - event.y
            if(x >= 1120 and x <= 1200 and y >= 820 and y <= 900):
                game_framework.pop_state()
            elif x >= 1010 and x <= 1090 and y >= 820 and y <= 900:
                game_world.clear()
                game_framework.change_state(lobby)
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_state()



def enter():
    global big_font, mid_font, small_font, resume_image, exit_image
    big_font = load_font('JejuHallasan.ttf', 44)
    mid_font = load_font('JejuHallasan.ttf', 32)
    small_font = load_font('JejuHallasan.ttf', 20)
    resume_image = load_image('UI_AreaMove_R.png')
    exit_image = load_image('UI_Exit.png')
    pass

def exit():
    global big_font, mid_font, small_font
    del big_font
    del mid_font
    del small_font
    pass

def draw():
    global big_font, mid_font, small_font, resume_image, exit_image
    clear_canvas()
    # main.draw()
    back = load_image('Sheet_AbilityCh.png')
    for game_object in game_world.all_objects():
        game_object.draw()
    back.clip_draw(0,0,220,300,600, 450, 600, 800)
    big_font.draw(500, 870, f'일시정지', (0, 0, 0))
    mid_font.draw(500, 770, f'Level : {character.hero.lv}', (255, 255, 255))
    mid_font.draw(500, 670, f'체력 : {character.hero.hp}/{character.hero_hp}', (255, 255, 255))
    mid_font.draw(500, 570, f'일반 공격 : {attack.normal_bullet_level} Level', (255, 255, 255))
    mid_font.draw(500, 470, f'화염구 : {attack.skill_q_level} Level', (255, 255, 255))
    mid_font.draw(500, 370, f'낙뢰 : {attack.skill_w_level} Level', (255, 255, 255))
    mid_font.draw(500, 270, f'전격 지대 : {attack.skill_e_level} Level', (255, 255, 255))
    mid_font.draw(500, 170, f'운석 낙하 : {attack.skill_r_level} Level', (255, 255, 255))

    resume_image.clip_draw(0, 0, 38, 48, 1160, 860, 80, 80)
    small_font.draw(1120, 810, f'resume', (0, 0, 0))
    exit_image.clip_draw(0, 0, 65, 65, 1050, 860, 80, 80)
    small_font.draw(1030, 810, f'exit', (0, 0, 0))

    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass

