import math


def calculate_street_width(x, y, c):
    w = 2 * math.sqrt(y**2 - c**2) + x
    return round(w, 3)


x, y, c = map(float, input().split())
print(calculate_street_width(x, y, c))
