import tkinter

root = tkinter.Tk()
root.title("Sample GUI Application")
root.geometry("1200x400")

label = tkinter.Label(root, text="Hello")
label.pack()

label = tkinter.Label(root, text="World")
label.pack()


# to directly input in the window but cannot edit
# tkinter.Label(root, text="Hello World").pack()

root. mainloop()



