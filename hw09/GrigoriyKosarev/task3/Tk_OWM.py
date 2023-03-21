import tkinter as tk
from builtins import print
from tkinter import font
from OWM import get_weather


def set_weather(city):
    w = get_weather(city)
    weather = [f"detailed_status: {str(w.detailed_status)}",
               f"wind: {str(w.wind())}",
               f"humidity: {str(w.humidity)}",
               f"humidity: {str(w.humidity)}",
               f"temperature: {str(w.temperature('celsius'))}",
               f"rain: {str(w.rain)}",
               f"heat_index: {str(w.heat_index)}",
               f"clouds: {str(w.clouds)}"]
    nl = "\n"
    str_res = f'{nl}{nl.join(weather)}'
    label.config(text=str_res)

HEIGHT = 350
WIDTH = 450

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
                   command=lambda: set_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()





