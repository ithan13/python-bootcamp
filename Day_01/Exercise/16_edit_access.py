number = input("Enter Role: ")

# if number == "admin" or number == "editor":
#     print("Edit access enabled")
# else:
#     print("Edit not allowed")

match number:
    case "admin"|"editor":
        print("Edit access enabled")
    case _:
        print("Edit not allowed")

