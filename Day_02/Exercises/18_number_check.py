user_input = input("Enter number: ")

#clean the input for the code
clean_input = user_input.strip().replace(",","")

if clean_input.isnumeric():
    clean_input = int(clean_input)
    print(clean_input+1)
else:
    print("Enter a valid number!!")