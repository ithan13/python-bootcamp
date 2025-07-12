import tkinter

root = tkinter.Tk()

label = tkinter.Label(
    root,
    text="Hello",
    fg="Black",
    bg="MediumTurquoise",
    font=("Chiller", 38, "bold italic"),
    width=100,
    height=100
)

label.pack()


root.mainloop()
