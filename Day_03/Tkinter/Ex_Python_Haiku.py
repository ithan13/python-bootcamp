import tkinter

root = tkinter.Tk()
root.title("Sample GUI Application 3")

message =""" 
Loops within loops spin, 
A silent function returns,
The logic is clear
"""

label = tkinter.Message(root, text=message)
label.pack()

root.mainloop()

