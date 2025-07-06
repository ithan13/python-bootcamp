attendee_names = set()
attendee_count = int(input("Attendee Count :"))

# _ is a variable in a range if no assigned variable
for _ in range(attendee_count):
    attendee_name = input("Attendee name: ")
    attendee_names.add(attendee_name)
print(attendee_names)
