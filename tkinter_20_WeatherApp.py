from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("github.com/zRainerzz")

""" Windows icon (replace with your .ico file) """
# root.iconbitmap("tkinter_icon.ico")  # Uncomment for Windows

""" Linux icon (replace with your .png file) """
icon_image = ImageTk.PhotoImage(Image.open("tkinter_icon.png"))
root.iconphoto(True, icon_image)

#designating how big the original window is
root.geometry("500x500")

#Frame
frame=LabelFrame(root,text="This is a Frame",padx=50,pady=100)#INTERNAL PADDING

root.mainloop()