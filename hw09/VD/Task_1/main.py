"""Write a game script that randomly generates a number from a range of
1 to 100 and asks the user to guess that number in 10 tries.
The program reads the numbers entered by the user and prompts the user
whether the guessed number is greater or less than the number entered by the
user. The game must continue until the user has used 10 attempts and guessed
the number. If the user guessed the number, the program prints a
congratulatory message, and if 10 attempts have been exhausted and the user
did not have time to guess the number, then the corresponding message is
displayed.
(to perform the task, you need to import the random module,
and from it the randint() function)
"""

### At the moment program only displays results and messages to User, for inputs you need to use terminal

import pygame
import random

FPS = 60
SCR_WIDTH = 800
SCR_HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
screen.fill((255, 255, 255))

pygame.display.set_caption("Guess the number")
clock = pygame.time.Clock()

scr_message = pygame.font.SysFont('Comic Sans MS', 20, True, False)
scr_guess = pygame.font.SysFont("Arial", 40, True, False)
game = True
number = 10
new_game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    # game logic
    if new_game:
        tries = 10
        number = random.randint(1, 100)
        new_game = False
    
    text_1 = scr_message.render(f"Try to guess the number in range 1-100, you have {tries} tries left", True, (0, 128, 0))
    screen.blit(text_1, [100, 100])
    pygame.display.update()
    
    guess = int(input(f"Try to guess the number in range 1-100, you have {tries} tries left\n"))
    
    screen.fill((255, 255, 255))
    text_guess = scr_guess.render(f"{guess}", True, (255, 0, 0))
    screen.blit(text_guess, [390, 200])
    pygame.display.update()
    
    tries -= 1

    if guess == number:
        message = "You WIN!"
    elif guess != number:
        message = "Try again! Number is bigger..." if number > guess else "Try again! Number is smaller..."
        if tries == 0:
            message = "You LOSE!"
    print(message)

    #visual part
   
    text_2 = scr_message.render(f"{message}", True, (0, 128, 0))
    screen.blit(text_2, [250, 350])
    pygame.display.update()

    if message == "You WIN!" or message == "You LOSE!":
        
        text_choise = scr_guess.render(f"Wanna try again? (Y/N)", True, (0, 128, 0))
        screen.blit(text_choise, [250, 100])
        pygame.display.update()

        choise = input("Wanna try again? (Y/N)\n")

        screen.fill((255, 255, 255))

        new_game = True if choise == "Y" else False
        game = False if choise == "N" else True
            
    
    clock.tick(FPS)