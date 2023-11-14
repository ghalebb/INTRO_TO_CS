import math

CHOICE_CIRCLE = "1"
CHOICE_RECTANGLE = "2"
CHOICE_TRIANGLE = "3"


def shape_area():
    """This function calculates the area of
   10 one of three shapes according to the user's choice
   11 (Circle, Rectangle or triangle)"""
    choice = input("Choose shape (1=circle, 2=rectangle, 3=triangle): ")
    if choice == CHOICE_CIRCLE:  # Checking the user's choice
        return circle_area()
    elif choice == CHOICE_RECTANGLE:
        return rectangle_area()
    elif choice == CHOICE_TRIANGLE:
        return triangle_area()
    else:  # if the user didn't enter one of the three choices the function
        # returns None
        return


def circle_area():
    """This function calculates the circle area"""
    radius = input()
    area = math.pi * float(radius) ** 2
    return area


def rectangle_area():
    """This function calculates the rectangle area"""
    a = input()
    b = input()
    area = float(a) * float(b)
    return area


def triangle_area():
    """This function calculates the triangle area"""
    side = input()
    area = (3 ** 0.5 / 4) * (float(side) ** 2)
    return area
