from pico2d import *
import character
import rect
import os

os.chdir('d:\\2021184011_2DGP_project\\Sprite_use')

class normal_bullet:
    def __init__(self):
        self.image_x = 43
        self.image_y = 24
        self.rect = rect.rect()
        self.rect.x = character.hero.rect.x
        self.rect.y = character.hero.rect.y
        self.rect.rx = self.image_x / 2
        self.rect.ry = self.image_y / 2
        self.unit_x = 0
        self.unit_y = 0
        self.rad = 0
        self.image = load_image('Bullet5_01.png')
    def update(self):
        self.rect.x += self.unit_x
        self.rect.y += self.unit_y
        if(self.rect.x > character.TUK_WIDTH or self.rect.x < 0 or self.rect.y > character.TUK_HEIGHT or self.rect.y < 0):
            return True
        return False
    def draw(self):
        self.image.rotate_draw(self.rad,self.rect.x,self.rect.y,43,24)
        #self.image.clip_draw(0, 0, self.image_x, self.image_y, self.rect.x, self.rect.y, self.image_x, self.image_x)
        