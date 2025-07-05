# def line_generator():
#     print("Line 1")
#     print("Line 2")
#     print("Line 3")
#
# line_generator()

# def line_generator(n):
#     for i in range(1,n+1):
#         print(f"line {i}")
#
# line_generator(5)

# def line_generator(message,n):
#     for i in range(1,n+1):
#         print(f"{message} {i}")
#
# line_generator("hello world",3)

def line_generator(message="Hello World",n=3):
    for i in range(1,n+1):
        print(f"{message} {i}")

line_generator()