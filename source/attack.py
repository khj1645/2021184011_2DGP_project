from pico2d import *
import character
import rect
import circle

class normal_bullet:
    def __init__(self):
        self.image_x = 43
        self.image_y = 24
        
        
        self.circle = circle.circle()
        self.circle.x = character.hero.rect.x + 9
        self.circle.y = character.hero.rect.y
        self.circle.r = 12
        self.unit_x = 0
        self.unit_y = 0
        self.rad = 0
        self.image = load_image('Bullet5_01.png')
    def update(self):
        self.circle.x += self.unit_x - character.hero.unit_x
        self.circle.y += self.unit_y - character.hero.unit_y
        self.circle.update()
       # self.rect.update()
        if(self.circle.x > character.TUK_WIDTH or self.circle.x < 0 or self.circle.y > character.TUK_HEIGHT or self.circle.y < 0):
            return True
        return False
    def draw(self):
        self.image.rotate_draw(self.rad,self.circle.x,self.circle.y,43,24)
        #self.image.clip_draw(0, 0, self.image_x, self.image_y, self.rect.x, self.rect.y, self.image_x, self.image_x)

  
class skill_q:
    def __init__(self):
        self.image_x = 64
        self.image_y = 32
        self.circle = circle.circle()
        self.circle.x = character.hero.rect.x + 16
        self.circle.y = character.hero.rect.y
        self.circle.r = 16
        self.unit_x = 0
        self.unit_y = 0
        self.rad = 0
        self.frame = 0
        self.image_list = ['Bullet6_01.png','Bullet6_02.png','Bullet6_03.png']
        self.image = load_image(self.image_list[0])
    def update(self):
        self.circle.x += self.unit_x - character.hero.unit_x
        self.circle.y += self.unit_y - character.hero.unit_y
        self.circle.update()
        
        self.frame +=1
        self.frame %=3
        self.image = load_image(self.image_list[self.frame])
        if(self.circle.x > character.TUK_WIDTH or self.circle.x < 0 or self.circle.y > character.TUK_HEIGHT or self.circle.y < 0):
            return True
        return False
    def draw(self):
        self.image.rotate_draw(self.rad,self.circle.x,self.circle.y,128,64)
        #self.image.clip_draw(0, 0, self.image_x, self.image_y, self.rect.x, self.rect.y, self.image_x, self.image_x)
        