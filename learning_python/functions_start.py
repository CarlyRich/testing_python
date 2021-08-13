#
# Example file for working with functions
#

# define a basic function
def func1():
    print("I am a function!")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, "", arg2)

# function that returns a value
def func3(x):
    return x*x*x

print(func3(2))
# function with default value for an argument
def func4(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

print(func4(2))
print(func4(2, 4))

#function with variable number of arguments
def func5(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print(func5(1, 2, 3, 4))
