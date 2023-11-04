#Projet crée par HEQUET Romain, DEMOURA William et FIGUEIRAS Jossua in 2023
import turtle
import math
from time import sleep

#nombre de points dans l'annimation
NB_POINT = 12
class Point:
    def __init__(self, dot, color, x = None, y = None):
        """défini l'objet point"""
        self.dot = dot
        self.color = color
        self.x = x
        self.y = y
    
    def Draw_Point(point):
        """place le point en paramètre sur la fenêtre"""
        pen.color(point.color)
        pen.goto(point.x, point.y)
        pen.dot(point.dot)

def window_configu():
    """donne les paramètre à la fen^tre"""
    window = turtle.Screen()
    window.title("Illusion par Romain, Wiliam et Jossua")
    window.bgcolor("#b2b2b2")
    #def la taille de la fenêtre
    window.setup(width=900, height=600) 
    #récupérer les informations de la fenêtre au premier plan (la seul ici)
    root = window.getcanvas().winfo_toplevel()
    #Interdit la redimention de la fenêtre récupéré sur la ligne précédente
    root.resizable(False, False)
    return window

def Create_Point_List():
    """Crée et return la liste de point avec des points sans coordonnées x et y"""
    point_list = []
    for i in range(NB_POINT):
        point_list.append(Point(50, "magenta"))
    return point_list

def Point_axes(point_list):
    """donne les coordonné de chaque points de la liste de point mis en paramètre"""
    radius = 150
    #centre du rond autour duquel les points vont ce mettre en place
    center = 0
    angle_step = 360 / NB_POINT
    for i in range(NB_POINT):
        angle_degrees = i * angle_step
        angle_radians = math.radians(angle_degrees)
        point_list[i].x = center + radius * math.cos(angle_radians)
        # - math.sin(angle_radians) , le - sert à faire apparaitre les points dans le 
        #sens des aiguilles d'une montre
        point_list[i].y = center + radius * - math.sin(angle_radians)
    return point_list

def Create_Cross(pen):
        """Crée la croix au centre de la fenêtre"""
        pen.penup()
        #change la taille de pen
        pen.width(3)
        pen.goto(-8, 0)
        pen.pendown() 
        pen.goto(8, 0)
        pen.penup()
        pen.goto(0, -8)
        pen.pendown()
        pen.goto(0, 8)


def Animation_Point(list_point):
    """Animation des points qui donne l'effet de chargement et
    l'effet d'optique"""
    base_color = list_point[1].color
    while (True):
        for point in list_point:
            point.color = window.bgcolor()
            Point.Draw_Point(point)
            point.color = base_color
            Point.Draw_Point(point)

def pen_settings():
    """return pen avec tous les paramètres"""
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed("fastest")
    return pen

window = window_configu()
pen = pen_settings()
Create_Cross(pen)
pen.penup()
point_list = Point_axes(Create_Point_List())
for p in point_list:
    Point.Draw_Point(p)
sleep(0.250)
Animation_Point(point_list)
turtle.done()