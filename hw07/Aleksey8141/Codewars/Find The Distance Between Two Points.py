from math import sqrt

def distance(x1, y1, x2, y2):
    a = (x2 - x1)
    b = (y2 - y1)
    dist = sqrt(a ** 2 + b ** 2)
    return round(dist, 2)


