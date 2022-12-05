from pico2d import *
import game_framework
import character
import rect

items = None


class Item:
    image = None
    def __init__(self, x, y):
        if Item.image == None:
            self.image = load_image('item15.png')
        self.rect = rect.rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.rx = 15
        self.rect.ry = 15
        self.rect.update()
        
    def update(self):
        #self.rect.x += -(character.hero.unit_x * game_framework.frame_time)
        #self.rect.y += -(character.hero.unit_y * game_framework.frame_time)
        self.rect.update()
        
    def draw(self):
        sx = self.rect.x - (character.hero.rect.x - 600)
        sy = self.rect.y - (character.hero.rect.y - 450)
        self.image.clip_draw(0, 0, 40, 40, sx, sy, self.rect.rx * 2, self.rect.ry * 2)
        
def enter():
    global items
    items = []

def update():
    for item in items:
        item.update()
        
def draw():
    for item in items:
        item.draw()
