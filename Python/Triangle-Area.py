class triangle:
    def __init__(self, h, b):
        self.height=h
        self.base=b

    def triangle_area(self):
        return self.height*self.base/2
    
triangle2=triangle(7,10)
print("Area of Triangle = Base x Height x 0.5")
print("=",triangle2.triangle_area)