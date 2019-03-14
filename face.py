##drawFace (center, size, win) center is a Point, size is an int, and
##win is a GraphWin. Draws a simple face of the given size in win.
##Your function can draw a simple smiley (or grim) face. Demonstrate the
##function by writing a program that draws several faces of varying size in a
##single window
 
#!/usr/local/bin/python3

from graphics import *
 
win = GraphWin('Smiley Faces', 400, 400) # give title and dimensions
win.setBackground('cyan')
win.setCoords(0, 0, 400, 400)
 
def drawFace(center, size,window):
 
    head = Circle(center,size*20)
    head.setFill("green")
    head.draw(win)
 
    mouth = Circle(center, size*13)
    mouth.setFill("red")
    mouth.setOutline("red")
    mouth.draw(win)
    smile = Circle(center, size*14)
    smile.move(0,size*4)
    smile.setFill("green")
    smile.setOutline("green")
    smile.draw(win)
 
    eyebrow = Circle(center,size*4)
    eyebrow.move(-size*8,size*10)
    eyebrow.setFill('black')
    eyebrow.draw(win)
    eyebrow2 = eyebrow.clone()
    eyebrow2.draw(win)
    eyebrow2.move(size*16, 0)
    eyecircle = Circle(center,size*4)
    eyecircle.move(-size*8,size*9)
    eyecircle.setFill('green')
    eyecircle.setOutline('green')
    eyecircle.draw(win)
    eyecircle2 = eyecircle.clone()
    eyecircle2.draw(win)
    eyecircle2.move(size*16, 0)
 
    eyelid = Circle(center,size*3)
    eyelid.move(-size*8,size*8)
    eyelid.setFill('brown')
    eyelid.draw(win)
    eyelid2 = eyelid.clone()
    eyelid2.draw(win)
    eyelid2.move(size*16, 0)
 
    eye = Circle(center, size*3)
    eye.move(-size*8,size*6)
    eye.setFill('orange')
    eye.draw(win)
    eye2 = eye.clone()
    eye2.draw(win)
    eye2.move(size*16, 0)
 
    pupil = Circle(center,size)
    pupil.move(-size*9,size*7)
    pupil.setFill('blue')
    pupil.draw(win)
    pupil2 = pupil.clone()
    pupil2.draw(win)
    pupil2.move(size*16,0)
 
    nose = Circle(center,size*3)
    nose.move(0,-size*2)
    nose.setOutline('yellow')
    nose.setFill('yellow')
    nose.draw(win)
 
def main():
 
    i = 0
    for i in range (1,5):
        center = Point(350,490-i*110)#top to bottom, increasing radius
        Face = drawFace(center,i*.8,win)
        center = Point(-50+i*85,-50+i*90)#bottom left to top right, decreasing radius
        Face = drawFace(center,3-(i*.5),win)
        center = Point(340-i*75,-65+i*100)#bottom right to top left, increasing radius
        Face = drawFace(center,i,win)
 
    message = Text(Point(200, 380), 'Click anywhere to quit.')
    message.setFill('blue')
    message.draw(win)
    win.getMouse()
    win.close()
 
main()
