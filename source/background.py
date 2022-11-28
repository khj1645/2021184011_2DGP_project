from pico2d import *
import character
import game_framework
import rect
ix = 600
iy = 450
background_pos = None
backgrounds = None
hit_background = None
hit = None
hitcnt = None

def enter():
    global backgrounds, background_pos, hit_background, hit, hitcnt
    background_pos = []
    #character.open_canvas(character.TUK_WIDTH, character.TUK_HEIGHT)
    backgrounds = load_image('Land1DecoA.png')
    hit_background = load_image('HurtGround.png')
    for i in range(0,9):
        background_pos.append(rect.rect())
    
        background_pos[i].x  = 100 + (i%3) * 2000
        background_pos[i].y  = -50 + (i//3) * 2000
        background_pos[i].rx = background_pos[i].ry = 1000
    hit = False
    hitcnt = 0

def update():
    global background_pos
    for i in range(0,9):
        background_pos[i].x -= character.hero.unit_x * game_framework.frame_time
        background_pos[i].y -= character.hero.unit_y * game_framework.frame_time
        background_pos[i].update()
        # backgrounds.clip_draw(0, 0, 500, 500, background_pos[i].x, background_pos[i].y, 2000, 2000)

    for i in range(0,9):
        if background_pos[i].right < 0:
            background_pos[i].x += 4000
        elif background_pos[i].left > 1200:
            background_pos[i].x -= 4000
        elif background_pos[i].top < 0:
            background_pos[i].y += 4000
        elif background_pos[i].bottom > 900:
            background_pos[i].y -= 4000
        background_pos[i].update()

def draw():
    global background_pos, hit, hitcnt
    if hit == True:
        hit_background.clip_draw(0, 0, 720, 1280, 600, 450, 1200, 900)
        hitcnt += 1
        if hitcnt > 5:
            hit = False
    else:
        for i in range(0,9):
            backgrounds.clip_draw(0, 0, 500, 500, background_pos[i].x, background_pos[i].y, 2000, 2000)