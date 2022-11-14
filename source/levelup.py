from pico2d import *
import character
import enemy
import background
import game_framework
import item
import random
import attack
# 기본 공격, 스킬 4개, 이속, 체력, 공격력, 쿨타임
image_list = ['Ability1Portrait.png', 'Ability2Portrait.png', 'Ability7Portrait.png','Ability8Portrait.png',
              'Ability10Portrait.png','Ability31Portrait.png','Ability33Portrait.png','Ability34Portrait.png']
image_size = [[193, 225], [205, 250], [196, 265], [230, 243], [217, 245], [231, 217], [210, 210], [195, 231]]
image = None
image_index = None

def upgrade(n):
    if n == 0:
        attack.normal_bullet_damage = attack.normal_bullet_damage + attack.normal_bullet_damage / 10
        attack.normal_bullet_level += 1
        pass
    if n == 1:
        attack.skill_q_damage += attack.skill_q_damage / 10
        attack.skill_q_level += 1
        pass
    if n == 2:
        attack.skill_w_damage += attack.skill_w_damage / 10
        attack.skill_w_level += 1
        # attack.skill_w_damage = attack.skill_w_damage + 50
        
        pass
    if n == 3:
        attack.skill_e_damage += attack.skill_e_damage / 10
        attack.skill_e_level += 1
        pass
    if n == 4:
        pass
    if n == 5:
        pass
    if n == 6:
        pass
    if n == 7:
        pass  
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            upgrade(image_index[0])
            game_framework.pop_state()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            upgrade(image_index[1])
            game_framework.pop_state()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
            upgrade(image_index[2])
            game_framework.pop_state()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_4:
            upgrade(image_index[3])
            game_framework.pop_state()


def enter():
    global image, image_index
    image = []
    image_index = []
    rd = 0
    for i in range(4):
        while rd in image_index:
            rd = random.randint(0,7)   
        image_index.append(rd)
        image.append(load_image(image_list[image_index[i]]))
    # image = load_image('081_아이템창.png')
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
    for i in range(4):
        image[i].clip_draw(0,0,image_size[image_index[i]][0],image_size[image_index[i]][1],400,200 + 150 * (i),100,100)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass

