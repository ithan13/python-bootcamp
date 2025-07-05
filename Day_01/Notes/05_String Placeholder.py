# Message Template
message = "Hello {}! Nice to meet you!"
print(message)

# Use Template
formatted_message =  message.format("Juan")
print(formatted_message)

message = "Hello {}! Nice to meet you {}!"
name = input("Enter name: ")
nickname = input("Enter nickname: ")
formatted_message = message.format(name,nickname)
print(formatted_message)

