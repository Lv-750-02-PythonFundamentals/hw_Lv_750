"""game logic part"""

# while game:
def input_number():
    import random

    game = True
    new_game = True
    
    if new_game:
        tries = 10
        number = random.randint(1, 100)
        new_game = False
    guess = int(input(f"Try to guess the number in range 1-100, you have {tries} tries left\n"))
    tries -= 1
    if guess == number:
        message = "You WIN!"
    elif guess != number:
        message = "Try again! Number is bigger..." if number > guess else "Try again! Number is smaller..."
        if tries == 0:
            message = "You LOSE!"
    print(message)
            
    if message == "You WIN!" or message == "You LOSE!":
        choise = input("Wanna try again? (Y/N)\n")
        new_game = True if choise == "Y" else False
        game = False if choise == "N" else True
    return number