import pico2d
import game_framework
import lobby
import os

os.chdir('d:\\2021184011_2DGP_project\\Sprite_use')
pico2d.open_canvas(1200, 900)
pico2d.hide_lattice()
game_framework.run(lobby)