count = 0
stop_program = False

# while not stop_program:
#     choice = input("Provide command:")
#     if choice == "add":
#         count += 1
#         print(count)
#     elif choice == "sub":
#         count -= 1
#         print(count)
#     elif choice == "double":
#         count *= 2
#         print(count)
#     elif choice == "exit":
#         stop_program = True

count = 1
stop_program = False

while not stop_program:
    choice = input("Provide command:")
match choice:
    case "Add":
        count += 1
        print(count)
    case "Sub":
        count -=1
        print(count)
    case "Double":
        count *=2
        print(count)
    case "Exit":
        stop_program = True

# match color_input:
#             case "green":
#                 print("go")
#             case "red":
#                 print("stop")
#             case "yellow":
#                 print("wait")
#             case _:
                print("Malfunction")