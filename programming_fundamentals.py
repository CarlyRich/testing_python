favouriteFood = "sushi"

print("what's my favourite food?")

userFavouriteFood = input("Enter your answer here: ")

if userFavouriteFood == favouriteFood:
    print("Yep, so amazing!")

else: 
    print("Yuck! That's not it!")

print("Thanks for playing!")


def say_hello():
    print("Hello, friends!")

say_hello()

def wash_car(amountPaid):
    if (amountPaid == 12):
        print("Rinse twice")
        print("Dry with large blow dryer")

    if (amountPaid == 6):
        print("Rinse once")
        print("Air dry")
    
    print ("You paid £", amountPaid)

wash_car(12)

def favourite_city(name):
    print("One of my favourite cities is", name)

favourite_city("Athens")
favourite_city("Rome")
favourite_city("Paris")
