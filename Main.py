#Project created by HEQUET Romain and FIGUEIRAS Jossua in 2023
import turtle
import math
import time

NB_POINT = 12
class Point:
    def __init__(self, dot, color, x = None, y = None):
        self.dot = dot
        self.color = color
        self.x = x
        self.y = y
    
    def Draw_Point(point):
        pen.color(point.color)
        pen.goto(point.x, point.y)
        pen.dot(point.dot)

def window_configu():
    window = turtle.Screen()
    window.title("Illusion par Romain et Jossua")
    window.bgcolor("grey")
    #defind window size
    window.setup(width=900, height=600) 
    #get information of Tkinter window (top level =  principal window)
    root = window.getcanvas().winfo_toplevel()
    #it's impossible to resise windows on x and y axes
    root.resizable(False, False)
    return window

def Create_Point_List():
    """Create a point list without value for x and y"""
    point_list = []
    for i in range(NB_POINT):
        point_list.append(Point(50, "magenta"))
    return point_list

def Point_axes(point_list):
    """def point position of all point of point_list"""
    radius = 150
    #center of the circle
    center = 0
    angle_step = 360 / NB_POINT
    for i in range(NB_POINT):
        angle_degrees = i * angle_step
        angle_radians = math.radians(angle_degrees)
        point_list[i].x = center + radius * math.cos(angle_radians)

        # use - math.sin(angle_radians) so that the points appear in a clockwise direction
        point_list[i].y = center + radius * - math.sin(angle_radians)
    return point_list

def Create_Cross():
        """Create the cross in the middle of window"""
        pen.penup()
        pen.width(3)
        pen.goto(-8, 0)
        pen.pendown() 
        pen.goto(8, 0)
        pen.penup()
        pen.goto(0, -8)
        pen.pendown()
        pen.goto(0, 8)

def Animation_Point(list_point):
    base_color = list_point[1].color
    while (True):
        for point in list_point:
            point.color = window.bgcolor()
            Point.Draw_Point(point)
            point.color = base_color
            Point.Draw_Point(point)



window = window_configu()
pen = turtle.Turtle()
pen.hideturtle()
pen.speed("fastest")
Create_Cross()
pen.penup()
point_list = Point_axes(Create_Point_List())
for p in point_list:
    Point.Draw_Point(p)
Animation_Point(point_list)
turtle.penup()
turtle.done()

