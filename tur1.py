/usr/local/bin/python3

import turtle

playground = turtle.Screen()       # use nouns for objects, play is a verb

playground.bgcolor("black")
playground.screensize(250, 250)
playground.title("Turtle Keys")

tom = turtle.Turtle()              # use nouns for objects, run is a verb

tom.color("white")
tom.setposition(130, 100)
tom.speed("fastest")
tom.color("white")

p = tom.pos()               # here you get the coordinates of the turtle
tom.write(str(p), True)     # and you print a string representation on screen
tom.penup()

print(p)                    # this prints to the console

playground.exitonclick()
