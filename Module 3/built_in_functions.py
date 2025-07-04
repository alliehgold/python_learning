#built in functions are functions native to Python
#They require no external library or class

#print displays the message in the terminal or program
print("Print is a built-in function of python.")

#len() returns the number of items in a sequence such as list, string, or tuple
shopping_list = ["apples", "bananas", "oranges"]

print(len(shopping_list))

name = input("input is also a function that takes user input. What is your name?\n")

print(f"Hello, {name}! We are using the print function again!")

#type() returns the data type of a variable or value

example_num = 17.25

print(f"This variable has a value of {example_num} and its type is {type(example_num)}!") #returns the type of example_num

#int() converts data to an integer
example_num = int(example_num)
print(f"Now, this variable has a value of {example_num} and its type is {type(example_num)}!")

#float() converts data to a decimal
float_num = 25
print(f"Now this number is currently of type {type(float_num)}, with a value of {float_num}!")
float_num = float(float_num)
print(f"Now this number is of type {type(float_num)} with a value of {float_num}!")

#String converts data to a text string
float_num = str(float_num)
print(f"Now the number is of type {type(float_num)} with a value of {float_num}!")
print("Note that while the value appears the same, the type is different")
