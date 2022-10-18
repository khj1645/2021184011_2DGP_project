from pico2d import *
class rect:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rx = 0
        self.ry = 0
        self.left = 0
        self.right = 0
        self.bottom = 0
        self.top = 0
    def update(self):
        self.left = self.x - self.rx
        self.right = self.x + self.rx
        self.bottom = self.y - self.ry
        self.top = self.y + self.ry
       # pico2d.draw_rectangle( self.left,self.top,self.right, self.bottom)

    def collide_rect(self,rect):
        return (self.left <= rect.right and
                self.right >= rect.left and
                self.top >= rect.bottom and
                self.bottom <= rect.top)
