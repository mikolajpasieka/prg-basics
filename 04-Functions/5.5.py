###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import figures
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)   

## Draw figures
pen.penup()
pen.goto(-100, 100)
pen.pendown()
print(figures.draw_square(100))
pen.penup()
pen.goto(0, 0)
pen.pendown()
print(figures.draw_square(100))
pen.penup()
pen.goto(100, -100)
pen.pendown()
print(figures.draw_triangle(100))
pen.penup()
pen.goto(50, -50)
pen.pendown()
print(figures.draw_triangle(100))
pen.penup()
pen.goto(20, -20)
pen.pendown()
print(figures.draw_rectangle(100,200))
pen.penup()
pen.goto(-20, 20)
pen.pendown()
print(figures.draw_rectangle(100,200))

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()