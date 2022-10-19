from this import d
from pico2d import *
class circle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.r = 0
    def update(self):
        pico2d.draw_rectangle( self.x - self.r,self.y - self.r,self.x + self.r, self.y + self.r)
       

    
