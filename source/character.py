from pico2d import *
import rect
import attack
import math
import lobby
import game_framework
import game_world
import enemy
import item
import background

def setMove(event):
    global mouse_x, mouse_y, isMove, hero,  height, weight, movesheep, now_image, speed
    movesheep = 0
    mouse_x, mouse_y = event.x, TUK_HEIGHT - 1 - event.y
    height = abs(mouse_y - hero.rect.y)
    weight = abs(mouse_x - hero.rect.x)
    _R = math.sqrt((height*height) + (weight*weight))
    _S = _R/speed
    hero.unit_y = height / _S
    hero.unit_x = weight / _S
    radian = math.atan2(mouse_y - hero.rect.y, mouse_x - hero.rect.x)
    degree = radian * 180 / math.pi
    if degree < 22.5 and degree > -22.5:
        now_image = right_image
        hero.image_x = 52
        hero.image_y = 59
        # hero.rect.rx = hero.image_x / 2
        # hero.rect.ry = hero.image_y / 2
        hero.rect.update()
    elif degree < 67.5:
        now_image = up_right_image
        hero.image_x = 40
        hero.image_y = 67
        # hero.rect.rx = hero.image_x / 2
        # hero.rect.ry = hero.image_y / 2
        hero.rect.update()
    elif degree < 112.5:# and degree > -300:
        now_image = up_image
        hero.image_x = 38
        hero.image_y = 66
        # hero.rect.rx = hero.image_x / 2
        # hero.rect.ry = hero.image_y / 2
        hero.rect.update()
    elif degree < 157.5:# and degree > -240:
        now_image = up_left_image
        hero.image_x = 39
        hero.image_y = 67
        # hero.rect.rx = hero.image_x / 2
        # hero.rect.ry = hero.image_y / 2
        hero.rect.update()
    elif degree < 180 and degree > -210:
        now_image = left_image
        hero.image_x = 52
        hero.image_y = 59
        # hero.rect.rx = hero.image_x / 2
        # hero.rect.ry = hero.image_y / 2
        hero.rect.update()
    if degree > -180 and degree < -157.5:
        now_image = left_image
        hero.image_x = 52
        hero.image_y = 59
        # hero.rect.rx = hero.image_x / 2
        # hero.rect.ry = hero.image_y / 2
        hero.rect.update()
    elif degree < -112.5 and degree > -157.5:
        now_image = down_left_image
        hero.image_x = 44
        hero.image_y = 63
        # hero.rect.rx = hero.image_x / 2
        # hero.rect.ry = hero.image_y / 2
        hero.rect.update()
    elif degree < -67.5 and degree > -112.5:
        now_image = down_image
        hero.image_x = 39
        hero.image_y = 67
        # hero.rect.rx = hero.image_x / 2
        # hero.rect.ry = hero.image_y / 2
        hero.rect.update()
    elif degree < -22.5 and degree > -67.5:
        now_image = down_right_image
        hero.image_x = 39
        hero.image_y = 67
        # hero.rect.rx = hero.image_x / 2
        # hero.rect.ry = hero.image_y / 2
        hero.rect.update()
    elif degree < 0 and degree > -22.5:
        now_image = right_image
        hero.image_x = 52
        hero.image_y = 59
        # hero.rect.rx = hero.image_x / 2
        # hero.rect.ry = hero.image_y / 2
        hero.rect.update()
    if mouse_y - hero.rect.y < 0:
        hero.unit_y *= -1
    if mouse_x - hero.rect.x < 0:
        hero.unit_x *= -1


    isMove = True
def setBullet(event, bullet):
    global mouse_x, mouse_y,  bheight, bweight
    mouse_x, mouse_y = event.x, TUK_HEIGHT - 1 - event.y
    bheight = abs(mouse_y - bullet[len(bullet) - 1].circle.y)
    bweight = abs(mouse_x - bullet[len(bullet) - 1].circle.x)
    _R = math.sqrt((bheight*bheight) + (bweight*bweight))
    _S = _R/10
    bullet[len(bullet) - 1].unit_y = bheight / _S
    bullet[len(bullet) - 1].unit_x = bweight / _S
    if mouse_y - bullet[len(bullet) - 1].circle.y < 0:
        bullet[len(bullet) - 1].unit_y *= -1
    if mouse_x - bullet[len(bullet) - 1].circle.x < 0:
        bullet[len(bullet) - 1].unit_x *= -1
    bullet[len(bullet) - 1].rad = math.atan2(mouse_y - bullet[len(bullet) - 1].circle.y, mouse_x - bullet[len(bullet) - 1].circle.x)

    
def arrival():
    global hero, isMove, movesheep, weight, now_image
    if(abs(movesheep) > weight):
        movesheep = 0
        hero.image_x = 31
        hero.image_y = 67
        hero.rect.rx = hero.image_x / 2
        hero.rect.ry = hero.image_y / 2
        hero.unit_x = hero.unit_y = 0
        hero.rect.update()
        now_image = idle_image
        isMove = False

def enter():
    global hero, running, left_image, right_image, idle_image, skill_q_coll_time, skill_e, skill_w, skill_w_coll_time, skill_r, skill_r_cool_time
    global up_image, down_image, up_right_image, down_right_image,up_left_image, down_left_image, now_image, hit_time, die_image, hero_hp
    global hp_level, int_level, speed_level, speed
    hp_level, int_level, speed_level, speed = 1, 1, 1, 5
    running = True
    right_image = ['Unit3Motion_MoveC1.png','Unit3Motion_MoveC2.png','Unit3Motion_MoveC3.png']
    left_image = ['Unit3Motion_MoveCx1.png','Unit3Motion_MoveCx2.png','Unit3Motion_MoveCx3.png']
    hero_hp = 100
    hero = Hero()
    game_world.add_object(hero,1)

    up_right_image = ['Unit3Motion_MoveB1.png','Unit3Motion_MoveB2.png','Unit3Motion_MoveB3.png']
    up_left_image = ['Unit3Motion_MoveBx1.png','Unit3Motion_MoveBx2.png','Unit3Motion_MoveBx3.png']

    down_right_image = ['Unit3Motion_MoveBa1.png','Unit3Motion_MoveBa2.png','Unit3Motion_MoveBa3.png']
    down_left_image = ['Unit3Motion_MoveBax1.png','Unit3Motion_MoveBax2.png','Unit3Motion_MoveBax3.png']

    up_image = ['Unit3Motion_MoveA1.png','Unit3Motion_MoveA2.png','Unit3Motion_MoveA3.png']
    down_image =  ['Unit3Motion_MoveAa1.png','Unit3Motion_MoveAa2.png','Unit3Motion_MoveAa3.png']

    idle_image = ['Unit3Motion_Nomal1.png','Unit3Motion_Nomal2.png', 'Unit3Motion_Nomal1.png']

    die_image =  ['Unit3Motion_DeathA1.png','Unit3Motion_DeathB1.png','Unit3Motion_DeathC1.png','Unit3Motion_DeathD1.png']
    
    now_image = idle_image

    skill_q_coll_time = 0
    skill_e = attack.skill_e()
    game_world.add_object(skill_e,1)
    skill_w_coll_time = 0
    skill_r_cool_time = 0
    skill_r = []
    skill_w = []
    hit_time = 0

def handle_events(event):
    global running, click, skill_q_coll_time, skill_w, skill_w_coll_time, skill_r_cool_time, skill_r
    if event.type == SDL_QUIT:
            running = False
    elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_RIGHT:
            click = True
            setMove(event)
    elif event.type == SDL_MOUSEMOTION and click == True:
            if(click):
                setMove(event)
    elif event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_RIGHT:
            click = False
    elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            normal_bullet.append(attack.normal_bullet())
            game_world.add_object(normal_bullet[len(normal_bullet) - 1],1)
            setBullet(event, normal_bullet)
    elif event.key == SDLK_q:
            if(skill_q_coll_time <= 0):
                skill_q_coll_time = 0.5
                skill_q.append(attack.skill_q())
                game_world.add_object(skill_q[len(skill_q) - 1],1)
                x, y = ctypes.c_int(0), ctypes.c_int(0)
                buttonstate = SDL_GetMouseState(ctypes.byref(x), ctypes.byref(y))
                event.x = x.value
                event.y = y.value
                setBullet(event,skill_q)
                print(get_time())
    elif event.key == SDLK_w:
            if(skill_w_coll_time <= 0):
                skill_w_coll_time = 0.5
                skill_w.append(attack.skill_w())
                game_world.add_object(skill_w[len(skill_w) - 1],1)
                x, y = ctypes.c_int(0), ctypes.c_int(0)
                buttonstate = SDL_GetMouseState(ctypes.byref(x), ctypes.byref(y))
                event.x = x.value
                skill_w[len(skill_w) - 1].rect[0].x = event.x

    elif event.key == SDLK_r:
            if(skill_r_cool_time <= 0):
                skill_r_temp = attack.skill_r()
                
                skill_r_cool_time = 2
                x, y = ctypes.c_int(0), ctypes.c_int(0)
                buttonstate = SDL_GetMouseState(ctypes.byref(x), ctypes.byref(y))
                event.x = x.value
                event.y = y.value
                skill_r_temp.move_rate_y = TUK_HEIGHT - 1 - event.y
                skill_r_temp.circle.x = x.value
                skill_r_temp.circle.y = 1350
                skill_r_temp.isuse = True
                skill_r.append(skill_r_temp)
                game_world.add_object(skill_r_temp,1)

def update():
    global hit_time, now_image, die_image
    if hit_time > 0:
        hit_time -= 0.016 # + game_framework.frame_time + 
    if hero.hp <= 0 and hero.die == False:
        hero.die = True
        hero.image_x = 40
        hero.image_y = 70
        hero.frame = 0
        now_image = die_image
    if hero.update():
        game_framework.change_state(lobby)

def draw():
    hero.draw()
class Hero:
    
    def __init__(self):
        self.image = load_image('Unit3Motion_Nomal1.png')
        self.hp_image = load_image('Sheet_UIBar03.png')
        self.exp_image = load_image('Sheet_ManaBar_Normal.png')
        self.rect = rect.rect()
        self.exp = 0
        self.lv = 1
        self.hp = hero_hp
        self.image_x = 31
        self.image_y = 67
        self.frame = 0
        self.movelen = 0
        self.rect.x = 600
        self.rect.y = 450
        self.rect.rx = self.image_x / 2
        self.rect.ry = self.image_y / 2
        self.unit_x = 0
        self.unit_y = 0
        self.die = False
        self.rect.update()

    def update(self):
        global movesheep, skill_q_coll_time, skill_w_coll_time, hit_time, skill_r_cool_time, hero_hp
        if self.die:
            self.image = load_image(now_image[self.frame % 4])
            self.frame = self.frame + 1
        else:
            skill_q_coll_time -= 0.016 # + game_framework.frame_time + 
            skill_w_coll_time -= 0.016 # + game_framework.frame_time + 
            skill_r_cool_time -= 0.016 # + game_framework.frame_time + 
            hit_time -= 0.016
            self.frame = (self.frame + 1) % 3 # todo 애니메이션 속도 조절
            self.image = load_image(now_image[self.frame])
            if(isMove):
                # self.rect.x += self.unit_x
                # self.rect.y += self.unit_y
                #pico2d.draw_rectangle(hero.rect.left,hero.rect.top, hero.rect.right, hero.rect.bottom )
                movesheep += self.unit_x
                self.rect.update()
                arrival()

            self.rect.update()
        return False
    def draw(self):
        
        for i in range(len(normal_bullet)):
            normal_bullet[i].draw()
        for i in range(len(skill_q)):
            skill_q[i].draw()
        for i in range(len(skill_w)):
            skill_w[i].draw()
        skill_e.draw()
        for a in skill_r:
            a.draw()
        if self.die:
            self.image.clip_draw(0, 0, self.image_x, self.image_y, self.rect.x, self.rect.y, 50, 80)
        else:    
            self.image.clip_draw(0, 0, self.image_x, self.image_y, self.rect.x, self.rect.y, 50, 80)
        self.exp_image.clip_draw(0, 0, 465,48, TUK_WIDTH / 2, TUK_HEIGHT, TUK_WIDTH * (self.exp / 100), 20)
        self.hp_image.clip_draw(0, 0, 465,48, self.rect.x, self.rect.y + 50, self.hp, 10)


normal_bullet = []
skill_q= []
skill_w= []
skill_r = []
skill_q_coll_time = None
skill_w_coll_time = None
skill_r_cool_time = None
skill_e = None
hero = None
running = False
click = False
up_image, down_image, up_right_image, down_right_image, die_image = None, None, None, None, None
up_left_image, down_left_image, right_image, left_image, idle_image = None, None, None, None, None
now_image = None
TUK_WIDTH, TUK_HEIGHT = 1200, 900
mouse_x, mouse_y = 0, 0
vector_x, vector_y = 0, 0
movesheep = 0
height, weight = 0, 0
bheight, bweight = 0, 0
isMove = False
hit_time = None
hero_hp = None
hp_level, int_level, speed_level, speed = None, None, None, None