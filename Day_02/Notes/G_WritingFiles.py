Names = ["Mia Anderson","Ethan Roberts","Liam Johnson","Sophia Martinez",
         "Olivia Davis","Noah Thompson"]

with open("test.txt","w") as file:
    # file.write(Names +"\n")
    # file.write("Ethan Roberts" + "\n")
    # file.write("Mia Anderson" + "\n")
    for name in Names:
        file.write(name + "\n")

with open("test.txt","a") as file:
    file.write("Alex Freze")

# Read to use the content of the file  as data
with open("test.txt","r") as file:
    file_contents = file.read().splitlines()
    print(file_contents)



