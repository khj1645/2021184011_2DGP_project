from pico2d import *
import circle
import random
import character
import item

enemys = None
maketime = None

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
        self.circle.x = random.randint(0,1200)
        self.circle.y = random.randint(0,900)
        if self.circle.y >= 450:
            self.circle.y += random.randint(500,700)
        else:
            self.circle.y -= random.randint(500,700)
            
        self.circle.r = enemy.radius[self.type]
        self.hp = 50
        self.frame = 0
        self.max_frame = enemy.frame[self.type]
        if self.type == 0:
            self.speed_x = 6
            self.speed_y = 3
        else:
            self.speed_x = 4
            self.speed_y = 2
        self.die = False
    def update(self):
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
        return False
    def draw(self):
        if self.die:
            self.image.clip_draw(0, 0, 180, 180, self.circle.x, self.circle.y, self.circle.r * 2, self.circle.r * 2)
        else:  
            self.image.clip_draw(0, 0, enemy.image_x[self.type], enemy.image_y[self.type], self.circle.x, self.circle.y, self.circle.r * 2, self.circle.r * 2)

def enter():
    global enemys, maketime
    enemys = []
    maketime = 1

def update():
    global enemys, maketime
    maketime -=0.016
    if(maketime <= 0):
        maketime = 0.5
        enemys.append(enemy())
    for enem in enemys[:]:
        if(enem.hp <= 0 and enem.die == False):
            enem.die = True
            enem.speed_x = enem.speed_y = enem.frame = 0
            enem.max_frame = 3
            enem.image_list = ['Unit16Motion_DeathA1.png', 'Unit16Motion_DeathB1.png', 'Unit16Motion_DeathC1.png']
            if random.randint(0,10) < 3:
                item.items.append(item.item(enem.circle.x,enem.circle.y))
                
        if enem.update():
            enemys.remove(enem)
def draw():
    for enemy in enemys:
        enemy.draw()
