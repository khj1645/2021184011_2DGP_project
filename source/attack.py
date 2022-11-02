from random import randint
from pico2d import *
import character
import rect
import circle
import enemy
class normal_bullet:
    image = None
    def __init__(self):
        self.image_x = 43
        self.image_y = 24
        
        
        self.circle = circle.circle()
        self.circle.x = character.hero.rect.x
        self.circle.y = character.hero.rect.y
        self.circle.r = 10
        self.unit_x = 0
        self.unit_y = 0
        self.rad = 0
        if normal_bullet.image == None:
            self.image = load_image('Bullet5_01.png')
    def update(self):
        self.circle.x += self.unit_x - character.hero.unit_x
        self.circle.y += self.unit_y - character.hero.unit_y
        self.circle.update()
       # self.rect.update()
        if(self.circle.x > character.TUK_WIDTH or self.circle.x < 0 or self.circle.y > character.TUK_HEIGHT or self.circle.y < 0):
            return True
        for ene in enemy.enemys:
            if(self.circle.collide_circle_to_circle(ene.circle)):
                ene.hp -=5
                return True
        return False
    def draw(self):
        self.image.rotate_draw(self.rad,self.circle.x,self.circle.y,43,24)
        #self.image.clip_draw(0, 0, self.image_x, self.image_y, self.rect.x, self.rect.y, self.image_x, self.image_x)

  
class skill_q:
    image = None
    def __init__(self):
        self.image_x = 64
        self.image_y = 32
        self.circle = circle.circle()
        self.circle.x = character.hero.rect.x
        self.circle.y = character.hero.rect.y
        self.circle.r = 20
        self.unit_x = 0
        self.unit_y = 0
        self.rad = 0
        self.frame = 0
        self.image_list = ['Bullet6_01t.png','Bullet6_02t.png','Bullet6_03t.png']
        if skill_q.image == None:
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
        for ene in enemy.enemys:
            if(self.circle.collide_circle_to_circle(ene.circle)):
                ene.hp -=50
                return True
        return False
    def draw(self):
        self.image.rotate_draw(self.rad,self.circle.x,self.circle.y,80,64)
        #self.image.clip_draw(0, 0, self.image_x, self.image_y, self.rect.x, self.rect.y, self.image_x, self.image_x)

class skill_e:
    image = None
    def __init__(self):
        self.image_x = 468
        self.image_y = 467
        self.circle = circle.circle()
        self.circle.x = character.hero.rect.x
        self.circle.y = character.hero.rect.y
        self.circle.r = 200
        self.frame = 0
        if skill_e.image == None:
            self.image_list = ['ElectricZone1A.png','ElectricZone1B.png','ElectricZone1C.png']
            self.image = load_image(self.image_list[0])
    def update(self):
        self.circle.update()
        self.frame +=1
        self.frame %=3
        self.image = load_image(self.image_list[self.frame])
        for ene in enemy.enemys:
            if self.circle.collide_circle_to_circle(ene.circle):
                ene.hp -= 0.5
       
    def draw(self):
        #self.image.rotate_draw(self.rad,self.circle.x,self.circle.y,128,64)
        self.image.clip_draw(0, 0, self.image_x, self.image_y, self.circle.x, self.circle.y, self.circle.r * 2, self.circle.r * 2)


class skill_w:
    image = None
    def __init__(self):
        self.image_x = 80
        self.image_y = 1440
        self.rect = [rect.rect() for i in range(3)]
        for i in range(3):
            self.rect[i].x = randint(0,1200)
            self.rect[i].rx = 20
            self.rect[i].ry = 450
            self.rect[i].y = character.hero.rect.y
        self.rect[1].x = 9999 # todo : 업그레이드에 따라 번개 갈래 수 증가
        self.rect[2].x = 9999 
        self.frame = -1
        if skill_w.image == None:
            self.image_list = ['ThunderA0.png','ThunderA1.png','ThunderA2.png']
            self.effect_list = ['Explosion7_01.png','Explosion7_02.png','Explosion7_03.png','Explosion7_04.png','Explosion7_05.png','Explosion7_06.png']
            self.image = load_image(self.image_list[0])
            self.effect = load_image(self.effect_list[0])
    def update(self):
        if self.frame >= 6:
            return True
        if self.frame == 0:
            for ene in enemy.enemys:
                for i in range(3):
                    if self.rect[i].collide_rect_to_circle(ene.circle):
                        ene.hp -=30
        self.frame += 1
        self.image = load_image(self.image_list[self.frame % 3])
        self.effect = load_image(self.effect_list[self.frame % 6])
        for i in range(3):
            self.rect[i].x += (-1) ** self.frame * (20)
            self.rect[i].update()
        return False
    def draw(self):
        #self.image.rotate_draw(self.rad,self.circle.x,self.circle.y,128,64)
        for i in range(3):
            self.image.clip_draw(0, 0, self.image_x, self.image_y, self.rect[i].x, self.rect[i].y, 40, 900)
            self.effect.clip_draw(0, 0, 181, 175, self.rect[i].x, 25, 100, 100)

class skill_r:
    image = None
    def __init__(self):
        self.isuse = False
        self.move_rate_y = 0
        self.move_rate_x = 0
        self.image_x = 330
        self.image_y = 330
        self.circle = circle.circle()
        self.circle.x = 0
        self.circle.y = 0
        self.circle.r = 150
        self.frame = -1
        if skill_r.image == None:
            self.image_list = ['MeteorC1.png','MeteorC2.png']
            self.image = load_image(self.image_list[0])
    def update(self):
        self.circle.update()
        self.frame +=1
        self.frame %=2
        self.circle.y -= 10
        self.circle.x += 1
        self.image = load_image(self.image_list[self.frame])
       
    def draw(self):
        #self.image.rotate_draw(self.rad,self.circle.x,self.circle.y,128,64)
        self.image.clip_draw(0, 0, self.image_x, self.image_y, self.circle.x, self.circle.y, self.circle.r * 2, self.circle.r * 2)