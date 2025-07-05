# Expected password
correct_password = "pass"

# Enter password
password_input = input("Enter password: ")

# #Notify user if password is invalid
# correct_password_given = correct_password == password_input
# print("Access: ", correct_password_given)

if password_input == correct_password:
    print("Access Granted")
else:
    print("Access Denied")