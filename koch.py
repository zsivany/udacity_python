import turtle

def koch_fractal(my_turtle, order, size):
    
    
    if order==0:
        my_turtle.forward(size)
    else:
        koch_fractal(my_turtle, order-1, size/3)
        my_turtle.left(60)
        koch_fractal(my_turtle, order-1, size/3)
        my_turtle.right(120)
        koch_fractal(my_turtle, order-1, size/3)
        my_turtle.left(60)
        koch_fractal(my_turtle, order-1, size/3)

window = turtle.Screen()
window.bgcolor("red")

brad=turtle.Turtle()
brad.tracer(8,25)
brad.speed(10)

koch_fractal(brad, 1, 100)

window.exitonclick()
