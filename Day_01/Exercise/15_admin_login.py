correct_username = "admin"
correct_password = "admin"

username_input = input("Please provide a username: ")
password_input = input("Please provide a password: ")

if username_input == correct_username and password_input == correct_password:
    print("Access Granted")
else:
    print("Access Denied")