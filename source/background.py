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


class InfiniteBackground:

    def __init__(self):
        self.image = load_image('Land1DecoA.png')
        self.hit_background = load_image('HurtGround.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.hit = False
        self.hitcnt = 0

    def draw(self):
        if self.hit == True:
            self.hit_background.clip_draw(0, 0, 720, 1280, 600, 450, 1200, 900)
            self.hitcnt += game_framework.frame_time
            if self.hitcnt > 0.3:
                self.hit = False
        else:
            self.image.clip_draw_to_origin(self.q3l, self.q3b, self.q3w, self.q3h, 0, 0) # quadrant 3
            self.image.clip_draw_to_origin(self.q2l, self.q2b, self.q2w, self.q2h, 0, self.q3h) # quadrant 2
            self.image.clip_draw_to_origin(self.q4l, self.q4b, self.q4w, self.q4h, self.q3w, 0) # quadrant 4
            self.image.clip_draw_to_origin(self.q1l, self.q1b, self.q1w, self.q1h, self.q3w, self.q3h)         # quadrant 1

    def update(self):

        # quadrant 3
        self.q3l = (int(character.hero.rect.x) - self.canvas_width // 2) % self.w
        self.q3b = (int(character.hero.rect.y) - self.canvas_height // 2) % self.h
        self.q3w = clamp(0, self.w - self.q3l, self.w)
        self.q3h = clamp(0, self.h - self.q3b, self.h)


        # quadrant 2
        self.q2l = self.q3l
        self.q2b = 0
        self.q2w = self.q3w
        self.q2h = self.canvas_height - self.q3h
        # quadrand 4
        self.q4l = 0
        self.q4b = self.q3b
        self.q4w = self.canvas_width - self.q3w
        self.q4h = self.q3h
        # quadrand 1
        self.q1l = 0
        self.q1b = 0
        self.q1w = self.q4w
        self.q1h = self.q2h

        # quadrant 2
        self.q2l = self.q3l
        self.q2b = 0
        self.q2w = self.q3w
        self.q2h = self.canvas_height - self.q3h
        # quadrand 4
        self.q4l = 0
        self.q4b = self.q3b
        self.q4w = self.canvas_width - self.q3w
        self.q4h = self.q3h
        # quadrand 1
        self.q1l = 0
        self.q1b = 0
        self.q1w = self.q4w
        self.q1h = self.q2h