stop_program = False

while not stop_program:
    choice = input("Provide command:")
    if choice == "command 1":
        print("command 1 done")
    elif choice == "command 2":
        print("command 2 done")
    elif choice == "exit":
        stop_program = True