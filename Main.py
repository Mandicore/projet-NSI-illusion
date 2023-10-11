import turtle

pen = turtle.Turtle()
pen.penup()
pen.goto(0, 0)
pen.dot(10)
turtle.done()

class Point:
    def __init__(self, x, y, dot, color):
        self.x = x
        self.y = y
        self.dot = dot
        self.color = color

def window_configu():
    window = turtle.Screen()
    window.title("Chargement")
    window.bgcolor("#555")
    return window

#def loading_bar_points():

window = window_configu()