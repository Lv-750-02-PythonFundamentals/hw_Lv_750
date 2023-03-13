import pygame

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GRAY_COLOR = (125, 125, 125)
LIGHT_BLUE_COLOR = (64, 128, 255)
GREEN_COLOR = (0, 200, 64)
YELLOW_COLOR = (225, 225, 0)
PINK_COLOR = (230, 50, 230)



pygame.init()
WIDTH_DISPLAY = 800
HEIGHT_DISPLAY = 600
gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))

pygame.display.set_caption('My first game')

COLOR = [0, 0, 0]  # RGB
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
gameDisplay.fill(tuple(COLOR))

circle = False
circle_x = 100
circle_y = 100
circle_r = 50
DELTA_STEP = 5
# -------- Main Program Loop -----------
while not done:

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            circle = not circle

            print("User pressed a mouse button")
    # --- Game logic should go here
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    if COLOR[0] >= 255:
        if COLOR[1] >= 255:
            if COLOR[2] >= 255:
                COLOR = [0, 0, 0]
            else:
                COLOR[2] += 1
        else:
            COLOR[1] += 1
    else:
        COLOR[0] += 1
    gameDisplay.fill(tuple(COLOR))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if circle_x > circle_r:
            circle_x = circle_x - DELTA_STEP
    if keys[pygame.K_RIGHT]:
        if circle_x < WIDTH_DISPLAY - circle_r:
            circle_x = circle_x + DELTA_STEP
    if keys[pygame.K_UP]:
        if circle_y > circle_r:
            circle_y = circle_y - DELTA_STEP
    if keys[pygame.K_DOWN]:
        if circle_y < HEIGHT_DISPLAY - circle_r:
            circle_y = circle_y + DELTA_STEP

    if circle:
        pygame.draw.circle(gameDisplay, YELLOW_COLOR, (circle_x, circle_y), circle_r, 5)
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("My text", True, GRAY_COLOR)
    gameDisplay.blit(text, [200, 100])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()
    # --- Limit to 60 frames per second
    clock.tick(60)
