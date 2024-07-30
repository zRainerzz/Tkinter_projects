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


vertical=Scale(root,from_=0,to=200)
horizontal=Scale(root,from_=0,to=200,orient=HORIZONTAL)

vertical.pack()
horizontal.pack()

def slide1():
    mylab=Label(root,text=vertical.get()).pack()

def slide2():
    mylab2=Label(root,text=horizontal.get()).pack()

btn1=Button(root,text="Slide vertically",command=slide1)
btn2=Button(root,text="Slide horizentally",command=slide2)














root.mainloop()