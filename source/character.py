from pico2d import *
import rect
import attack
import math


def setMove(event):
    global mouse_x, mouse_y, isMove, hero,  height, weight, movesheep, now_image
    movesheep = 0
    mouse_x, mouse_y = event.x, TUK_HEIGHT - 1 - event.y
    height = abs(mouse_y - hero.rect.y)
    weight = abs(mouse_x - hero.rect.x)
    _R = math.sqrt((height*height) + (weight*weight))
    _S = _R/2
    hero.unit_y = height / _S
    hero.unit_x = weight / _S
    radian = math.atan2(mouse_y - hero.rect.y, mouse_x - hero.rect.x)
    degree = radian * 180 / math.pi
    if degree < 22.5 and degree > -22.5:
        now_image = right_image
        hero.image_x = 52
        hero.image_y = 59
        hero.rect.rx = hero.image_x / 2
        hero.rect.ry = hero.image_y / 2
        hero.rect.update()
    elif degree < 67.5:
        now_image = up_right_image
        hero.image_x = 40
        hero.image_y = 67
        hero.rect.rx = hero.image_x / 2
        hero.rect.ry = hero.image_y / 2
        hero.rect.update()
    elif degree < 112.5:# and degree > -300:
        now_image = up_image
        hero.image_x = 38
        hero.image_y = 66
        hero.rect.rx = hero.image_x / 2
        hero.rect.ry = hero.image_y / 2
        hero.rect.update()
    elif degree < 157.5:# and degree > -240:
        now_image = up_left_image
        hero.image_x = 39
        hero.image_y = 67
        hero.rect.rx = hero.image_x / 2
        hero.rect.ry = hero.image_y / 2
        hero.rect.update()
    elif degree < 180 and degree > -210:
        now_image = left_image
        hero.image_x = 52
        hero.image_y = 59
        hero.rect.rx = hero.image_x / 2
        hero.rect.ry = hero.image_y / 2
        hero.rect.update()
    if degree > -180 and degree < -157.5:
        now_image = left_image
        hero.image_x = 52
        hero.image_y = 59
        hero.rect.rx = hero.image_x / 2
        hero.rect.ry = hero.image_y / 2
        hero.rect.update()
    elif degree < -112.5 and degree > -157.5:
        now_image = down_left_image
        hero.image_x = 44
        hero.image_y = 63
        hero.rect.rx = hero.image_x / 2
        hero.rect.ry = hero.image_y / 2
        hero.rect.update()
    elif degree < -67.5 and degree > -112.5:
        now_image = down_image
        hero.image_x = 39
        hero.image_y = 67
        hero.rect.rx = hero.image_x / 2
        hero.rect.ry = hero.image_y / 2
        hero.rect.update()
    elif degree < -22.5 and degree > -67.5:
        now_image = down_right_image
        hero.image_x = 39
        hero.image_y = 67
        hero.rect.rx = hero.image_x / 2
        hero.rect.ry = hero.image_y / 2
        hero.rect.update()
    elif degree < 0 and degree > -22.5:
        now_image = right_image
        hero.image_x = 52
        hero.image_y = 59
        hero.rect.rx = hero.image_x / 2
        hero.rect.ry = hero.image_y / 2
        hero.rect.update()
    if mouse_y - hero.rect.y < 0:
        hero.unit_y *= -1
    if mouse_x - hero.rect.x < 0:
        hero.unit_x *= -1


    isMove = True
def setNormalBullet(event):
    global mouse_x, mouse_y,  bheight, bweight, normal_bullet
    mouse_x, mouse_y = event.x, TUK_HEIGHT - 1 - event.y
    bheight = abs(mouse_y - normal_bullet[len(normal_bullet) - 1].rect.y)
    bweight = abs(mouse_x - normal_bullet[len(normal_bullet) - 1].rect.x)
    _R = math.sqrt((bheight*bheight) + (bweight*bweight))
    _S = _R/5
    normal_bullet[len(normal_bullet) - 1].unit_y = bheight / _S
    normal_bullet[len(normal_bullet) - 1].unit_x = bweight / _S
    if mouse_y - normal_bullet[len(normal_bullet) - 1].rect.y < 0:
        normal_bullet[len(normal_bullet) - 1].unit_y *= -1
    if mouse_x - normal_bullet[len(normal_bullet) - 1].rect.x < 0:
        normal_bullet[len(normal_bullet) - 1].unit_x *= -1
    normal_bullet[len(normal_bullet) - 1].rad = math.atan2(mouse_y - normal_bullet[len(normal_bullet) - 1].rect.y, mouse_x - normal_bullet[len(normal_bullet) - 1].rect.x)

def arrival():
    global hero, isMove, movesheep, weight, now_image
    if(abs(movesheep) > weight):
        movesheep = 0
        hero.image_x = 31
        hero.image_y = 67
        hero.rect.rx = hero.image_x / 2
        hero.rect.ry = hero.image_y / 2
        hero.rect.update()
        now_image = idle_image
        isMove = False

def enter():
    global hero, running, left_image, right_image, idle_image 
    global up_image, down_image, up_right_image, down_right_image,up_left_image, down_left_image, now_image
    hero = Hero()
    running = True
    right_image = ['Unit3Motion_MoveC1.png','Unit3Motion_MoveC2.png','Unit3Motion_MoveC3.png']
    left_image = ['Unit3Motion_MoveCx1.png','Unit3Motion_MoveCx2.png','Unit3Motion_MoveCx3.png']

    up_right_image = ['Unit3Motion_MoveB1.png','Unit3Motion_MoveB2.png','Unit3Motion_MoveB3.png']
    up_left_image = ['Unit3Motion_MoveBx1.png','Unit3Motion_MoveBx2.png','Unit3Motion_MoveBx3.png']

    down_right_image = ['Unit3Motion_MoveBa1.png','Unit3Motion_MoveBa2.png','Unit3Motion_MoveBa3.png']
    down_left_image = ['Unit3Motion_MoveBax1.png','Unit3Motion_MoveBax2.png','Unit3Motion_MoveBax3.png']

    up_image = ['Unit3Motion_MoveA1.png','Unit3Motion_MoveA2.png','Unit3Motion_MoveA3.png']
    down_image =  ['Unit3Motion_MoveAa1.png','Unit3Motion_MoveAa2.png','Unit3Motion_MoveAa3.png']

    idle_image = ['Unit3Motion_Nomal1.png','Unit3Motion_Nomal2.png', 'Unit3Motion_Nomal1.png']

    now_image = idle_image

def handle_events():
    global running, click
    events = get_events()
    for event in events:
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
            setNormalBullet(event)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

class Hero:
    
    def __init__(self):
        self.image = load_image('Unit3Motion_Nomal1.png')
        self.rect = rect.rect()
        self.image_x = 31
        self.image_y = 67
        self.frame = 0
        self.movelen = 0
        self.rect.x = 500
        self.rect.y = 500
        self.rect.rx = self.image_x / 2
        self.rect.ry = self.image_y / 2
        self.unit_x = 0
        self.unit_y = 0
        self.rect.update()

    def update(self):
        global movesheep
        self.frame = (self.frame + 1) % 3 # todo 애니메이션 속도 조절
        self.image = load_image(now_image[self.frame])
        if(isMove):
            self.rect.x += self.unit_x
            self.rect.y += self.unit_y
            movesheep += self.unit_x
            arrival()
        for a in normal_bullet[:]:
            if a.update():
                normal_bullet.remove(a) 

    def draw(self):
        self.image.clip_draw(0, 0, self.image_x, self.image_y, self.rect.x, self.rect.y, 50, 80)
        for i in range(len(normal_bullet)):
            normal_bullet[i].draw()


normal_bullet = []

hero = None
running = False
click = False
up_image, down_image, up_right_image, down_right_image = None, None, None, None
up_left_image, down_left_image, right_image, left_image, idle_image = None, None, None, None, None
now_image = None
TUK_WIDTH, TUK_HEIGHT = 1200, 900
mouse_x, mouse_y = 0, 0
vector_x, vector_y = 0, 0
movesheep = 0
height, weight = 0, 0
bheight, bweight = 0, 0
isMove = False