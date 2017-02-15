import turtle

def draw_square(some_turtle):
	for i in range (0,4):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor('red')
	# Create Brad the turtle 
	brad = turtle.Turtle()
	brad.shape('turtle')
	brad.color('yellow')
	brad.speed(2)

	for i in range (0,36):
		draw_square(brad)
		brad.right(10)

	window.exitonclick()
draw_art()