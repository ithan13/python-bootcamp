color_input = input("Please enter color: ")

# if color_input == "green":
#     print("Go")
# elif color_input == "yellow":
#     print("wait")
# elif color_input == "red":
#     print("Stop")
# else:
#     print("Error")

match color_input:
    case "green":
        print("go")
    case "red":
        print("stop")
    case "yellow":
        print("wait")
    case _:
        print("Malfunction")
