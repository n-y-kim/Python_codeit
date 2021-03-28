class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14*self.radius*self.radius

class Square:
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length**2