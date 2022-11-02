from pico2d import *
import circle
import random
import character

enemys = None
maketime = None
class enemy:
    image = None
    def __init__(self):
        if enemy.image == None:
            self.image = load_image('Unit15Motion_MoveA.png')
        self.circle = circle.circle()
        self.circle.x = random.randint(0,1200)
        self.circle.y = random.randint(0,900)
        if self.circle.y >= 450:
            self.circle.y += random.randint(500,700)
        else:
            self.circle.y -= random.randint(500,700)
            
        self.circle.r = 60
        self.hp = 50
    def update(self):
        if self.circle.x < character.hero.rect.x:
            self.circle.x += 2 - character.hero.unit_x
        if self.circle.x > character.hero.rect.x:
            self.circle.x += -2 - character.hero.unit_x
        if self.circle.y < character.hero.rect.y:
            self.circle.y += 2 - character.hero.unit_y
        if self.circle.y > character.hero.rect.y:
            self.circle.y += -2 - character.hero.unit_y
    def draw(self):
        self.image.clip_draw(0, 0, 110, 120, self.circle.x, self.circle.y, 120, 120)

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
