from pyowm import OWM
import tkinter as tk
from tkinter import messagebox as mbox
from tkinter import font

# ---------- FREE API KEY examples ---------------------

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
HEIGHT = 350
WIDTH = 450

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def message(wrong_city):
    mbox.showwarning(wrong_city, "Retrieving that information.")

def get_weather():
    try:
        input_city = entry_field.get()
        observation = mgr.weather_at_place(input_city)
        w = observation.weather
        label['text'] = f"City: {input_city}\nConditions: {w.detailed_status }" \
                    f"\nTemperature is {round(w.temperature('celsius')['temp'], 2)} c "\
                    f"\nTemp max is {round(w.temperature('celsius')['temp_max'], 2)} c" \
                    f"\nTemp min is {round(w.temperature('celsius')['temp_min'], 2)} c" \
                    f"\nWind speed is {w.wind()['speed']} km/hours\nHumidity of the air is {w.humidity}"

    except:
        message('Oops!!! There was a problem')

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
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()

