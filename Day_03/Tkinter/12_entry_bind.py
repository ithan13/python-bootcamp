
import tkinter

root = tkinter.Tk()
enter_msg = tkinter.Label(root, text="Enter your password")
enter_msg.pack()

entry = tkinter.Entry(root)
entry.pack()

user_input = tkinter.StringVar(root, value="Enter your password and press enter")
label = tkinter.Label(root, textvariable=user_input)
label.pack()

def show_input(event):
        if entry.get() == "pass":
            user_input.set("Password correct! Access granted")
        else:
            user_input.set("Incorrect password. Try again.")

root.bind("<Return>", show_input)
root.bind("<space>", show_input)
root.mainloop()
