from pico2d import *
import circle
import random
import character
import item
import game_framework
import game_world
import levelup
import main
enemys = None
maketime = None
make_limit = None
make_flag = None

PIXEL_PER_METER = (10.0 / 0.2) # 10 pixel 30 cm
RUN_SPEED_MPS_SLOW_ENEMY_X = 3.0
RUN_SPEED_MPS_SLOW_ENEMY_Y = 2.4
RUN_SPEED_PPS_SLOW_ENEMY_X = (RUN_SPEED_MPS_SLOW_ENEMY_X * PIXEL_PER_METER)
RUN_SPEED_PPS_SLOW_ENEMY_Y = (RUN_SPEED_MPS_SLOW_ENEMY_Y * PIXEL_PER_METER)
TIME_PER_ACTION_SLOW_ENEMY = 0.5
ACTION_PER_TIME_SLOW_ENEMY = 1.0 /  TIME_PER_ACTION_SLOW_ENEMY
FRAMES_PER_ACTION_SLOW_ENEMY = 4

RUN_SPEED_MPS_FAST_ENEMY_X = 4.2
RUN_SPEED_MPS_FAST_ENEMY_Y = 3.6
RUN_SPEED_PPS_FAST_ENEMY_X = (RUN_SPEED_MPS_FAST_ENEMY_X * PIXEL_PER_METER)
RUN_SPEED_PPS_FAST_ENEMY_Y = (RUN_SPEED_MPS_FAST_ENEMY_Y * PIXEL_PER_METER)
TIME_PER_ACTION_FAST_ENEMY = 0.5
ACTION_PER_TIME_FAST_ENEMY = 1.0 /  TIME_PER_ACTION_SLOW_ENEMY
FRAMES_PER_ACTION_FAST_ENEMY = 6

class enemy:
    image = None
    radius = [40, 60, 60 ]
    image_x = [130, 110, 105 ]
    image_y = [150, 120, 114 ]
    frame = [6, 4, 4]
    def __init__(self):
        self.type = random.randint(0,2)
        if self.type == 0:
            self.image_list = ['Unit14Motion_MoveA.png','Unit14Motion_MoveB.png',
                                'Unit14Motion_MoveC.png','Unit14Motion_MoveD.png',
                                'Unit14Motion_MoveE.png','Unit14Motion_MoveF.png']
        elif self.type == 1:
            self.image_list = ['Unit15Motion_MoveA.png','Unit15Motion_MoveB.png',
                            'Unit15Motion_MoveC.png','Unit15Motion_MoveD.png']
        else:
            self.image_list = ['Unit22Motion_MoveA.png','Unit22Motion_MoveB.png',
                            'Unit22Motion_MoveC.png','Unit22Motion_MoveD.png']
        self.image = load_image(self.image_list[0])
        self.circle = circle.circle()
        self.circle.x = random.randint(int(character.hero.rect.x -700),int(character.hero.rect.x + 700))
        self.circle.y = random.randint(int(character.hero.rect.y - 450),int(character.hero.rect.y + 450))
        if self.circle.y >= character.hero.rect.y:
            self.circle.y += random.randint(1000,1500)
        else:
            self.circle.y -= random.randint(1000,1500)
            
        self.circle.r = enemy.radius[self.type]
        self.hp = 50
        self.frame = 0
        self.max_frame = enemy.frame[self.type]
        if self.type == 0:
            self.speed_x = RUN_SPEED_PPS_FAST_ENEMY_X * game_framework.frame_time
            self.speed_y = RUN_SPEED_PPS_FAST_ENEMY_Y * game_framework.frame_time
            self.TIME_PER_ACTION = 0.5
            self.ACTION_PER_TIME = 1.0 /  self.TIME_PER_ACTION
            self.FRAMES_PER_ACTION = 4
        else:
            self.speed_x = RUN_SPEED_PPS_SLOW_ENEMY_X * game_framework.frame_time
            self.speed_y = RUN_SPEED_PPS_SLOW_ENEMY_Y * game_framework.frame_time
            self.TIME_PER_ACTION = 0.5
            self.ACTION_PER_TIME = 1.0 /  self.TIME_PER_ACTION
            self.FRAMES_PER_ACTION = 6
        self.die = False
    def update(self):
        self.circle.update()
        if self.die:
            if self.frame >=3:
                return True
            self.image = load_image(self.image_list[int(self.frame)])
            self.frame = (self.frame +  self.FRAMES_PER_ACTION *  self.ACTION_PER_TIME * game_framework.frame_time)
        else:
            if self.type == 0:
                self.speed_x = RUN_SPEED_PPS_FAST_ENEMY_X * game_framework.frame_time
                self.speed_y = RUN_SPEED_PPS_FAST_ENEMY_Y * game_framework.frame_time
                self.TIME_PER_ACTION = 0.5
                self.ACTION_PER_TIME = 1.0 /  self.TIME_PER_ACTION
                self.FRAMES_PER_ACTION = 4
            else:
                self.speed_x = RUN_SPEED_PPS_SLOW_ENEMY_X * game_framework.frame_time
                self.speed_y = RUN_SPEED_PPS_SLOW_ENEMY_Y * game_framework.frame_time
                self.TIME_PER_ACTION = 0.5
                self.ACTION_PER_TIME = 1.0 /  self.TIME_PER_ACTION
                self.FRAMES_PER_ACTION = 6
            self.image = load_image(self.image_list[int(self.frame)])
            self.frame = (self.frame +  self.FRAMES_PER_ACTION *  self.ACTION_PER_TIME * game_framework.frame_time) % self.max_frame
            if self.circle.x < character.hero.rect.x:
                self.circle.x += self.speed_x# - (character.hero.unit_x * game_framework.frame_time)
            if self.circle.x > character.hero.rect.x:
                self.circle.x += -1 * self.speed_x #- (character.hero.unit_x * game_framework.frame_time)
            if self.circle.y < character.hero.rect.y:
                self.circle.y += self.speed_y #- (character.hero.unit_y * game_framework.frame_time)
            if self.circle.y > character.hero.rect.y:
                self.circle.y += -1 * self.speed_y #- (character.hero.unit_y * game_framework.frame_time)
            # for en in enemys:
            #     if en != self and not en.die and self.circle.collide_circle_to_circle(en.circle):
            #         if self.circle.x > en.circle.x: Iw = en.circle.right - self.circle.left
            #         else: Iw = self.circle.right - en.circle.left
            #         if self.circle.y > en.circle.y: Ih = en.circle.top - self.circle.bottom
            #         else: 
            #             Ih = self.circle.top - en.circle.bottom
            #         if Iw > Ih:
            #             if self.circle.y > en.circle.y:
            #                 self.circle.y += Ih
            #             else:
            #                 self.circle.y -= Ih
            #         else:
            #             if self.circle.x > en.circle.x:
            #                 self.circle.x += Iw
            #             else:
            #                 self.circle.x -= Iw
            #         self.circle.update()
                   #  break
        return False
    def draw(self):
        sx = self.circle.x - (character.hero.rect.x - 600)
        sy = self.circle.y - (character.hero.rect.y - 450)
        if self.die:
            self.image.clip_draw(0, 0, 180, 180, sx, sy, self.circle.r * 2, self.circle.r * 2)
        else:  
            self.image.clip_draw(0, 0, enemy.image_x[self.type], enemy.image_y[self.type], sx, sy, self.circle.r * 2, self.circle.r * 2)

def enter():
    global enemys, maketime, make_limit, make_flag
    enemys = []
    maketime = 0
    make_limit = 0.7
    make_flag = False

        
def draw():
    for enemy in enemys:
        enemy.draw()

def make_enemy():
    global maketime, make_limit, make_flag
    
    maketime -= game_framework.frame_time
    if(maketime <= 0):
        maketime = make_limit
        enemys.append(enemy())
        game_world.add_object(enemys[len(enemys) - 1],1)
    if (main.second == 0 or main.second == 30):
        if make_flag == False:
            make_flag = True
            if(make_limit > 0.1):
                print("생성시간 감소")
                make_limit -= 0.1
    else:
        make_flag = False

def check_enemy():
    global enemys
    for enem in enemys[:]:
        if(enem.hp <= 0 and enem.die == False):
            character.hero.exp += 10
            if character.hero.exp >=100:
                game_framework.push_state(levelup)
                character.hero.lv += 1
                character.hero.exp = 100 - character.hero.exp
            enem.die = True
            enem.speed_x = enem.speed_y = enem.frame = 0
            enem.max_frame = 3
            enem.image_list = ['Unit16Motion_DeathA1.png', 'Unit16Motion_DeathB1.png', 'Unit16Motion_DeathC1.png']
            if random.randint(0,10) < 3:
                item.items.append(item.item(enem.circle.x,enem.circle.y))
                game_world.add_object(item.items[len(item.items) - 1],1)

        if enem.die and enem.frame >=3:
            enemys.remove(enem)
            game_world.remove_object(enem)
