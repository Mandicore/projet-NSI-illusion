import turtle

NB_POINT = 12

class Point:
    def __init__(self, dot, color, x = None, y = None):
        self.dot = dot
        self.color = color
        self.x = x
        self.y = y
    
    def Draw_Point(Point):
        pen.goto(Point.x, Point.y)
        pen.dot(Point.dot)

def window_configu():
    window = turtle.Screen()
    window.title("Chargement")
    window.bgcolor("#555")
    return window

def Create_Point_List():
    """Create a point list without value for x and y"""
    point_list = []
    for i in range(NB_POINT):
        point_list.append(Point(10, "red"))
    return point_list

def Point_axes(point_list):
    """Return point list with x and y value"""



#def loading_bar_points():

window = window_configu()
turtle.hideturtle()
pen = turtle.Turtle()
turtle.penup()
Point.Draw_Point(Point(30, "red", 0, 50 ))
turtle.done()
