import math


def distancia(point_1, point_2):
    dist = (point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2
    return math.sqrt(dist)