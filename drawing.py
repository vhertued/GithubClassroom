import turtle
from pixart import draw_shape_from_string, draw_grid, draw_shape_from_file

if __name__ == "__main__":
    screen = turtle.Screen()
    turta = turtle.Turtle()
    turta.speed(0)  # Fastest speed for drawing
    draw_shape_from_file(turta)

    screen.exitonclick()
