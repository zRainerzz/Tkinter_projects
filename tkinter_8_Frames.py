from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("github.com/zRainerzz")

""" Windows icon (replace with your .ico file) """
# root.iconbitmap("tkinter_icon.ico")  # Uncomment for Windows

""" Linux icon (replace with your .png file) """
icon_image = ImageTk.PhotoImage(Image.open("tkinter_icon.png"))
root.iconphoto(True, icon_image)


frame=LabelFrame(root,text="This is a Frame",padx=50,pady=100)#INTERNAL PADDING
b1=Button(frame,text="Don't click me",command=quit,bd=5)
b2=Button(frame,text="Can't click me", state=DISABLED,bd=5)

frame.pack(padx=20,pady=20)#EXTERNAL PADDING
b1.grid(row=0,column=0)
b2.grid(row=1,column=0)

root.mainloop()