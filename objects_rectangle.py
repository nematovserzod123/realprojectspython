class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rectangle(self, rectangle):
        if rectangle.lowleft.x  < rectangle.upright.x   \
        and rectangle.lowleft.y < rectangle.upright.y:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright
    
    def Area(self):
        return(self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)
