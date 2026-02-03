import turtle
import random

#fonction pour dessiner un carrre
def draw_square(size, color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

# fonction pour dessiner un triangle
def draw_triangle(size, color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)

# fonction pour dessiner un cercle
def draw_circle(size, color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(size)

# Paramètres
N = int(input("Entrez un nombre entre 0 et 9 : "))

# liste des forme  et couleur possible 
shapes = [draw_square, draw_triangle, draw_circle]
colors = ["red", "blue", "green", "purple", "orange"]

# Dessin des forme 
turtle.speed(0)
for _ in range(N):
    shape = random.choice(shapes)
    size = random.randint(20, 100)
    color = random.choice(colors)
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    shape(size, color, x, y)

turtle.done()
