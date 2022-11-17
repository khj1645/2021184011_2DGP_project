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
        pico2d.draw_rectangle( self.left,self.top,self.right, self.bottom)

    def collide_rect_to_rect(self,r):
        if self.left > r.right: return False
        if self.right < r.left: return False
        if self.top < r.bottom: return False
        if self.bottom > r.top: return False
        return True
       

    def collide_rect_to_circle(self,circle):
        temp = rect()
        temp.left = self.left - circle.r
        temp.right = self.right + circle.r
        temp.bottom = self.bottom - circle.r
        temp.top = self.top + circle.r
        if circle.x < temp.right and circle.x > temp.left and circle.y > temp.bottom and circle.y < temp.top:
            return True
        if math.sqrt(((circle.x - self.left) ** 2) + ((circle.y - self.bottom) ** 2)) <= circle.r:
            return True
        if math.sqrt(((circle.x - self.left) ** 2) + ((circle.y - self.top) ** 2)) <= circle.r:
            return True
        if math.sqrt(((circle.x - self.right) ** 2) + ((circle.y - self.bottom) ** 2)) <= circle.r:
            return True
        if math.sqrt(((circle.x - self.right) ** 2) + ((circle.y - self.top) ** 2)) <= circle.r:
            return True
        
        return False