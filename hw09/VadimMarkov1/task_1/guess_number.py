import pygame
import random


WIDTH = 600
HEIGHT = 600


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Number")
icon = pygame.image.load("icon.png")
trident = pygame.image.load("trident.png")
trident_x = 0
trident_y = 485
speed = 2
pygame.display.set_icon(icon)
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.2)


number = random.randint(1, 100)
attempts_left = 10
input_text = ""
result_text = ""
ability_input = True


def reset_game():
    global number, attempts_left, result_text, ability_input, input_text
    number = random.randint(1, 100)
    attempts_left = 10
    result_text = ""
    input_text = ""
    ability_input = True


def run_game():
    print_text("Guess a number from 1 to 100 in 10 tries", 35, 25, 25)
    game = True
    pygame.mixer.music.play(-1)
    while game:
        screen.fill((255, 237, 155))
        print_text("Guess a number from 1 to 100 in 10 tries", 35, 25, 25)
        print_text(f"Attempts left: {attempts_left}", 30, 25, 80)
        print_text("Enter the number:", 30, 25, 150)
        get_input()
        print_text(result_text, 30, 25, 300)
        click_button()
        pygame.draw.rect(screen, (210, 218, 255), (238, 400, 125, 55))
        print_text("Try again", 30, 248, 410)
        draw_trident()
        pygame.display.update()


def print_text(message, font_size, x_coord, y_coord):
    font = pygame.font.SysFont('arial', font_size)
    text = font.render(message, True, (65, 40, 255))
    screen.blit(text, (x_coord, y_coord))


def get_input():
    global input_text, ability_input
    input_rect = pygame.Rect(250, 130, 170, 85)
    pygame.draw.rect(screen, (210, 218, 255), input_rect)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and ability_input:
            if event.key == pygame.K_RETURN:
                check_input()
                input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                if len(input_text) < 3:
                    input_text += event.unicode
        elif event.type == pygame.QUIT:
            pygame.quit()
            quit()
    print_text(input_text, 35, input_rect.x + 65, input_rect.y + 20)


def check_input():
    global result_text, attempts_left, input_text, ability_input
    if not input_text.isdigit() or int(input_text) not in range(1, 101):
        result_text = "Please enter a number from 1 to 100."
    else:
        guess = int(input_text)
        if guess == number:
            result_text = f"Congratulations, you guessed the number - {number}!"
            ability_input = False
        elif guess < number:
            result_text = f"The number is greater than {guess}"
            attempts_left -= 1
        elif guess > number:
            result_text = f"The number is less than {guess}"
            attempts_left -= 1
        if attempts_left < 1:
            result_text = f"Sorry you didn't guess the number - {number}"
            ability_input = False
            print(ability_input)


def click_button():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 238 < mouse[0] < 363 and 400 < mouse[1] < 455 and click[0] == 1:
        reset_game()


def draw_trident():
    global trident_x, trident_y, speed
    if trident_x > 528 or trident_x < 0:
        speed = -speed
    screen.blit(trident, (trident_x, trident_y))
    trident_x += speed


if __name__ == '__main__':
    run_game()
