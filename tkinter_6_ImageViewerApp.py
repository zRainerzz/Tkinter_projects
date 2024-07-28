from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("github.com/zRainerzz")

""" Windows icon (replace with your .ico file) """
# root.iconbitmap("tkinter_icon.ico")  # Uncomment for Windows

""" Linux icon (replace with your .png file) """
icon_image = ImageTk.PhotoImage(Image.open("tkinter_icon.png"))
root.iconphoto(True, icon_image)


""" Load and resize image """
img = Image.open("python.jpg")  # Replace with your image path
img_resized = img.resize((200, 200))
photo = ImageTk.PhotoImage(img_resized)


""" Display image on label """
my_label = Label(image=photo)
my_label.grid(row=1, column=0)


""" Exit button """
button_quit = Button(root, text="EXIT", bg="black", fg="yellow", command=root.quit,width=100)
button_quit.grid(row=0, column=0)


root.mainloop()
