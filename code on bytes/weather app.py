from geopy.geocoders import Nominatim
import os
import requests
from tkinter import *
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
import tkinter as tk


def getWeather():
    try:
        place = textfield.get()
        geolocator = Nominatim(user_agent="weather app")
        location = geolocator.geocode(place)
        
        if location:
            lat = location.latitude
            lon = location.longitude
            
            tzf = TimezoneFinder()
            result = tzf.timezone_at(lng=lon, lat=lat)

            if result:
                home = pytz.timezone(result)
                local_time = datetime.now(home)
                current_time = local_time.strftime('%I:%M %p') 
                clock.config(text=current_time)
                name.config(text="current time")

                api_key = os.environ.get("current_weather_api")

                api_link = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
                send_link = requests.get(api_link)
                
                data = send_link.json()
   
               
                condition = data['weather'][0]['main']
                description = data['weather'][0]['description']
                temp = int(data['main']['temp'] - 273.15)
                pressure = data['main']['pressure']
                humidity = data['main']['humidity']
                wind = data['wind']['speed']
                if condition == 'Clouds':
                    logo_img = PhotoImage(file=r"C:\Users\anish\OneDrive\Desktop\code on bytes\cloud.png")
                
                elif condition == 'Rain':
                    logo_img = PhotoImage(file=r"C:\Users\anish\OneDrive\Desktop\code on bytes\rain.png")
                
                else:
                    logo_img = PhotoImage(file=r"C:\Users\anish\OneDrive\Desktop\code on bytes\newlogo.png")
                logo.config(image=logo_img)
                logo.image = logo_img
             
                


                t.config(text=(temp, '°'))
                c.config(text=f"{condition} | feels like {temp}")

                w.config(text=(wind,"knots"))
                h.config(text=humidity)
                p.config(text=description)
                d.config(text=(pressure,"PA"))
            else:
                messagebox.showerror('Timezone Not Found', 'Unable to determine the timezone for the location.')
        else:
            messagebox.showerror('Location Not Found', 'Unable to determine the location.')
    except Exception as e:
        messagebox.showerror('Error', 'An error occurred while fetching weather data.')


root=tk.Tk()
root.title('weather app')
root.geometry('900x500+300+200')
root.resizable(False,False)

search_img=PhotoImage(file=r"C:\Users\anish\OneDrive\Desktop\code on bytes\Copy of search.png")
myimage=Label(image=search_img)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,'bold'),bg='#404040',fg="white",border=0)
textfield.place(x=50,y=40)
textfield.focus()

search_icon=PhotoImage(file=r"C:\Users\anish\OneDrive\Desktop\code on bytes\Copy of search_icon.png")
search_btn=Button(image=search_icon,cursor='hand2',borderwidth=0,bg="#404040",command=getWeather)
search_btn.place(x=400,y=34)


logo_img=PhotoImage(file=r"C:\Users\anish\OneDrive\Desktop\code on bytes\newlogo.png")
logo=Label(image=logo_img)
logo.place(x=150,y=100)

bottom_img=PhotoImage(file=r"C:\Users\anish\OneDrive\Desktop\code on bytes\box.png")
bottom_lable=Label(image=bottom_img)
bottom_lable.pack(padx=5,pady=5,side=BOTTOM)

Label1=Label(root,text='wind',font=('Helvetica',15,'bold'),fg="white",bg='#1ab5ef')
Label1.place(x=120,y=400)

Label2=Label(root,text='humidity',font=('Helvetica',15,'bold'),fg="white",bg='#1ab5ef')
Label2.place(x=250,y=400)

Label3=Label(root,text='descrption',font=('Helvetica',15,'bold'),fg="white",bg='#1ab5ef')
Label3.place(x=430,y=400)

Label1=Label(root,text='pressure',font=('Helvetica',15,'bold'),fg="white",bg='#1ab5ef')
Label1.place(x=650,y=400)

t=Label(font=("arial",70,'bold'),fg="#ee666d")
t.place(x=400,y=150)

c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",15,'bold'),bg='#1ab5ef')
w.place(x=117,y=430)

h=Label(text="...",font=("arial",15,'bold'),bg='#1ab5ef')
h.place(x=254,y=430)

p=Label(text="...",font=("arial",15,'bold'),bg='#1ab5ef',wraplength=150)
p.place(x=438,y=427)

d=Label(text="...",font=("arial",15,'bold'),bg='#1ab5ef')
d.place(x=670,y=430)



name=Label(root,font=("arial",15,'bold'))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20,'bold'))
clock.place(x=30,y=130)




root.mainloop()
