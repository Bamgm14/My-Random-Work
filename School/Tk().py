from tkinter import *

root = Tk()
root.title("Addition Calculator")

answer_label =Label(root, text ="---")
answer_label.grid(row =0, column =0)

label1 =Label(root, text ="first")
label1.grid(row =1, column =0)

num1_txtbx =Entry(root)
num1_txtbx.grid(row =1, column =1)

label2 =Label(root, text ="second")
label2.grid(row =2, column =0)

num2_txtbx =Entry(root)
num2_txtbx.grid(row =2, column =1)

def addF():
    if (num1_txtbx.get() and num2_txtbx.get() != ""):
        try:
            num1 =float(num1_txtbx.get())
            num2 =float(num2_txtbx.get())

            answer= num1 + num2
            answer_label.configure(text =answer)
            status_label.configure(text ="successfully computed")
        except:
            status_label.configure(text ="invalid input, check your input types")
    else:
        status_label.configure(text ="fill in all the required fields")

calculate_button =Button(root, text="calculate", command= addF)
calculate_button.grid(row =3, column =0, columnspan =2)

status_label =Label(root, height =5, width =25, bg ="black", fg ="#00FF00", text ="---", wraplength =150)
status_label.grid(row =4, column =0, columnspan =2)

root.mainloop()
"""from tkinter import *

root = Tk()

def key(event):
    print ("pressed", repr(event.char))

def callback(event):
    frame.focus_set()
    print ("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()
"""
