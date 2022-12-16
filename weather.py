from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import requests
import os
os.system("cls")
root = Tk()
root.title("See the weather in your city")
root.geometry("500x300")

bg = ImageTk.PhotoImage(file="weather.jpg")


def GetWeather():
    holdCity = city_text.get()
    link = "https://api.openweathermap.org/data/2.5/weather?q=" + \
        holdCity + "&units=metric&appid=22515dbe8047cf659da74a1cae281c2e"
    response = requests.get(link)

    data = response.json()

    placeLabel["text"] = "{} , {}".format(data['name'], data['sys']['country'])

    placeLabel.place(x=200, y=130)

    tempLabel["text"] = "Temperature: {} °C".format(data['main']['temp'])

    tempLabel.place(x=200,y=150)

    mintempLabel["text"] = "The low for today: {} °C".format(data['main']['temp_min'])
    mintempLabel.place(x=200,y=170)

    maxtempLabel["text"] = "The high for today: {} °C".format(data['main']['temp_max'])
    maxtempLabel.place(x=200,y=190)

canvas = Canvas(root, width=700, height=3500)
canvas.pack(fill=BOTH, expand=True)
canvas.create_image(0, 0, image=bg, anchor="nw")
title = Label(root, text="Weather App", font=("bold", 15)).place(x=190, y=50)

cityLabel = Label(root, text="Enter City Name: ",
                  font=("bold", 10)).place(x=150, y=80)
city_text = StringVar()
city_entry = Entry(root, textvariable=city_text)
city_entry.place(x=255, y=79)


goButton = Button(root, text="Go", width=12, command=GetWeather)
goButton.place(x=210, y=100)

placeLabel = Label(root, text="", font=("bold", 10))

tempLabel = Label(root, text="", font=("bold", 10))
mintempLabel = Label(root, text="", font=("bold", 10))
maxtempLabel = Label(root, text="", font=("bold", 10))


root.mainloop()