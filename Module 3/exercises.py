print("This is a simple calculator!")

first_num = float(input("Please enter the first number you would like to use\n"))

second_num = float(input("Please enter the second number you would like to use\n"))

#performing each of the arithmitic oeprations
print(f"{first_num} plus {second_num} is {first_num + second_num}.\n")
print(f"{first_num} minus {second_num} is {first_num - second_num}.\n")
print(f"{first_num} times {second_num} is {first_num * second_num}\n")
print(f"{first_num} divided by {second_num} is {first_num / second_num}\n")

#takes user input for a password
user_pass = input("please enter a password that is at least 8 characters long\n")

#This ensures that any password less than 8 characters will not be accepted
while len(user_pass) < 8:
    user_pass = input("your password is not long enough. Please try again\n")

#prints the length of the password
print(f"Your password is {len(user_pass)} characters long!")