import turtle

janela =turtle.Screen()
janela.setup(width=800, height=600)
janela.bgcolor("white")
janela.title("Feliz dia dos namorados!")

pen = turtle.Turtle()
pen.color("red")
pen.fillcolor("red")
pen.pensize(3)
pen.speed(12)

pen.up()
pen.goto(0, -100)
pen.down()

pen.begin_fill()
pen.left(140)
pen.forward(224)
for _ in range(200):
    pen.right(1)
    pen.forward(2)
pen.left(120)
for _ in range(200):
    pen.right(1)
    pen.forward(2)
pen.forward(224)
pen.end_fill()

pen.up()
pen.goto(0, -170)
pen.down()

pen.color("black")
pen.write("Para você que roubou meu coração \nFeliz dia dos namorados, te amo!",
          align="center", font=("Montserrat", 14, "bold"))



pen.hideturtle()

turtle.done()