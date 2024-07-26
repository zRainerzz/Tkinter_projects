from tkinter import *
"""
mostly called root, the root is the main widget (the graphical big box), so we generally start with it.
"""

root= Tk()

#creating a label widget.
my_label=Label(root,"Hello World.")

#shoving it onto the screen. 
my_label.pack()
