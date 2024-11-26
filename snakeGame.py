import turtle
import time
import random

# Variables
delay = 0.01
score = 0
heigh_score = 0

# Setup window
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("#000087")
window.setup(width=600, height=600)
window.tracer(0)

# Snake Head
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.speed(0)

head.direction = "stop"

# Food
food = turtle.Turtle()
colors = random.choice(["red", "green", "blue"])  # Randomly choose a color
shapes = random.choice(["square", "circle"])  # Randomly choose a shape
food.color(colors)
food.shape(shapes)
food.penup()
food.speed(0)
food.goto(0, 100)

# Pen (Score Display)
pen = turtle.Turtle()
pen.shape("square")
pen.color("white")  # Set a valid color
pen.speed(0)
pen.penup()  # Prevent the pen from drawing when moving
pen.goto(0, 260)  # Move it to a proper display position
pen.hideturtle()
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Keep the turtle window open at the end
turtle.done()
