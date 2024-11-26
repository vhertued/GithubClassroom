import pytest
from polygon import Polygon

def test_polygon_initialization():
    polygon = Polygon(name="Triangle", sides=[3.0, 3.0, 3.0])    # Creating the polygon object

    assert polygon.get_name() == "Triangle"                      # Assert that object is initialized with correct name
    assert polygon.get_sides() == [3.0, 3.0, 3.0]                # Assert that object is initialized with correct sides

def test_polygon_name_methods():
    polygon = Polygon(name="Square", sides=[4.0, 4.0, 4.0])      # Creating the polygon object

    assert polygon.get_name() == "Square"                        # Assert that the getter returns correct name
    assert polygon.get_sides() == [4.0, 4.0, 4.0]                # Assert that the getter returns correct sides

    polygon.set_name("Hexagon")                                  # Use the setter to change name to Hexagon

    assert polygon.get_name() == "Hexagon"                       # Assert that the getter returns the UPDATED name


def test_polygon_sides_methods():
    polygon = Polygon(name="Hexagon", sides=[6.0, 6.0, 6.0])     # Creating the polygon object

    assert polygon.get_sides() == [6.0, 6.0, 6.0]                # Assert that the getter returns correct data

    polygon.set_sides([5.0, 5.0, 5.0])                           # Use the setter to change the sides

    assert polygon.get_sides() == [5.0, 5.0, 5.0]                # Assert that the getter returns the UPDATED sides 


def test_polygon_equality():
    polygon1 = Polygon(name="Triangle", sides=[3.0, 3.0, 3.0])   # Creating two identical polygon objects
    polygon2 = Polygon(name="Triangle", sides=[3.0, 3.0, 3.0])   

    assert polygon1 == polygon2                                  # Assert that equality operator works correctly

def test_polygon_inequality():
    polygon1 = Polygon(name="Triangle", sides=[3.0, 3.0, 3.0])   # Creating two different polygon objects
    polygon2 = Polygon(name="Square", sides=[3.0, 3.0, 3.0])    
    polygon3 = Polygon(name="Triangle", sides=[4.0, 4.0, 4.0])   

    assert polygon1 != polygon2                                  # Assert that polygons with different names are not equal
    assert polygon1 != polygon3                                  # Assert that polygons with different sides are not equal

def test_polygon_str():                                          # Testing the string representation
    polygon = Polygon(name="Pentagon", sides=[5.0, 5.0, 5.0, 5.0, 5.0]) 
    expected_str = "Pentagon with sides: [5.0, 5.0, 5.0, 5.0, 5.0]"  # Expected string representation

    assert str(polygon) == expected_str                          # Assert that __str__ method returns the expected format