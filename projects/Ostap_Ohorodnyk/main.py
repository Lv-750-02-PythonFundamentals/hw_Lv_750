"""program to do list"""
from tkinter import *
from tkinter.font import Font


root = Tk()
root.title("My ToDO list!")
bg="light gray"
root.geometry("570x500")
root.configure(bg="light gray")

# Define font
my_font = Font(family="Purisa",
               size=20,
               weight="bold",)

# Creat frame
my_frame=Frame(root)
my_frame.pack(pady=10)

# Create list box
my_list = Listbox(my_frame,
                  font=my_font,
                  width=35,
                  height=5,
                  bg="light gray",
                  bd=0,
                  fg="#464646",
                  highlightthickness=0,
                  selectbackground="#a6a6a6",
                  activestyle="none")

my_list.pack(side=LEFT, fill=BOTH, )
# start list

stuff = ["write your tasks"]

for item in stuff:
    my_list.insert(END, item)

#ADD scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# entry text box
my_entry = Entry(root, font=("Purisa", 20), width=26)
my_entry.pack(pady=20)
# buttons

button_frame = Frame(root)
button_frame.pack(pady=20)
# button function

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0,END)

def cross_off_item():
    my_list.itemconfig(
        my_list.curselection(), fg="#FFFAFA"
    )
    my_list.selection_clear(0,END)

def uncross_off_item():
    my_list.itemconfig(
        my_list.curselection(), fg="#464646"
    )
    my_list.selection_clear(0, END)

def delete_crossed():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#FFFAFA":
            my_list.delete(my_list.index(count))
        else:
            count += 1

add_button = Button(button_frame, text="Add task", command=add_item)
cross_off_button = Button(button_frame, text="Cross task", command=cross_off_item)
uncross_off_button = Button(button_frame, text="Uncross tsk", command=uncross_off_item)
delete_crossed_button = Button(button_frame, text="Delete crossed", command=delete_crossed)

add_button.grid(row=0, column=0, padx=10)
cross_off_button.grid(row=0, column=1, padx=10)
uncross_off_button.grid(row=0, column=2, )
delete_crossed_button.grid(row=0, column=3,padx=10)


root.mainloop()