import turtle
import matplotlib
matplotlib.use('Agg')

smiles = turtle.Turtle()    
smiles.penup()
smiles.goto(-75,150)
smiles.pendown()
smiles.circle(10)     #eye one

smiles.penup()
smiles.goto(75,150)
smiles.pendown()
smiles.circle(10)     #eye two

smiles.penup()
smiles.goto(0,0)
smiles.pendown()
smiles.circle(100,90)   #right smile

smiles.penup()           
smiles.setheading(180) # <-- look West
smiles.goto(0,0)
smiles.pendown()
smiles.circle(-100,90)
