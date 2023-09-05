import math


def distance_between_points(p1, p2):
    """Returns the distance between two points."""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
