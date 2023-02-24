# Write a script that will check whether
# the entered number is even or odd and
# display the appropriate message.

numb = input("Please enter a number: ")
if numb.isdigit():
    print("Entered number is even") if int(numb) % 2 == 0 else "Entered number is odd"

else:
    print("It seems you have entered not a number")