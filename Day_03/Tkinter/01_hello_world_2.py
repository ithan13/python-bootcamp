import tkinter

root = tkinter.Tk()
root.title("Sample GUI Application 2")
root.geometry("1200x400")

message = """
Hello
World
"""

label = tkinter.Label(root, text=message)
label.pack()



root. mainloop()



