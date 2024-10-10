import turtle

#1. (5%)
def get_color(char):
    color_map = {
        '0': 'black',
        '1': 'white',
        '2': 'red',
        '3': 'yellow',
        '4': 'orange',
        '5': 'green',
        '6': 'yellowgreen',
        '7': 'sienna',
        '8': 'tan',
        '9': 'gray',
        'A': 'darkgray'
    }
    result = color_map.get(char, None)  # Getting the color, or returning None if invalid
    print(f"get_color('{char}') -> {result}")  # Debug statement
    return result

# 2. draw_color_pixel(color_string, turta) function (10%)
def draw_color_pixel(color_string, turta):
    print(f"Drawing pixel with color: {color_string}")  # Debug statement
    if color_string:
        turta.fillcolor(color_string)
        turta.begin_fill()
        for _ in range(4):  # Draw a square pixel
            turta.forward(20)
            turta.right(90)
        turta.end_fill()
        turta.forward(20)  # Move to the next position

# 3. draw_pixel(color_string, turta) function (10%)
def draw_pixel(char, turta):
    color_string = get_color(char)  # Get the corresponding color
    if color_string:
        draw_color_pixel(color_string, turta)
        return True
    else:
        print(f"Invalid character: {char}")  # Debug statement for invalid characters
        return False

# 4. draw_line_from_string(color_string, turta) function (15%)
def draw_line_from_string(color_string, turta):
    print(f"Drawing line from string: {color_string}")  # Debug statement
    for char in color_string:
        if not draw_pixel(char, turta):
            print(f"Stopped drawing line. Invalid character encountered: {char}")  # Debug
            return False  # Stop drawing if there's an invalid character
    return True

# 5. draw_shape_from_string(turta) function (20%)
def draw_shape_from_string(turta):
    while True:
        user_input = input("Enter a string of colors (or press enter to stop): ")
        if user_input == "" or not draw_line_from_string(user_input, turta):
            print("Drawing stopped.")  # Debug statement
            break
        turta.penup()
        turta.setx(0)  # Move to the start of the next row
        turta.sety(turta.ycor() - 20)  # Move down one row
        turta.pendown()

# 6. draw_grid(turta) function (15%)
def draw_grid(turta):
    grid_size = 20  # 20x20 grid
    for row in range(grid_size):
        line = ""
        for column in range(grid_size):
            if (row + column) % 2 == 0:
                line = line + '0'  # black
            else:
                line = line + '1'  # white
        draw_line_from_string(line, turta)
        turta.penup()
        turta.setx(0)
        turta.sety(turta.ycor() - 20)
        turta.pendown()

# 7. draw_shape_from_file(turta) function (15%)
def draw_shape_from_file(turta):
    file_path = input("Enter the path of the file that you want to read its content: ")
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()  # Remove newline characters
                print(f"Drawing line from file: {line}")  # Debug statement
                if not draw_line_from_string(line, turta):
                    print(f"Invalid character found in {file_path}. Stopping drawing.")
                    break
                turta.penup()
                turta.setx(0)
                turta.sety(turta.ycor() - 20)
                turta.pendown()
    except FileNotFoundError:
        print(f"File {file_path} not found.")


if __name__ == "__main__":
    screen = turtle.Screen()
    turta = turtle.Turtle()
    turta.speed(0)  # Fastest speed for drawing
    draw_shape_from_string(turta)
    screen.exitonclick()
