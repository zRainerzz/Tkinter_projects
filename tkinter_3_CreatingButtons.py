from tkinter import *

root=Tk()

def MyClick():
    mylabel1=Label(root,text="Look I Clicked A Button!").grid(row=5,column=0)

mybutton1= Button(root,text="Click Me!",padx=50, command=MyClick, fg="blue", bg="white")
#command allows the execute of a function.
#padx change the width (x abscissa axis)
#pady change the heigh (y coordinate axis)
#by adding disabled to the button, now it is disabled
mybutton2=Button(root,text="You can't click me.",pady=50,state=DISABLED,bg="black",fg="white")
#fg is for colors, bg is for background color.





mybutton1.grid(row=0,column=0)
mybutton2.grid(row=0,column=1)


root.mainloop()