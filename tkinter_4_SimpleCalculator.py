from tkinter import *
root=Tk()
root.title("Calculator")


e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
#e.insert(0, "")

def button_add():
    

button_1= Button(root,text="1",padx=40,pady=20,command=button_add)

myButton=Button(root,text="Enter Your Stock Quote",command=myClick)


root.mainloop()