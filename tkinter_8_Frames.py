from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("github.com/zRainerzz")

""" Windows icon (replace with your .ico file) """
# root.iconbitmap("tkinter_icon.ico")  # Uncomment for Windows

""" Linux icon (replace with your .png file) """
icon_image = ImageTk.PhotoImage(Image.open("tkinter_icon.png"))
root.iconphoto(True, icon_image)


frame=LabelFrame(root,text="This is a Frame",padx=5,pady=10)
frame.pack(padx=10,pady=10)

root.mainloop()