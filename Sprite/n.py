from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)

character = load_image('Unit1Motion_MoveB2.png')

character.clip_draw(0,0,45,55,600,500,80,80)
update_canvas()
delay(4)
close_canvas()








