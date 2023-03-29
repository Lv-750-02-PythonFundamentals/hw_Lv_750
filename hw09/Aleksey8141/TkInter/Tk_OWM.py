import tkinter as tk
from tkinter import font
from pyowm import OWM

HEIGHT = 600
WIDTH = 800

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather(place):
    observation = mgr.weather_at_place(place)
    w = observation.weather
    detailed_status = w.detailed_status
    wind = w.wind()
    humidity = w.humidity
    temperature = w.temperature('celsius')
    rain = w.rain
    heat_index = w.heat_index
    clouds = w.clouds
    return detailed_status, wind, humidity, temperature, rain, heat_index, clouds


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: show_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

def show_weather():
    place = entry_field.get()
    detailed_status, wind, humidity, temperature, rain, heat_index, clouds = get_weather(place)
    text = f"Detailed status: {detailed_status}\nWind: {wind}\nHumidity: {humidity}\nTemperature: {temperature}\nRain: {rain}\nHeat index: {heat_index}\nClouds: {clouds}"
    label.config(text=text)

root.mainloop()

