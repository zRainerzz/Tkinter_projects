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

#since we have the data base we don't want to run it again. we did a .db already
'''
#Create table
c.execute("""CREATE TABLE adresses (
          first_name text,
          last_name text,
          adress text,
          city text,
          state text,
          zipcode integer
          
)""")

'''

#Create function to delete record.
def deleter():
        #Create a database or connect to one.
    conn=sqlite3.connect('tkinter_17_GUI4DATABASE.db')

    #Create cursor
    c=conn.cursor()
    

#Create Submit Function For Database
def submit():
    #Create a database or connect to one.
    conn=sqlite3.connect('tkinter_17_GUI4DATABASE.db')

    #Create cursor
    c=conn.cursor()
    
    

    #Insert Into Table
    c.execute("INSERT INTO adresses VALUES (:f_name, :l_name, :adress, :city, :state, :zipcode)",
              
              {
                  'f_name':f_name.get(),
                  'l_name':l_name.get(),
                  'adress':adress.get(),
                  'city':city.get(),
                  'state':state.get(),
                  'zipcode':zipcode.get()
              })
    
   


    #Commit changes
    conn.commit()

    #Close connection
    conn.close
    #Clear The Text Boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    adress.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

#Create Querry func
def querry():
    #Create a database or connect to one.
    conn=sqlite3.connect('tkinter_17_GUI4DATABASE.db')

    #Create cursor
    c=conn.cursor()

    #Querry the Database
    #primary key iod
    #sqlite3 created and id for you (iod)
    c.execute("SELECT *, oid FROM adresses")
    records=c.fetchall()
    #print(records)

    #Loop through results
    print_records=''
    for record in records:
        print_records += str(record[0])+" " +str(record[1]) +" "+str(record[2]) +" "+str(record[3]) +" "+str(record[4]) +" "+str(record[5]) + "\t"+str(record[6]) + "\n"

    querry_label=Label(root, text=print_records)
    querry_label.grid(row=8,column=0,columnspan=2)

    #Commit changes
    conn.commit()

    #Close connection
    conn.close



#Create Text Boxes

f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))

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

f_name_Label=Label(root,text="First Name :")
f_name_Label.grid(row=0,column=0,pady=(10,0))

l_name_Label=Label(root,text="Last Name :")
l_name_Label.grid(row=1,column=0)

adress_Label=Label(root,text="Adress :")
adress_Label.grid(row=2,column=0)

city_Label=Label(root,text="City :")
city_Label.grid(row=3,column=0)

state_Label=Label(root,text="State :")
state_Label.grid(row=4,column=0)

zipcode_Label=Label(root,text="Zipcode :")
zipcode_Label.grid(row=5,column=0)

#Create Submit Button

submit_button=Button(root,text="Submit to the Database.",command=submit)
submit_button.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

 #Create a Query Button
query_button=Button(root,text="Show Records",command=querry)
query_button.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=132)

#Commit changes
conn.commit()

#Close connection
conn.close


root.mainloop()