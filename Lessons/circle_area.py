'Area of a circle = pi * r**2'

pi = 3.1416


def area_circle(radius):
    'Function that calculates the area of a circle'
    area = pi * int(radius) ** 2
    return area

radius = raw_input('Give the Radius of the circle in cm: ')
area = area_circle(radius)
print "The area of a circle of radius ", radius
print "cm is", area, "cm^2"
