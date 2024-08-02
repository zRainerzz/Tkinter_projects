from tkinter import *
from PIL import Image, ImageTk
import requests
import json

root = Tk()
root.title("github.com/zRainerzz")

""" Windows icon (replace with your .ico file) """
# root.iconbitmap("tkinter_icon.ico")  # Uncomment for Windows

""" Linux icon (replace with your .png file) """
icon_image = ImageTk.PhotoImage(Image.open("tkinter_icon.png"))
root.iconphoto(True, icon_image)

#designating how big the original window is
root.geometry("600x100")
#Weather app, api from AirNow.gov

def zipLookup():
    #zpi.get()
    #zipLabel=Label(root,text=zpi.get())
    #zipLabel.grip(row=1,column=0,columnspan=2)

#Creating a request, it has my API Key , you can create a new account or just use my account, since AirNow.gov works only in USA i don't need that api.
    try:
        api_req=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zpi.get() + "&distance=5&API_KEY=9BE25E99-5FC4-4F57-B4AD-72DC0518FE67")
        api=json.loads(api_req.content)
        city= api[0]["ReportingArea"]
        quality=api[0]['AQI']
        category=api[0]["Category"]["Name"]

        if category=='Good':
            weather_color='#0C0'
        elif category=='Moderate':
            weather_color='#FFFF00'
        elif category=='Unhealthy for Sensitive Groups':
            weather_color='#ff9900'
        elif category=='Unhealthy':
            weather_color='#FF0000'
        elif category=='Very Unhealthy':
            weather_color='#990066'
        elif category=='Hazardous':
            weather_color='#600000'

        #Changing color of bg
        root.configure(background=weather_color)

        mylab=Label(root,pady=5,text=city + "Air Quality: "+ str(quality)+ " "+ category,font=("Helvetica",20),background=weather_color)
        mylab.grid(row=1,column=0,columnspan=2)        

    except Exception as e:
        api='ERROR...'



zpi=Entry(root)
zipButton=Button(root,text='Lookup Zipcode',command=zipLookup)


zipButton.grid(row=0,column=1)
zpi.grid(row=0,column=0)

root.mainloop()