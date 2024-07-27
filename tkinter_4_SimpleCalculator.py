from tkinter import *
root=Tk()
root.title("Calculator")


e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
e.insert(0, "")

def myClick():
    hello="Hello" + e.get()
    label1=Label(root,text="Hello")
    label1.pack()


myButton=Button(root,text="Enter Your Stock Quote",command=myClick)


root.mainloop()