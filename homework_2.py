import turtle

def monogram():
    window = turtle.Screen()
    window.bgcolor("green")

    monogram_t = turtle.Turtle()

    monogram_t.color("black")
    monogram_t.speed(1)
    monogram_t.forward(150)
    monogram_t.left(180)
    monogram_t.forward(75)
    monogram_t.left(90)
    monogram_t.forward(200)

    
    monogram_p = turtle.Turtle()
    monogram_p.home()
    monogram_p.color("brown")


    monogram_p.left(90)
    monogram_p.fd(350)
    monogram_p.right(90)
    monogram_p.fd(50)
    monogram_p.circle(-80, 180)
    monogram_p.fd(50)
    
    

    window.exitonclick()

monogram()


