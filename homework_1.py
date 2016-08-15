import turtle

def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_rhomb(some_turtle):
    some_turtle.forward(100)
    some_turtle.right(60)
    some_turtle.forward(100)
    some_turtle.right(120)
    some_turtle.forward(100)
    some_turtle.right(60)
    some_turtle.forward(100)

def draw_shapes():

    window=turtle.Screen()
    window.bgcolor("red")
    
    donatello = turtle.Turtle()
    donatello.color("white")
    donatello.shape("turtle")
    donatello.speed(30)
    #draw_rhomb(donatello)
    
    #for i in range(36):
        #donatello.right(10)
        #draw_square(donatello)

    #draw flower
    for i in range(36):
        donatello.right(10)
        draw_rhomb(donatello)

    #draw stalk
    donatello.right(90)
    donatello.forward(400)
    

    window.exitonclick()

draw_shapes()
