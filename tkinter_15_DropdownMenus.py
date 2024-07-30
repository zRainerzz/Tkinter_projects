from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("github.com/zRainerzz")


frame=LabelFrame(root,text="eyes on the button not me, stalker!",padx=50,pady=100)#INTERNAL PADDING


""" Windows icon (replace with your .ico file) """
# root.iconbitmap("tkinter_icon.ico")  # Uncomment for Windows

""" Linux icon (replace with your .png file) """
icon_image = ImageTk.PhotoImage(Image.open("tkinter_icon.png"))
root.iconphoto(True, icon_image)

#designating how big the original window is
root.geometry("500x500")


#Drop Down Boxes
def show():
    mylab=Label(root,text=clicked.get()).pack()


options=["Monday",
         "Tuesday",
         "Wednesday",
         "Thursday",
         "Friday",
         "Saturday",
         "Sunday"]

#clicked need to be defined
clicked=StringVar()
clicked.set("Monday")


drop=OptionMenu(root, clicked,"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
drop.pack()

but=Button(root,text="Show Selection",command=show).pack()




root.mainloop()