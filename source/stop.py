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


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_world.clear()
            game_framework.change_state(lobby)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.pop_state()



def enter():
    global big_font, mid_font, small_font
    big_font = load_font('JejuHallasan.ttf', 44)
    mid_font = load_font('JejuHallasan.ttf', 32)
    small_font = load_font('JejuHallasan.ttf', 20)
    pass

def exit():
    pass

def draw():
    global big_font, mid_font, small_font
    clear_canvas()
    # main.draw()
    back = load_image('Sheet_AbilityCh.png')
    background.draw()
    enemy.draw()
    item.draw()
    character.draw()
    back.clip_draw(0,0,220,300,600, 450, 1000, 800)
    big_font.draw(500, 870, f'일시정지', (0, 0, 0))
    mid_font.draw(500, 770, f'Level : {character.hero.lv}', (255, 255, 255))
    mid_font.draw(500, 670, f'체력 : {character.hero.hp}/{character.hero_hp}', (255, 255, 255))
    mid_font.draw(500, 570, f'일반 공격 : {attack.normal_bullet_level} Level', (255, 255, 255))
    mid_font.draw(500, 470, f'화염구 : {attack.skill_q_level} Level', (255, 255, 255))
    mid_font.draw(500, 370, f'낙뢰 : {attack.skill_w_level} Level', (255, 255, 255))
    mid_font.draw(500, 270, f'전격 지대 : {attack.skill_e_level} Level', (255, 255, 255))
    mid_font.draw(500, 170, f'운석 낙하 : {attack.skill_r_level} Level', (255, 255, 255))

    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass

