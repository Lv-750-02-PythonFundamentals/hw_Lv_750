"""Write a program that analyzes the entered number and, depending on the number, gives
the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). Take
into account cases of entering numbers from 8 and more, as well as cases of entering nonnumerical data.
"""

week = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
go = 1
while go:
    try:
        number = int(input("Please enter day of the week: "))
        if 0 < number < 8:
            print(week[number])
            go = 0
        else:
            raise ValueError("Week has 7 days starting from 1")
    except ValueError as e:
        print(e)