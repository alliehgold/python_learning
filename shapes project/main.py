from Shapes import *

triangle = Triangle(10, 11.5)
circle = Circle(13.75)
prism = Prism(10, 11.5, 5)
cylinder = Cylinder(13.75, 6.75)

print(f"The area of the triangle is {triangle.get_triangle_area()}")
print(f"The area of the circle is {circle.get_circle_area()}")
print(f"The volume of the prism is {prism.get_prism_volume()}")
print(f"The volume of the cylinder is {cylinder.get_cylinder_volume()}")
