import pico2d
import game_framework
import lobby
import os


os.chdir('Sprite_use')
pico2d.open_canvas(1200, 900)
pico2d.hide_lattice()
game_framework.run(lobby)
