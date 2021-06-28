import turtle

myPen = turtle.Turtle()
myPen.tracer(5)
myPen.speed(5)
myPen.color("yellow")

def box(intDim):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)

boxSize = 25
#Position myPen in top left area of the screen
myPen.penup()
myPen.forward(-100)
myPen.setheading(90)
myPen.forward(100)
myPen.setheading(0)

pixels     = [[0,0,0,0,0,0,1,1,1,0,0]]
pixels.append([0,0,0,0,0,1,1,1,1,1,0])
pixels.append([0,0,0,0,1,1,1,1,1,1,0])
pixels.append([0,1,0,0,1,1,1,1,1,1,1])
pixels.append([1,1,1,1,1,1,1,1,1,1,0])
pixels.append([1,1,1,1,1,1,1,1,1,0,0])
pixels.append([0,0,1,1,1,1,1,1,1,0,0])
pixels.append([0,0,0,1,1,1,1,1,0,0,0])


for i in range (0,len(pixels)):
    for j in range (0,len(pixels[i])):
		if pixels[i][j]==1:
			box(boxSize)
		myPen.penup()
		myPen.forward(boxSize)
		myPen.pendown()	
    myPen.setheading(270) 
    myPen.penup()
    myPen.forward(boxSize)
    myPen.setheading(180) 
    myPen.forward(boxSize*len(pixels[i]))
    myPen.setheading(0)
    myPen.pendown()
	
myPen.getscreen().update()	