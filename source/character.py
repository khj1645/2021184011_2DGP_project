from pico2d import *
import math
import os

os.chdir('d:\\2021184011_2DGP_project\\Sprite_use')

hero = None
running = False
def enter():
    global hero, running
    hero = Hero()
    running = True

def handle_events():
    global running, mouse_x, mouse_y, isMove, vector_x, vector_y, hero, unit_x, unit_y, height, weight, movesheep
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            movesheep = 0
            mouse_x, mouse_y = event.x, TUK_HEIGHT - 1 - event.y
            height = abs(mouse_y - hero.y)
            weight = abs(mouse_x - hero.x)
            _R = math.sqrt((height*height) + (weight*weight))
            _S = _R/2
            unit_y = height / _S
            unit_x = weight / _S
            if mouse_y - hero.y < 0: unit_y *= -1
            if mouse_x - hero.x < 0: unit_x *= -1
            # vector_x = mouse_x - hero.x
            # vector_y = mouse_y - hero.y
            # unit_x = vector_x / math.sqrt(math.pow(vector_x, 2) + math.pow(vector_y, 2))
            # unit_y = vector_y / math.sqrt(math.pow(vector_x, 2) + math.pow(vector_y, 2))
            isMove = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

class Hero:
    
    def __init__(self):
        self.image = load_image('Unit3Motion_MoveAa1.png')
        self.x = 500
        self.y = 500
        self.frame = 0


    def update(self):
        global unit_x, unit_y, isMove, mouse_x, mouse_y, height, weight, movesheep
        if(isMove):
            self.x += unit_x
            self.y += unit_y
            movesheep += unit_x
            if(abs(movesheep) > weight):
                movesheep = 0
                isMove = False

    def draw(self):
        self.image.clip_draw(0, 0, 39, 67, self.x, self.y, 50, 80)



TUK_WIDTH, TUK_HEIGHT = 1200, 900
mouse_x, mouse_y = 0, 0
vector_x, vector_y = 0, 0
unit_x, unit_y = 0, 0
movesheep = 0
height, weight = 0, 0
isMove = False