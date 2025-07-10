
#the math library must be imported as we are using pi and pow to calculate the area of the circle
import math

class Triangle():
  #initializing the Triangle Class
  def __init__(self, base, height):
    self.base = base
    self.height = height
  
  #calculate the area of the triangle
  def get_triangle_area(self):
    #return the area of the triangle
    return round(self.base * self.height * 0.5, 2)
    

class Circle():
  #initializing the Pircle class
  def __init__(self, radius):
    self.radius = radius

  #calculate the area of the circle 
  def get_circle_area(self):
     #return the area of the circle
     return round(math.pi*math.pow(self.radius, 2), 2)
  
class Prism():
  #initializing the Prism class
  def __init__(self, base, height, prism_length):
      self.base = base
      self.height = height
      self.prism_length = prism_length

  #calculate the area of the prism
  def get_prism_volume(self):
    #because the area of a triangle is needed, we can use the Triangle class to calculate this
    triangle = Triangle(self.base, self.height)
    #return the cylinder volume
    return round(triangle.get_triangle_area()*self.prism_length, 2)

class Cylinder():
  #initializing the Cylinder class
  def __init__(self, radius, height):
    self.radius = radius
    self.height = height

  #calculate the volume of the cylinder
  def get_cylinder_volume(self):
    #since the volume is determined by the area of a circle, we can use the Circle class to calculate this
    circle = Circle(self.radius)
    #return the cylinder volume
    return round(circle.get_circle_area()*self.height, 2)
