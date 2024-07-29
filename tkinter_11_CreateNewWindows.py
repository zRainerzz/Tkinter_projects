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



""" Load and resize image """
img = Image.open("image2.jpg")  # Replace with your image path
img_resized = img.resize((400, 400))
photo = ImageTk.PhotoImage(img_resized)




def popup():
    top=Toplevel()
    top.title("BINGO! the new window")
    icon_image = ImageTk.PhotoImage(Image.open("tkinter_icon.png"))
    top.iconphoto(True, icon_image)
    """ Display image on label """
    my_label = Label(top,image=photo)
    my_label.pack()


""" Load and resize image """
img = Image.open("image2.jpg")  # Replace with your image path
img_resized = img.resize((400, 400))
photo = ImageTk.PhotoImage(img_resized)







frame.pack(padx=20,pady=20)#EXTERNAL PADDING
Button(frame,text="Validation",command=popup,bd=3,fg="white",bg="green",width=10).pack()
Button(frame,text="EXIT",command=quit,fg="black",bg="red",bd=3,width=10).pack()


root.mainloop()