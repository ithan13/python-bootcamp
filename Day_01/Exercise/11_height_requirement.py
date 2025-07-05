minimum_height = 138

# Ask the user for the following inputs
user_height = int(input("Enter Height in cm: "))

can_enter_ride = (user_height>=minimum_height)
print("Can enter ride:", can_enter_ride)