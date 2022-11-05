import pico2d
import game_framework

import main
import os

os.chdir('d:\\2021184011_2DGP_project\\Sprite_use')
pico2d.open_canvas(1200, 900)
game_framework.run(main)
pico2d.clear_canvas()

