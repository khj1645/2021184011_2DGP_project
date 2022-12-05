from pico2d import *
import character
import game_framework
import random
import attack
import game_world
# 기본 공격, 스킬 4개, 이속, 체력, 공격력, 쿨타임
image_list = ['Ability1Portrait.png', 'Ability2Portrait.png', 'Ability7Portrait.png','Ability8Portrait.png',
              'Ability10Portrait.png','Ability31Portrait.png','Ability33Portrait.png','Ability34Portrait.png']
image_size = [[193, 225], [205, 250], [196, 265], [230, 243], [217, 245], [231, 217], [210, 210], [195, 231]]
skill_name = ['마력탄', '화염구', '낙뢰','감전지대',
              '운석 낙하','지능','생명력','가속']
index_list = None
image = None
image_index = None
big_font, mid_font, small_font = None, None, None
def upgrade(n):
    if n == 0:
        attack.normal_bullet_damage += attack.normal_bullet_damage / 20
        attack.normal_bullet_level += 1
        print("평타 업글")
        pass
    if n == 1:
        if attack.skill_q_level % 2 != 0:
            attack.skill_q_damage += attack.skill_q_damage / 20
        else:
            character.skill_q_coll_time = character.skill_q_coll_time - character.skill_q_coll_time / 10
        attack.skill_q_level += 1
        print("q 업글")
        pass
    if n == 2:
        if attack.skill_w_level % 2 != 0:
            attack.skill_w_damage += attack.skill_w_damage / 20
            attack.skill_w_level += 1
        else:
            character.skill_w_coll_time = character.skill_w_coll_time - character.skill_w_coll_time / 10
        print("w 업글")
        # attack.skill_w_damage = attack.skill_w_damage + 50
        
        pass
    if n == 3:
        attack.skill_e_damage += attack.skill_e_damage / 20
        attack.skill_e_level += 1
        print("e 업글")
        pass
    if n == 4:
        if attack.skill_r_level % 2 != 0:
            attack.skill_r_damage += attack.skill_r_damage / 20
            attack.skill_r_level += 1
        else:
            character.skill_r_cool_time = character.skill_r_cool_time - character.skill_r_cool_time / 10
        print("r 업글")
        pass
    if n == 5:
        character.int_level += 1
        attack.skill_q_damage += attack.skill_q_damage / 5
        attack.skill_w_damage += attack.skill_w_damage / 5
        attack.skill_e_damage += attack.skill_e_damage / 5
        attack.skill_r_damage += attack.skill_r_damage / 5
        print("능지 업글")
        pass
    if n == 6:
        character.hp_level += 1
        character.hero.hp += 20
        print("hp 업글")
        pass
    if n == 7:
        character.speed_level += 1
        character.speed += 1
        print("가속 업글")
        pass
    print(attack.normal_bullet_damage)
    print(attack.skill_q_damage)
    print(attack.skill_w_damage)
    print(attack.skill_e_damage)
    print(attack.skill_r_damage)
    enter()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            upgrade(image_index[2])
            game_framework.pop_state()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            upgrade(image_index[1])
            game_framework.pop_state()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
            upgrade(image_index[0])
            game_framework.pop_state()


def enter():
    global image, image_index, big_font, mid_font, small_font, index_list
    big_font = load_font('JejuHallasan.ttf', 44)
    mid_font = load_font('JejuHallasan.ttf', 32)
    small_font = load_font('JejuHallasan.ttf', 20)
    image = []
    image_index = []
    index_list = []
    rd = 0
    for i in range(3):
        while rd in image_index:
            rd = random.randint(0,7)
        index_list.append(rd)
        image_index.append(rd)
        image.append(load_image(image_list[image_index[i]]))
    # image = load_image('081_아이템창.png')
    pass

def exit():
    global image, image_index, big_font, mid_font, small_font, index_list
    pass

def draw():
    global image, big_font, mid_font, small_font, index_list
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    big_font.draw(500, 850, f'Level : {character.hero.lv}', (0, 255, 0))
    back = load_image('Sheet_AbilityCh.png')
    for i in range(3):
        back.clip_draw(0,0,220,300,600,250 * i + 200,900,200) # 200, 450, 700
        mid_font.draw(400, 250 * i + 240, skill_name[index_list[i]], (255, 255, 255))
        small_font.draw(120, 250 * i + 200, f'{3 - i}',(255,255,255))
        if image_index[i] == 0:
            small_font.draw(400, 250 * i + 200, f'{skill_name[image_index[i]]}의 데미지 20% 증가', (255, 255, 255))
            small_font.draw(900, 250 * i + 240, f'Lv  {attack.normal_bullet_level}', (204, 204, 0))

        if image_index[i] == 1:
            if attack.skill_q_level % 2 != 0:
                small_font.draw(400, 250 * i + 200, f'{skill_name[image_index[i]]}의 데미지 20% 증가', (255, 255, 255))
                small_font.draw(900, 250 * i + 240, f'Lv  {attack.skill_q_level}', (204, 204, 0))
            else:
                small_font.draw(400, 250 * i + 200, f'{skill_name[image_index[i]]}의 쿨타임 10% 감소', (255, 255, 255))
                small_font.draw(900, 250 * i + 240, f'Lv  {attack.skill_q_level}', (204, 204, 0))

        if image_index[i] == 2:
            if attack.skill_w_level % 2 != 0:
                small_font.draw(400, 250 * i + 200, f'{skill_name[image_index[i]]}의 데미지 20% 증가', (255, 255, 255))
                small_font.draw(900, 250 * i + 240, f'Lv  {attack.skill_w_level}', (204, 204, 0))
            else:
                small_font.draw(400, 250 * i + 200, f'{skill_name[image_index[i]]}의 쿨타임 10% 감소', (255, 255, 255))
                small_font.draw(900, 250 * i + 240, f'Lv  {attack.skill_w_level}', (204, 204, 0))

        if image_index[i] == 3:
            small_font.draw(400, 250 * i + 200, f'{skill_name[image_index[i]]}의 데미지 20% 증가', (255, 255, 255))
            small_font.draw(900, 250 * i + 240, f'Lv  {attack.skill_e_level}', (204, 204, 0))
        if image_index[i] == 4:
            if attack.skill_r_level % 2 != 0:
                small_font.draw(400, 250 * i + 200, f'{skill_name[image_index[i]]}의 데미지 10% 증가', (255, 255, 255))
                small_font.draw(900, 250 * i + 240, f'Lv  {attack.skill_r_level}', (204, 204, 0))
            else:
                small_font.draw(400, 250 * i + 200, f'{skill_name[image_index[i]]}의 쿨타임 10% 감소', (255, 255, 255))
                small_font.draw(900, 250 * i + 240, f'Lv  {attack.skill_r_level}', (204, 204, 0))

        if image_index[i] == 5:
            small_font.draw(400, 250 * i + 200, f'모든 스킬의 데미지 5% 증가', (255, 255, 255))
            small_font.draw(900, 250 * i + 240, f'Lv  {character.int_level}', (204, 204, 0))

        if image_index[i] == 6:
            small_font.draw(400, 250 * i + 200, f'최대 체력 20 증가', (255, 255, 255))
            small_font.draw(900, 250 * i + 240, f'Lv  {character.hp_level}', (204, 204, 0))

        if image_index[i] == 7:
            small_font.draw(400, 250 * i + 200, f'이동속도 증가', (255, 255, 255))
            small_font.draw(900, 250 * i + 240, f'Lv  {character.speed_level}', (204, 204, 0))

        image[i].clip_draw(0,0,image_size[image_index[i]][0],image_size[image_index[i]][1],300,250 * i + 200,100,100)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass

