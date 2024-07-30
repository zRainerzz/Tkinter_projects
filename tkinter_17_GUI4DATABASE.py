from tkinter import *
from PIL import Image, ImageTk
import sqlite3


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


#Databases


#Create a database or connect to one.
conn=sqlite3.connect('tkinter_17_GUI4DATABASE.db')

#Create cursor
c=conn.cursor()


#Create table
c.execute("""CREATE TABLE adresses (
          first_name text,
          last_name text,
          adress text,
          city text,
          state text,
          zipcode integer
          
)""")


#Create Text Boxes
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)

l_name=Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)

adress=Entry(root,width=30)
adress.grid(row=2,column=1,padx=20)

city=Entry(root,width=30)
city.grid(row=3,column=1,padx=20)

state=Entry(root,width=30)
state.grid(row=4,column=1,padx=20)

zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1,padx=20)

#Create Text Box Labels
f_name_Label=Label()


#Commit changes
conn.commit()

#Close connection
conn.close


root.mainloop()