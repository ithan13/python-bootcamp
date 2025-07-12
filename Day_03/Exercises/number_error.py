from unicodedata import numeric

user_input = input("Enter a number [1 to 1000]: ")

#Not a Number check
class NotANumber(ValueError):
    pass

if not user_input.isnumeric() and not user_input[1:].isnumeric():
    raise NotANumber(ValueError)

#Not a positive Number error
class NotPositive(ValueError):
    pass

number = int(user_input)

if number < 0:
    raise NotPositive()

#Not in the range
class NotWithinRange(ValueError):
    pass

if not (1 <= number <=100):
    raise NotWithinRange()
