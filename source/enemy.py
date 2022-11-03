from pico2d import *
import circle
import random
import character

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
    def update(self):
        self.image = load_image(self.image_list[self.frame % self.max_frame])
        self.frame +=1
        if self.circle.x < character.hero.rect.x:
            self.circle.x += 4 - character.hero.unit_x
        if self.circle.x > character.hero.rect.x:
            self.circle.x += -4 - character.hero.unit_x
        if self.circle.y < character.hero.rect.y:
            self.circle.y += 2 - character.hero.unit_y
        if self.circle.y > character.hero.rect.y:
            self.circle.y += -2 - character.hero.unit_y
    def draw(self):
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
        enem.update()
        if(enem.hp <= 0):
            enemys.remove(enem)
def draw():
    for enemy in enemys:
        enemy.draw()
