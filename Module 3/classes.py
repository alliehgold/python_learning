#Classes are blueprints for creating objects
#Classes are a combination of methods, functions, and characteristics
#Classes are essentially a blueprint that is used to create multiple objects
#based on the class's data and functionality

#We are importing the Car class from the CarClass module
from CarClass import Car

my_car = Car("Toyota", "Prius", 2015, "teal")

#This prints the attributes of the my_car object created from CarClass
print(f"My car is a {my_car.color} {my_car.year} {my_car.make} {my_car.model}.")

#These are methods contained with in the Car class
#The paranthesies are required even though we do not have any attributes
my_car.start_engine()
my_car.accelerate()
my_car.brake()

#Classes have 3 important abilities:
#Encapsulation
#Inheritence
#Polymorphism


#Encapsulation:
#Classes bundle together data and the functions that operate on the data
#This creates self-contained  units of code
#This promotes organization and modularity


#Inheritence:
#Classes can inherit attributes and methods from other classes
#This allows for a hierarchical relationship


#Polymorphism
#Polymorphism allows objects of different classes to respond to the same
#function call in their own, unique way
#This provides flexibility and flexibility


#Key components:
#The attributes are variables that store data specific to each object of the class
#They define the properties of the object
#Methods are functions in the class that represent the actions or
#behaviors an object can perform
#The constructor is automatically called when you create an object of a class
#The constructor initializes the object's attributes and sets the initial values


#When a class is defined, you can create an instance of that class
#This is called instantiation



