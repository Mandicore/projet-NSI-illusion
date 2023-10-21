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
    x = 0
    y = 250

    point_list[0].x, point_list[0].y = x, y

    for i in range(1, len(point_list)):
        if ((i <= 3) or(i >= 10)):
            x += 40
            point_list[i].x = x
        else :
            x -= 40
            point_list[i].x = x
        if (i <= 6):
            y -= 20
            point_list[i].y = y
        else:
            y += 20
            point_list[i].y = y
    return point_list


#def loading_bar_points():

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

