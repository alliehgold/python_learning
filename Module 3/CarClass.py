
#classes contain their own functions, or methods, that can be called via an instance
#You can explain a class using a docstring which can be used by typing '''

"""
The car class allows you to create a car object with info about what kind of car it is.

Args:
    make:   The manufacturer of the car (str).
    model:  The model of the car (str).
    year:   The year of the car (int).
    color:  The color of the car (str).

Methods:
    start_engine:   Indicates that the engine is turned on.
    accelerate:     Indicates that the car is picking up speed.
    brake:          Indicates that the car has come to a stop.

Raises:
     NameError: If any strings are not in quotes.

Example:
    >>> Car("Chevrolet", "Corvette", 2010, "Red")
"""

class Car:
    # __init__ is a constructor. it is called when you create a new object of this class.
    # This function initializes the object's attributes and assigns them their default values
    def __init__(self, make: str, model: str, year: int, color: str):

        #These assign the variables 
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_level = 100 #initial fuel level
    
    #Methods are functions that are defined within the class

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine roars to life!")

    def accelerate(self):
        print(f"The {self.color} {self.make} {self.model} picks up speed!")

    def brake(self):
        print(f"The {self.make} {self.model} comes to a smooth stop.")