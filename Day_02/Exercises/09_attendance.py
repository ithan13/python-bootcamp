attendee_names = []
attendee_count = int(input("Attendee Count :"))

# _ is a variable in a range if no assigned variable
for _ in range(attendee_count):
    attendee_name = input("Attendee name: ")
    attendee_names.append(attendee_name)
print(attendee_names)

#Check the name's index
check_name = input("Enter check name: ")
print(attendee_names.index(check_name))

#Remove the name from the list
index_name = attendee_names.remove(check_name)
print(attendee_names)

#Pop out last
removed_name = attendee_names.pop(attendee_count-2)
print(removed_name)
print(attendee_names)



