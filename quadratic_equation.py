def quadratic_equation(a, b, c):
    """ This function calculates the solutions of a quadratic equation"""
    d = b ** 2 - (4 * a * c)
    if d < 0:
        return None, None
    elif d == 0:
        x = (-b + d ** 0.5) / 2 * a
        return x, None
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2


def quadratic_equation_user_input():
    """ This function calculates and gives the user the solution of
     quadratic equation according to the user's equation components choice"""
    parameters = input("Insert coefficients a, b, and c: ")
    a, b, c = parameters.split(" ")
    a, b, c = float(a), float(b), float(c)
    if a == 0:
        print("The parameter 'a' may not equal 0")
        return
    sol1, sol2 = quadratic_equation(a, b, c)
    if sol1 is not None and sol2 is not None:
        print("The equation has 2 solutions:", sol1, "and", sol2)
    elif sol1 is not None and sol2 is None:
        print("The equation has 1 solution:", sol1)
    elif sol1 is None and sol2 is not None:
        print("The equation has 1 solution:", sol2)
    else:
        print("The equation has no solutions")
    return


print(quadratic_equation(2,26,72))