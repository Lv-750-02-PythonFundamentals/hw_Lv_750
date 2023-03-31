def distance(x1, y1, x2, y2):
    calculated_distance = (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
    return round(calculated_distance, 2)


print(distance(3, 4, 4, 3))
