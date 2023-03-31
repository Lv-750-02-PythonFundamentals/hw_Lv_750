import tkinter as tk
from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

HEIGHT = 450
WIDTH = 550

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)


def get_weather():
    city_name = entry_field.get()
    observation = mgr.weather_at_place(city_name)
    w = observation.weather
    empty = {}

    weather = f"City: {city_name}\n General: {w.detailed_status}\n" \
              f"Wind(m per second): {w.wind()['speed']} \n Humidity: {w.humidity}\n Temperature(°C): {w.temperature('celsius')['temp']}\n" \
              f"Rain(mm per hour): {w.rain['1h'] if w.rain!=empty else'No Rain'}\n"\
              f"Heat index: {w.heat_index if w.heat_index is not None else '-'}\n Clouds: {w.clouds}"

    label["text"] = weather


button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
label = tk.Label(lower_frame, font=('Courier', 12))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
