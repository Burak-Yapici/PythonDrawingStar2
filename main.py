import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("Lightblue")
drawing_board.title("Bro Turtle")

turtle_instance = turtle.Turtle()
for i in range(5):

    turtle_instance.right(144)
    turtle_instance.forward(100)

turtle.done