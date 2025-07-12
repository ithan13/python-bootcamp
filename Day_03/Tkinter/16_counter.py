import tkinter

root = tkinter.Tk()

count = tkinter.IntVar(root, value=0)
label = tkinter.Label(root, textvariable=count)
label.pack()

def increment():
    new_value = count.get() + 1
    count.set(new_value)

def decrease():
    new_value = count.get() - 1
    count.set(new_value)

button1 = tkinter.Button(root, text="+", command=increment)
button1.pack()
button2 = tkinter.Button(root, text="-", command=decrease)
button2.pack()

root.mainloop()