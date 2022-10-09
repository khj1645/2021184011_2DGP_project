from pico2d import *
import os


TUK_WIDTH, TUK_HEIGHT = 1200, 900
os.chdir('d:\\2021184011_2DGP_project\\Sprite_use')

open_canvas(TUK_WIDTH, TUK_HEIGHT)
character = load_image('Unit3Motion_MoveAa1.png')
enemy1 = load_image('Unit14Motion_MoveA.png')
enemy2 = load_image('Unit15Motion_MoveA.png')
enemy3 = load_image('Unit22Motion_MoveA.png')
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
character.clip_draw(0, 0, 39, 67, 100, 100,50,80)
enemy1.clip_draw(0, 0, 122, 150, 300, 100,60,90)
enemy2.clip_draw(0, 0, 112, 118, 500, 100,110,120)
enemy3.clip_draw(0, 0, 105, 119, 700, 100,110,120)
update_canvas()
delay(50)
close_canvas()

