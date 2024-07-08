"""Dummy challenge for Kitt Demo"""



def circle_area(radius):
    """Returns the area of the circle of given radius"""
    area = radius * radius * 3.14
    if radius < 0:
        return 0
    return area
