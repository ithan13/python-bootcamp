attendee_names = set()
attendee_count = int(input("Attendee Count :"))

# _ is a variable in a range if no assigned variable
for _ in range(attendee_count):
    attendee_name = input("Attendee name: ")
    attendee_names.add(attendee_name)

print(attendee_names)

# Remove name from attendees
remove_name = input("Enter name to remove: ")
attendee_names.discard(remove_name)
print(attendee_names)

# Pick a random raffle winner
returnvalue = attendee_names.pop()
print("Raffle winner is:",returnvalue)