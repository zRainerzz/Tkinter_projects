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
img_resized = img.resize((400, 400))
photo = ImageTk.PhotoImage(img_resized)

img1 = Image.open("image1.jpg")  # Replace with your image path
img_resized1 = img1.resize((400, 400))
photo1 = ImageTk.PhotoImage(img_resized1)

img2 = Image.open("image2.jpg")  # Replace with your image path
img_resized2 = img2.resize((400, 400))
photo2 = ImageTk.PhotoImage(img_resized2)

img3 = Image.open("image3.jpg")  # Replace with your image path
img_resized3 = img3.resize((400, 400))
photo3 = ImageTk.PhotoImage(img_resized3)

img4 = Image.open("image4.jpg")  # Replace with your image path
img_resized4 = img4.resize((400, 400))
photo4 = ImageTk.PhotoImage(img_resized4)


#listing images
image_list=[photo, photo1, photo2, photo3, photo4]



#creating a status bar:
status=Label(root,text="Image 1 of "+ str(len(image_list)),bd=1,relief=SUNKEN,anchor=W)#bd is border.









""" Display image on label """
my_label = Label(image=photo)
my_label.grid(row=0, column=0,columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])#we passed 2 which is the 3rd item in the list(since lists start from 0), we do -1 to go the image number 1
    button_forward=Button(root,text=">>",bg="yellow",fg="black",command=lambda: forward(image_number+1))#why? because it is back to normal, now you back normal
    button_back=Button(root,text="<<",bg="yellow",fg="black",command=lambda:back(image_number-1))
    
    if image_number==5:
        button_forward=Button(root,text=">>",bg="yellow",fg="black",state=DISABLED)

    my_label.grid(row=0, column=0,columnspan=3)
    button_back.grid(row=1,column=0,pady=20)
    button_forward.grid(row=1, column=2,pady=20)
    
    #UPDATE STATUS BAR
    status=Label(root,text="Image "+ str(image_number)+" of "+ str(len(image_list)),bd=1,relief=SUNKEN,anchor=W)#bd is border.
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)



def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_back=Button(root,text="<<",bg="yellow",fg="black",command=lambda:back(image_number-1))
    button_forward=Button(root,text=">>",bg="yellow",fg="black",command=lambda: forward(image_number+1))

    if image_number==1 :
        button_back=Button(root,text=">>",bg="yellow",fg="black",state=DISABLED)

    my_label.grid(row=0, column=0,columnspan=3)
    button_back.grid(row=1,column=0,pady=20)
    button_forward.grid(row=1, column=2,pady=20)
    
    #UPDATE STATUS BAR
    status=Label(root,text="Image "+ str(image_number)+" of "+ str(len(image_list)),bd=1,relief=SUNKEN,anchor=W)#bd is border.
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)




"""Back, Forward and Exit buttons """
button_quit = Button(root, text="EXIT", bg="black", fg="yellow", command=root.quit,)
button_back=Button(root,text="<<",bg="yellow",fg="black",command=back,state=DISABLED)
button_forward=Button(root,text=">>",bg="yellow",fg="black",command=lambda : forward(2))

"""DISPLAY BUTTONS"""

button_quit.grid(row=1, column=1,pady=20)
button_back.grid(row=1,column=0,pady=20)
button_forward.grid(row=1, column=2,pady=20)

"""DISPLAY STATUS BAR"""
status.grid(row=2,column=0,columnspan=3,sticky=W+E)
"""
we want to stretch from left to right,

that's how stiky works:
    #with N, refers to North
    #with S, refers to South
    #with W, refers to West
    #with E, refers to East
"""
root.mainloop()
