from this import d
from pico2d import *
import math
class circle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.r = 0
    def update(self):
        pico2d.draw_rectangle( self.x - self.r,self.y - self.r,self.x + self.r, self.y + self.r)
        
    def collide_circle_to_circle(self,circle):
        if ((self.x - circle.x) ** 2) + ((self.y - circle.y) ** 2) > (self.r + circle.r) ** 2:
            return False
        return True
        
       

    
