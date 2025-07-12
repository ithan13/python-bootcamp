import tkinter
import json
from tkinter import simpledialog, BooleanVar, IntVar

root = tkinter.Tk()
root.title("Data Form")
root.geometry("300x200")

entry = tkinter.Entry(root)
entry.pack

label = tkinter.Label(root, text="Name")
label.pack()
entry1=tkinter.Entry(root)
entry1.pack()

label = tkinter.Label(root, text="Age")
label.pack()
entry2=tkinter.Entry(root)
entry2.pack()

label = tkinter.Label(root, text="Preferred Theme")
label.pack()
radio_var = tkinter.StringVar(value="Light")
radio1 = tkinter.Radiobutton(root, text="Light", variable=radio_var, value="Light")
radio1.pack()
radio2 = tkinter.Radiobutton(root, text="Dark", variable=radio_var, value="Dark")
radio2.pack()

check_value = tkinter.BooleanVar()
checkbox = tkinter.Checkbutton(root, text="Subscribe to newsletter", variable=check_value).pack()

slider_value = tkinter.IntVar(value=0)
slider = tkinter.Scale(root, from_=0, to=100, orient="horizontal", variable=slider_value).pack()

def submit():
    user = {
        "Name":entry1.get(),
        "Age":entry2.get(),
        "Themes":radio_var.get(),
        "Subscribe":check_value.get(),
        "Rating":slider_value.get()
    }
    with open('user.json','w') as file:
        json.dump(user,file)

# xxxx.get() wherein xxxx = variable name

button = tkinter.Button(root, text="Submit",command=submit)
button.pack()

root.mainloop()
