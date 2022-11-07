from pico2d import *
import character
import rect

items = None


class item:
    image = None
    def __init__(self, x, y):
        if item.image == None:
            self.image = load_image('item15.png')
        self.rect = rect.rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.rx = 15
        self.rect.ry = 15
        self.rect.update()
        
    def update(self):
        self.rect.x += -character.hero.unit_x
        self.rect.y += -character.hero.unit_y
        self.rect.update()
        
    def draw(self):
        self.image.clip_draw(0, 0, 40, 40, self.rect.x, self.rect.y, self.rect.rx * 2, self.rect.ry * 2)
        
def enter():
    global items
    items = []

def update():
    for item in items:
        item.update()
        
def draw():
    for item in items:
        item.draw()
