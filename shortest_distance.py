import math


def distance(x1, y1, x2, y2):  # this function finds the distance between two points (x1,y1) and (x2,y2)
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 4)
