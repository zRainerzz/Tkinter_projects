from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("github.com/zRainerzz")

""" Windows icon (replace with your .ico file) """
# root.iconbitmap("tkinter_icon.ico")  # Uncomment for Windows

""" Linux icon (replace with your .png file) """
icon_image = ImageTk.PhotoImage(Image.open("tkinter_icon.png"))
root.iconphoto(True, icon_image)


#we do r=StrVar() incase we want to pass a string to radios.
r=IntVar()#this allows tkinter to keep track to the changes overtime.
#and in order to call r, we r.get()
r.set("2")

def clicked(value):
    mylab=Label(root,text=value)



Radiobutton(root,text="option 1",variable=r,value=1,command=lambda: clicked(r.get())).pack()#variable needed in radio but
Radiobutton(root,text="option 2",variable=r,value=2,command=lambda: clicked(r.get())).pack()#variable needed in radio but


mylab=Label(root,text=r.get())
mylab.pack()

b=Button(root,text="click me",command=lambda:clicked(r.get()))
b.pack()

root.mainloop()