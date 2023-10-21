import turtle
import math

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
        point_list.append(Point(50, "red"))
    return point_list

def Point_axes(point_list):
    num_points = len(point_list)
    radius = 150
    center = 0

    # Calcule l'angle entre chaque point
    angle_step = 360 / num_points

    for i in range(num_points):
        angle_degrees = i * angle_step
        angle_radians = math.radians(angle_degrees)
        point_list[i].x = center + radius * math.cos(angle_radians)
        point_list[i].y = center + radius * math.sin(angle_radians)
    return point_list

window = window_configu()
turtle.hideturtle()
pen = turtle.Turtle()
pen.penup()
##test
point_list = Point_axes(Create_Point_List())
for p in point_list:
    Point.Draw_Point(p)

##test

turtle.penup()
turtle.done()

