# import the math module, which contains features for working with mathematics
import math

# the math module contains lots of pre-built functions
print("the square root of 16 is", math.sqrt(16))

# in addition to functions, some modules contain useful constants
print("Pi is", math.pi)

# try some of the math functions for yourself here:

# Rounds up to nearest integer
print(math.ceil(4.35345345))

# Rounds down to nearest integer
print(math.floor(4.35345345))

# calculates sum in tuple, array, list
print(math.fsum([2, 3, 4]))

# Checks whether a/b are close
print(math.isclose(2, 3))
print(math.isclose(2.1, 2.12, abs_tol = 0.5))

# power of
print(math.pow(2, 3))