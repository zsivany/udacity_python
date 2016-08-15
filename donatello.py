import turtle

def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_shapes():

    window=turtle.Screen()
    window.bgcolor("red")
    
    donatello = turtle.Turtle()
    donatello.color("white")
    donatello.shape("turtle")
    donatello.speed(5)
    
    for i in range(36):
        draw_square(donatello)
        donatello.right(10)
    
    

    leonardo = turtle.Turtle()
    leonardo.color("blue")
    leonardo.shape("classic")
    leonardo.circle(50)
    
    raffaelo = turtle.Turtle()
    raffaelo.color("black")
    raffaelo.shape("triangle")

                
    raffaelo.forward(100)
    raffaelo.left(120)  
    raffaelo.forward(100)
    raffaelo.left(120)
    raffaelo.forward(100)

    window.exitonclick()

draw_shapes()
