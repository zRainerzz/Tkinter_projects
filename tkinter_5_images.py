from tkinter import *
from PIL import ImageTk, Image
#i'll be adding a small revision about PILLOW (PIL) , in the upcoming repository.


root=Tk()
root.title("github.com/zRainerzz")

"""as a windows user, you just need this line to upload the icon which is in .ico format (i added an ico image to the repository for your use.)

root.iconbitmap("tkinter_icon.ico")
"""

"""For LINUX users:"""
# Load the image
icon_image = PhotoImage(file="tkinter_icon.png")
# Set the icon
root.iconphoto(True, icon_image)


"""images are 3 steps process:"""

# Define/Load the image using Pillow
img = ImageTk.PhotoImage(Image.open("python.jpg"))      # Replace with your image path


# Put the image on something
my_label=Label(image=img)

#put it in the screen
my_label.grid(row=1,column=2)

#let's resize the img
img_resized=img.resize((200,200))



button_quit=Button(root,text="EXIT",bg="black",fg="yellow",command=root.quit)
button_quit.grid(row=1,column=0)





root.mainloop()