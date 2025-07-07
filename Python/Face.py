import turtle
class Face:
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

    def drawOutline(self):
        self.penup()
        self.forward(self.size)
        self.left(90)
        self.pendown()
        self.circle(self.size)
        self.goHome()