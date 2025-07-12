import tkinter
from tkinter import messagebox

root = tkinter.Tk()
enter_msg = tkinter.Label(root, text="Enter your password")
enter_msg.pack()

entry = tkinter.Entry(root)
entry.pack()

user_input = tkinter.StringVar(root, value="Enter your password and press enter")
label = tkinter.Label(root, textvariable=user_input)
label.pack()

def show_input():
        if entry.get() == "pass":
            user_input.set("Password correct! Access granted")
        else:
            user_input.set("")
            messagebox.showerror(
                "Error",
                "Incorrect password!"
            )

button = tkinter.Button(root, text="Submit", command=show_input)
button.pack()

root.mainloop()
