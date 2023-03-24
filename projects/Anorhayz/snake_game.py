import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

BLOCK_SIZE = 50
FONT = pygame.font.SysFont("roboto-font.ttf", BLOCK_SIZE * 2)

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()


class Snake:
    def __init__(self):
        self.x = BLOCK_SIZE
        self.y = BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    def update_position(self):
        global food

        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0, SCREEN_WIDTH) or self.head.y not in range(0, SCREEN_HEIGHT):
                self.dead = True

        if self.dead:
            self.x = BLOCK_SIZE
            self.y = BLOCK_SIZE
            self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
            self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
            self.xdir = 1
            self.ydir = 0
            self.dead = False
            food = Food()

        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)


class Food:
    def __init__(self):
        self.x = int(random.randint(0, SCREEN_WIDTH) / BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, SCREEN_HEIGHT) / BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def update_pos(self):
        pygame.draw.rect(screen, "red", self.rect)


def draw_grid():
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#2E2E2E", rect, 1)


draw_grid()

score = FONT.render("1", True, "white")
score_rect = score.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 20))

snake = Snake()
food = Food()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.ydir = 1
                snake.xdir = 0
            elif event.key == pygame.K_UP:
                snake.ydir = -1
                snake.xdir = 0
            elif event.key == pygame.K_RIGHT:
                snake.ydir = 0
                snake.xdir = 1
            elif event.key == pygame.K_LEFT:
                snake.ydir = 0
                snake.xdir = -1

    snake.update_position()

    screen.fill("black")
    draw_grid()

    food.update_pos()

    score = FONT.render(f"{len(snake.body)}", True, "white")

    pygame.draw.rect(screen, "yellow", snake.head)

    for square in snake.body:
        pygame.draw.rect(screen, "green", square)

    screen.blit(score, score_rect)

    if snake.head.x == food.x and snake.head.y == food.y:
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        food = Food()

    pygame.display.update()
    clock.tick(10)
