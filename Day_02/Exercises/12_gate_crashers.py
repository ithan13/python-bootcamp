invited = {"Ana", "Ben", "Carlo", "Dani"}
attended = {"Ben", "Carlo", "Ely"}

# Who are all involved members?
print("Involved members: ", invited|attended)

# Who was absent?
print("Absent: ", invited-attended)

# Who gate crashed?
print("Gate Crashed: ", attended-invited)

# Who are invited and attended?
print("Invited and Attended: ", attended&invited)