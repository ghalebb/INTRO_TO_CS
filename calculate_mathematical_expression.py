def calculate_mathematical_expression(first_num, second_num, sign):
    """ This function executes a mathematical operation according to the given sign"""
    if sign == '+':
        return first_num + second_num
    elif sign == '-':
        return first_num - second_num
    elif sign == '*':
        return first_num * second_num
    elif sign == ':' and second_num != 0:  # making sure there is no zero division
        return first_num / second_num
    return None


def calculate_from_string(single_string):
    """ This function translates a string with mathematical expression to a result"""
    a, op, b = single_string.split(" ")
    a = float(a)
    b = float(b)
    return calculate_mathematical_expression(a, b, op)
