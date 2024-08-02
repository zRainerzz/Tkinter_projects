from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("github.com/zRainerzz")

""" Windows icon (replace with your .ico file) """
# root.iconbitmap("tkinter_icon.ico")  # Uncomment for Windows

""" Linux icon (replace with your .png file) """
icon_image = ImageTk.PhotoImage(Image.open("tkinter_icon.png"))
root.iconphoto(True, icon_image)

#designating how big the original window is
root.geometry("400x200")

def graph1():
    house_prices=np.random.normal(200000,25000,5000)
    plt.hist(house_prices, 250)
    plt.show()

def graph2():
    house_prices1=np.random.normal(200000,25000,5000)
    plt.pie(house_prices1)
    plt.show()

my_but=Button(root,text='Graphic',command=graph1)
my_but2=Button(root,text='PIE GRAPHIC',command=graph2)

my_but.pack()
my_but2.pack()

root.mainloop()