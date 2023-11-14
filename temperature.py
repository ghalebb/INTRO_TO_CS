def is_it_summer_yet(temperature, first, second, third):
    """ this function checks if there are two temps above the given temp"""
    if first > temperature and second > temperature:
        return True
    elif first > temperature and third > temperature:
        return True
    elif second > temperature and third > temperature:
        return True
    return False
