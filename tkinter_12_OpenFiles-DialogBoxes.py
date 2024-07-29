import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

def open_image():
    filename = filedialog.askopenfilename(initialdir="/home/khedhri/Desktop/Tkinter_course",
                                       title="Select A file.",
                                       filetypes=(("png files", "*.png"), ("all files", "*.*")))
    if filename:
        img = Image.open(filename)
        img_resized = img.resize((400, 400))
        photo = ImageTk.PhotoImage(img_resized)
        my_img_label.config(image=photo)
        my_img_label.image = photo  # Keep a reference to prevent garbage collection

root = tk.Tk()
root.title("github.com/zRainerzz")

""" Windows icon (replace with your .ico file) """
# root.iconbitmap("tkinter_icon.ico")  # Uncomment for Windows

""" Linux icon (replace with your .png file) """
icon_image = ImageTk.PhotoImage(Image.open("tkinter_icon.png"))
root.iconphoto(True, icon_image)

my_img_label = tk.Label(root)
my_img_label.pack()

open_image_button = tk.Button(root, text="Open Image", command=open_image)
open_image_button.pack()

root.mainloop()