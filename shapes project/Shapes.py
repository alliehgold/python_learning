#the math library must be imported as we are using pi and pow to calculate the area of the circle
import math


class Triangle:
    # initializing the Triangle Class
    def __init__(self, base, height):
        self.base = base
        self.height = height

    # calculate the area of the triangle
    def get_triangle_area(self):
        # return the area of the triangle
        return round(self.base * self.height * 0.5, 2)


class Circle:
    # initializing the Pircle class
    def __init__(self, radius):
        self.radius = radius

    # calculate the area of the circle
    def get_circle_area(self):
        # return the area of the circle
        return round(math.pi * math.pow(self.radius, 2), 2)


# Calculates the area of a prism, borrowing from the Triangle class
class Prism(Triangle):
    # initializing the Prism class
    def __init__(self, base, height, prism_length):
        super().__init__(base, height)
        self.base = base
        self.height = height
        self.prism_length = prism_length

    # calculate the area of the prism
    def get_prism_volume(self):
        # return the Prism area
        return round(self.get_triangle_area() * self.prism_length, 2)


# Calculates the volume of a cylinder, borrowing from the Circle class
class Cylinder(Circle):
    # initializing the Cylinder class
    def __init__(self, radius, height):
        super().__init__(radius)
        self.radius = radius
        self.height = height

    # calculate the volume of the cylinder
    def get_cylinder_volume(self):
        # return the cylinder volume
        return round(self.get_circle_area() * self.height, 2)
