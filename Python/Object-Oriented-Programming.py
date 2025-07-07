class rectangle:
    def __init__(self, l, w):
        self.length=l
        self.width=w

    def rectangle_area(self):
        return self.length*self.width
    
newRectangle= rectangle(20, 7)
print("Rectangle length :",newRectangle.length," width :",newRectangle.width)
print("Area of Rectangle :",newRectangle.rectangle_area())