from this import d
from pico2d import *
import math
class circle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.r = 0
        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0
    def update(self):
        self.left = self.x - self.r
        self.right = self.x + self.r
        self.bottom = self.y - self.r
        self.top = self.y + self.r
        pico2d.draw_rectangle( self.left,self.top,self.right, self.bottom)
        
    def collide_circle_to_circle(self,circle):
        if ((self.x - circle.x) ** 2) + ((self.y - circle.y) ** 2) > (self.r + circle.r) ** 2:
            return False
        return True
        
       

    
