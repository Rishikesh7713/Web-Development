import turtle
class Face(turtle.Turtle):
    def __init__(self, xpos, ypos):
        self.size=90
        self.coord=(xpos,ypos)
        self.noseSize='small'
    
    def setSize(self, radius):
        self.size=radius

    def draw(self):
        self.goHome()
        self.pensize(3)
        self.speed(0)
        self.drawOutline()
        self.drawEye(135)
        self.drawEye(45)
        self.drawMouth()
        self.drawNose()
        self.pensize(5)

    def goHome(self):
        self.penup()
        self.goto(self.coord)

        self.setheading(0)


    def drawOutline(self):
        self.penup()
        self.forward(self.size)
        self.left(90)
        self.pendown()
        self.circle(self.size)
        self.goHome()

    def drawEye(self, turn):
        self.penup()
        self.left(turn)
        self.forward(self.size/2)
        self.pendown()
        self.dot(self.size/10)
        self.goHome()

    def drawMouth(self):
        self.penup()
        self.right(135)
        self.forward(self.size/1.7)
        self.left(90)
        self.pendown()
        self.circle(self.size/1.7,90)
        self.goHome()

    def drawNose(self):
        if self.noseSize == 'large':
            self.dot(self.size/2, "grey")
        elif self.noseSize == 'small':
            self.dot(self.size/6, "grey")
        else:
            self.dot(self.size/4, "grey")
            self.goHome()

f1= Face(0, 0)
f1.draw()
    
turtle.done