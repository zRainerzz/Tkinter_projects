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
root.geometry("400x400")

#Weather app, api from AirNow.gov

#Frame
frame=LabelFrame(root,text="This is a Frame",padx=5,pady=5)#INTERNAL PADDING

#Creating a request, it has my API Key , i'll delete it once i finish recording, go to airnowapi and make your own account.
try:
    api_req=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=7")
    api=json.loads(api_req.content)
    city=api[0]["ReportinArea"]
    quality=api[0]['AQI']
    category=api[0]["Category"]["Name"]
except Exception as e:
    api='ERROR...'

mylab=Label(frame,text=city + "Air Quality: "+ str(quality)+ " "+ category)


mylab.pack()
frame.pack(padx=20,pady=20)#EXTERNAL PADDING

root.mainloop()