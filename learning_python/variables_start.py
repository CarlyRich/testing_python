# 
# Example file for variables
#

# Declare a variable and initialize it
f = 0
print (f)


# re-declaring the variable works

# f = "abc" <---
# print (f) <---

# ERROR: variables of different types cannot be combined
def someFunc():
    f = "def"
    print (f)

someFunc()
print(f)

# Global vs. local variables in functions


