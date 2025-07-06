#Functions are reusable blocks of code that offer organization, reusability, and abstraction
#There are multiple built in functions such as print and len
#There are also user defined functions, which are functions that a user creates
#Lastly, there are lambda functions, which are often used for simple operations or as arguments for other functions
#define a function with the def command followed by the function name. the variables in the parenthasies are arguments
def final_price(sale_amount, tax_percent):
    tax_amount = sale_amount * (tax_percent/100.0)

    total_price = sale_amount + tax_amount
    #functions end with a return statement
    return total_price


#Note that the function must be created before it gets called since Python interprets the code line-by-line
#This function can now be called
print("Your final price is $", final_price(100, 8))

# Further notes:
# The naming convention for functions is snake_case
# Avoid generic names
# Keep the vocabulary consistent
# prioritize clerity over short names
# For functions that return a boolean value, consider prefixes such as is_, has_, or can_ to signal their nature

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return float(fahrenheit)
    
def fahrenheit_to_celsius(fahrenheit):
    celsius = (float(fahrenheit) - 32) * 5/9
    return float(celsius)

def convert_temperature(temperature, unit):
    if unit == 'C':
        return celsius_to_fahrenheit(temperature)
    elif unit == 'F':
        return fahrenheit_to_celsius(temperature)
    
temperature_c = 25
converted_c = convert_temperature(25, 'C')

print(f"{temperature_c} in celsius is {converted_c} in fahrenheit")

