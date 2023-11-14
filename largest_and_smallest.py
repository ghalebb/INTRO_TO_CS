# I chose the first case (-1,0,1) to check if my function works on negative and positive as it should
# in the second case I chose three negative numbers to checks if the function returns true values in negative

def largest_and_smallest(x, y, z):
    """ This function calculates the max and min among three numbers"""
    maximum = minimum = x
    for num in [x, y, z]:
        if num > maximum:
            maximum = num
        elif num < minimum:
            minimum = num
    return maximum, minimum


def check_largest_and_smallest():
    """ This function tests if the largest_and_smallest function works according to five tests"""
    if largest_and_smallest(17, 1, 6) != (17, 1):
        return False
    if largest_and_smallest(1, 17, 6) != (17, 1):
        return False
    if largest_and_smallest(1, 1, 2) != (2, 1):
        return False
    if largest_and_smallest(-1, 0, 1) != (1, -1):
        return False
    if largest_and_smallest(-100, -23, -19) != (-19, -100):
        return False
    return True
