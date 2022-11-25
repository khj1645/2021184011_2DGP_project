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
        self.circle.x = random.randint(-100,1300)
        self.circle.y = random.randint(0,900)
        if self.circle.y >= 450:
            self.circle.y += random.randint(1000,1500)
        else:
            self.circle.y -= random.randint(1000,1500)
            
        self.circle.r = enemy.radius[self.type]
        self.hp = 50
        self.frame = 0
        self.max_frame = enemy.frame[self.type]
        if self.type == 0:
            self.speed_x = 3.5
            self.speed_y = 3
        else:
            self.speed_x = 2.5
            self.speed_y = 2
        self.die = False
    def update(self):
        self.circle.update()
        if self.die:
            if self.frame >=3:
                return True
            self.image = load_image(self.image_list[self.frame % self.max_frame])
            self.frame +=1
        else:
            self.image = load_image(self.image_list[self.frame % self.max_frame])
            self.frame +=1
            if self.circle.x < character.hero.rect.x:
                self.circle.x += self.speed_x - character.hero.unit_x
            if self.circle.x > character.hero.rect.x:
                self.circle.x += -1 * self.speed_x - character.hero.unit_x
            if self.circle.y < character.hero.rect.y:
                self.circle.y += self.speed_y - character.hero.unit_y
            if self.circle.y > character.hero.rect.y:
                self.circle.y += -1 * self.speed_y - character.hero.unit_y
            for en in enemys:
                if en != self and not en.die and self.circle.collide_circle_to_circle(en.circle):
                    if self.circle.x > en.circle.x: Iw = en.circle.right - self.circle.left
                    else: Iw = self.circle.right - en.circle.left
                    if self.circle.y > en.circle.y: Ih = en.circle.top - self.circle.bottom
                    else: 
                        Ih = self.circle.top - en.circle.bottom
                    if Iw > Ih:
                        if self.circle.y > en.circle.y:
                            self.circle.y += Ih
                        else:
                            self.circle.y -= Ih
                    else:
                        if self.circle.x > en.circle.x:
                            self.circle.x += Iw
                        else:
                            self.circle.x -= Iw
                    self.circle.update()
                   #  break
        return False
    def draw(self):
        if self.die:
            self.image.clip_draw(0, 0, 180, 180, self.circle.x, self.circle.y, self.circle.r * 2, self.circle.r * 2)
        else:  
            self.image.clip_draw(0, 0, enemy.image_x[self.type], enemy.image_y[self.type], self.circle.x, self.circle.y, self.circle.r * 2, self.circle.r * 2)

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
    
    maketime -= 0.016 # + game_framework.frame_time + 
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
            character.hero.exp += 10
            if character.hero.exp >=100:
                game_framework.push_state(levelup)
                character.hero.lv += 1
                character.hero.exp = 100 - character.hero.exp
