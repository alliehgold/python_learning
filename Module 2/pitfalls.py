
#indentation errors are one of the most common

x = 0

# if x > 5:
#     print("x is greater than 5")
#     else:  # Incorrect indentation
#     print("x is less than or equal to 5")


#Another common one is attempting to access variables out of scope


#if the 'flag' variable is false, this will give an error because x is only initialized if flag = True
flag = True
if flag:
    x = 10
    print(x) # No problem here

print(x) # No error if flag = True 

#attempting to change an immutable value, such as a string, will also cause an error.

value = "Hello"
# value[0] = 'h' --This will throw an error as you are trying to chagne a string, which is immutable
print(value)

#if you need to change a value in a string, you must create a new string

new_value = "h" + value[1:]
print(new_value)
