from random import randint
from pico2d import *
import character
import game_framework
import rect
import circle

normal_bullet_damage = 5
skill_q_damage = 50
skill_w_damage = 30
skill_e_damage = 1
skill_r_damage = 200

normal_bullet_level = 1
skill_q_level = 1
skill_w_level = 1
skill_e_level = 1
skill_r_level = 1

TIME_PER_ACTION_E = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION_E
FRAMES_PER_ACTION_E = 3

TIME_PER_ACTION_W = 0.1
ACTION_PER_TIME_W = 1.0 / TIME_PER_ACTION_W
FRAMES_PER_ACTION_W = 3

TIME_PER_ACTION_R = 0.3
ACTION_PER_TIME_R = 1.0 / TIME_PER_ACTION_R
FRAMES_PER_ACTION_R = 4

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
        self.circle.x += (self.unit_x * game_framework.frame_time) #- (character.hero.unit_x * game_framework.frame_time)
        self.circle.y += (self.unit_y * game_framework.frame_time) #- (character.hero.unit_y * game_framework.frame_time)
        self.circle.update()
       # self.rect.update()
    def draw(self):
        sx = self.circle.x - (character.hero.rect.x - 600)
        sy = self.circle.y - (character.hero.rect.y - 450)
        self.image.rotate_draw(self.rad,sx,sy,43,24)
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
        self.circle.x += (self.unit_x * game_framework.frame_time) #- (character.hero.unit_x * game_framework.frame_time)
        self.circle.y += (self.unit_y * game_framework.frame_time) #- (character.hero.unit_y * game_framework.frame_time)
        self.circle.update()
        
        self.frame +=1
        self.frame %=3
        self.image = load_image(self.image_list[self.frame])
    def draw(self):
        sx = self.circle.x - (character.hero.rect.x - 600)
        sy = self.circle.y - (character.hero.rect.y - 450)
        self.image.rotate_draw(self.rad,sx,sy,80,64)
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
        self.frame = (self.frame + FRAMES_PER_ACTION_E * ACTION_PER_TIME * game_framework.frame_time) % 3
        self.image = load_image(self.image_list[int(self.frame)])
        self.circle.x = character.hero.rect.x
        self.circle.y = character.hero.rect.y
       
    def draw(self):
        sx = self.circle.x - (character.hero.rect.x - 600)
        sy = self.circle.y - (character.hero.rect.y - 450)
        #self.image.rotate_draw(self.rad,self.circle.x,self.circle.y,128,64)
        self.image.clip_draw(0, 0, self.image_x, self.image_y, sx, sy, self.circle.r * 2, self.circle.r * 2)


class skill_w:
    image = None
    def __init__(self):
        self.image_x = 80
        self.image_y = 1440
        self.rect = [rect.rect() for i in range(3)]
        self.rect[0].x = randint(0,1200)
        self.rect[0].rx = 20
        self.rect[0].ry = 450
        self.rect[0].y = character.hero.rect.y
        self.sx = 0
        self.frame = 0
        if skill_w.image == None:
            self.image_list = ['ThunderA0.png','ThunderA1.png','ThunderA2.png']
            self.effect_list = ['Explosion7_01.png','Explosion7_02.png','Explosion7_03.png','Explosion7_04.png','Explosion7_05.png','Explosion7_06.png']
            self.image = load_image(self.image_list[0])
            self.effect = load_image(self.effect_list[0])
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION_W * ACTION_PER_TIME_W * game_framework.frame_time)
        #self.frame += 1
        self.image = load_image(self.image_list[int(self.frame) % 3])
        self.effect = load_image(self.effect_list[int(self.frame) % 6])
        self.rect[0].x += (-1) ** int(self.frame) * (5)
        self.rect[0].update()
    def draw(self):

        sy = self.rect[0].y - (character.hero.rect.y - 450)
        #self.image.rotate_draw(self.rad,self.circle.x,self.circle.y,128,64)
        self.image.clip_draw(0, 0, self.image_x, self.image_y, self.sx, sy, 40, 900)
        self.effect.clip_draw(0, 0, 181, 175, self.sx, sy - 425, 100, 100)

class skill_r:
    image = None
    explosion_image = None
    def __init__(self):
        self.isuse = False
        self.isexplo = False
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
            self.image_list = ['MeteorC1.png','MeteorC2.png', 'MeteorC3.png']
            self.explosion_image_list = ['Explosion54_02.png','Explosion54_03.png',
                                         'Explosion54_04.png','Explosion54_05.png',
                                         ]
            self.image = load_image(self.image_list[0])
    def update(self):
        if self.isexplo:
            if self.frame >= 3:
                self.isuse = False
                self.isexplo = False
            else:
                self.frame = (self.frame + FRAMES_PER_ACTION_R * ACTION_PER_TIME_R * game_framework.frame_time)
                self.image = load_image(self.explosion_image_list[int(self.frame) % 4])
        else:
            self.circle.update()
            self.frame = (self.frame + FRAMES_PER_ACTION_R * ACTION_PER_TIME_R * game_framework.frame_time)
            self.circle.y -= 1800 * game_framework.frame_time #+ (character.hero.unit_y * game_framework.frame_time)
            #self.circle.x -= (character.hero.unit_x * game_framework.frame_time)
            # self.circle.x += 1
            self.image = load_image(self.image_list[int(self.frame) % 3])
       
    def draw(self):
        #self.image.rotate_draw(self.rad,self.circle.x,self.circle.y,128,64)
        sx = self.circle.x - (character.hero.rect.x - 600)
        sy = self.circle.y - (character.hero.rect.y - 450)
        if self.isexplo:
            self.image.clip_draw(0, 0, 524, 556, sx, sy, 600, 600)
            # draw_rectangle(self.circle.x - self.circle.r, self.circle.y - self.circle.r,
                           # self.circle.x + self.circle.r,self.circle.y + self.circle.r)
                
        else:    
            self.image.clip_draw(0, 0, self.image_x, self.image_y, sx, sy, 317, 354)
