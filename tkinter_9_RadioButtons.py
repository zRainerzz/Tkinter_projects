from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("github.com/zRainerzz")

""" Windows icon (replace with your .ico file) """
# root.iconbitmap("tkinter_icon.ico")  # Uncomment for Windows

""" Linux icon (replace with your .png file) """
icon_image = ImageTk.PhotoImage(Image.open("tkinter_icon.png"))
root.iconphoto(True, icon_image)


r=IntVar()#this allows tkinter to keep track to the changes overtime.
Radiobutton(root,text="option 1",variable=r,value=1).pack()#variable needed in radio but
Radiobutton(root,text="option 2",variable=r,value=2).pack()#variable needed in radio but


root.mainloop()