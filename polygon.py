class Polygon:
    def __init__(self, name: str, sides: list):     # Initializing with name and sides
        self.__name = name                          # name is str format
        self.__sides = sides                        # sides is a list of floats

    def get_name(self):                             # Getter for name
        return self.__name
     
    def set_name(self, name: str):                  # Setter for name
        self.__name = name
    
    def get_sides(self):                            # Getter for sides
        return self.__sides
    
    def set_sides(self, sides: list):               # Setter for sides
        self.__sides = sides

    def __eq__(self, other):                        # Equality method, checks if two polygons are equal
        return self.__name == other.get_name() and self.__sides == other.get_sides()

    def __ne__(self, other):                        # Inequality method, opposite of __eq__
        return not self.__eq__(other)

    def __str__(self):                              # String representation method
        return f"{self.__name} with sides: {self.__sides}"
    
    def calculate_circumference(self):
        return sum(self.__sides)

def main():
    # Instantiate Polygon objects
    triangle = Polygon(name="Triangle", sides=[3.0, 4.0, 5.0])  # A triangle with side lengths 3, 4, 5
    square = Polygon(name="Square", sides=[4.0, 4.0, 4.0, 4.0])  # A square with all sides equal to 4
    hexagon = Polygon(name="Hexagon", sides=[6.0, 6.0, 6.0, 6.0, 6.0, 6.0])  # A regular hexagon

    # Print string representations and calculated circumferences
    for polygon in [triangle, square, hexagon]:
        print(polygon)  # Uses the __str__ method
        print(f"Circumference: {polygon.calculate_circumference():.2f}")
        print("-" * 40)  # Separator for better readability

# Add the main block
if __name__ == "__main__":
    main()
