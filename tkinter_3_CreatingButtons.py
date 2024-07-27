from tkinter import *



root=Tk()



def MyClick():
    hello= "Hello "+ e.get()
    mylabel1=Label(root,text=hello).grid(row=5,column=0)



mybutton1= Button(root,text="Click Me!",padx=50, command=MyClick, fg="blue", bg="white")
#command allows the execute of a function.
#padx change the x abscissa axis (padding in the x axis)
#pady change the y coordinate axis (padding in the y axis)
#by adding disabled to the button, now it is disabled



mybutton2=Button(root,text="You can't click me.",pady=50,state=DISABLED,bg="black",fg="white")
#fg is for colors, bg is for background color.
e=Entry(root,width=50,bg="black",fg="white",borderwidth=5)
e.grid(row=3,column=6)
e.get()
#get function gets whatever u typed in the entry widget
e.insert(0,"What's your name? ")
#put some default text in the entry box



mybutton1.grid(row=0,column=0)
mybutton2.grid(row=0,column=1)



root.mainloop()