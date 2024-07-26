from tkinter import *
"""
mostly called root, the root is the main widget (the graphical big box), so we generally start with it.
"""

root= Tk()

#creating a label widget.
my_label1=Label(root,text="Hello World.")
my_label2=Label(root,text="My name is Rain.")
my_label3=Label(root,text="Python obsession is real!.")

#shoving it onto the screen. 
my_label1.grid(row=0,column=0)
my_label2.grid(row=1,column=1)
my_label3.grid(row=2,column=1)

#that way it is constantly looping, clarify the program keeps working (constant loop until you kill the whole proccess by ticking the red button.)
root.mainloop()