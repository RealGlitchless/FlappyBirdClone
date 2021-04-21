import pygame
import sys
import os
import random
import ctypes

pygame.init()
white = (255, 255, 255)

# Get window width and height and set to window size
size = width, height = 350, 512

# Set windows size
screen = pygame.display.set_mode(size)
# Get root
root = os.path.dirname(sys.modules['__main__'].__file__)
# Set title
pygame.display.set_caption('Flappy bird')
# Get Clock
clock = pygame.time.Clock()
# Get assets in folder
assets = root + "\\Assets\\"

scrollSpeed = 80
highScore = 0


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


isRunning = True
while isRunning:

    bird = pygame.image.load(assets + "bird.png")
    # Bird starting pos
    bird_x = 40
    bird_y = 220

    # Open pipe image and load it
    pipe = pygame.image.load(assets + "pipe.png")
    # Pipe starting pos
    pipeStaring = 350
    pipeGap_y = 430
    # Gap between pipes
    pipeGap_x = 170

    # open image, set pos and set rect
    pipe1 = pipe
    pipe1rect = pipe1.get_rect()
    pipe1_y = random.randint(192, 320)
    pipe1_2 = pipe
    # Rotate pipe 180 degrees
    pipe1_2 = pygame.transform.rotate(pipe1_2, 180)
    pipe1_2_y = pipe1_y - pipeGap_y
    pipe1_x = pipeStaring

    # open image, set pos and set rect
    pipe2 = pipe
    pipe2_y = random.randint(192, 320)
    pipe2_2 = pipe
    # Rotate pipe 180 degrees
    pipe2_2 = pygame.transform.rotate(pipe2_2, 180)
    pipe2_2_y = pipe2_y - pipeGap_y
    pipe2_x = pipe1_x + pipeGap_x

    # open image, set pos and set rect
    pipe3 = pipe
    pipe3_y = random.randint(192, 320)
    pipe3_2 = pipe
    #  Rotate pipe 180 degrees
    pipe3_2 = pygame.transform.rotate(pipe3_2, 180)
    pipe3_2_y = pipe3_y - pipeGap_y
    pipe3_x = pipe2_x + pipeGap_x

    # open image, set pos and set rect
    base = pygame.image.load(assets + "base.png")
    baserect = base.get_rect()
    base_x = 0
    base_x2 = base.get_width()

    # open image, set pos and set rect
    gameover = pygame.image.load(assets + "gameover.png")
    gameoverRect = gameover.get_rect()

    # Create point system
    point1Width = pipe.get_width()
    point1Height = pipe1_y - pipe1_2_y
    point1 = pygame.Surface((point1Width, point1Height))
    point1.set_alpha(128)
    point1.fill(white)
    point1Rect = point1.get_rect()

    point2Width = pipe.get_width()
    point2Height = pipe2_y - pipe2_2_y
    point2 = pygame.Surface((point2Width, point2Height))
    point2.set_alpha(128)
    point2.fill(white)
    point2Rect = point2.get_rect()

    point3Width = pipe.get_width()
    point3Height = pipe3_y - pipe3_2_y
    point3 = pygame.Surface((point3Width, point3Height))
    point3.set_alpha(128)
    point3.fill(white)
    point3Rect = point3.get_rect()

    # open image, set pos and set rect
    background = pygame.image.load(assets + "background.png")
    bgrect = background.get_rect()
    bg_x = 0
    bg_x2 = background.get_width()

    score = 0

    gameRunning = True
    while gameRunning:
        clock.tick(scrollSpeed)  # framerate

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.blit(background, (bg_x, 0))  # draws our first background image
        screen.blit(background, (bg_x2, 0))  # draws the second background image
        screen.blit(bird, (bird_x, bird_y))  # draw bird
        screen.blit(pipe1, (pipe1_x, pipe1_y))  # draws our first pipe on bottom
        screen.blit(pipe1_2, (pipe1_x, pipe1_2_y))  # draws the first pipe on top
        screen.blit(pipe2, (pipe2_x, pipe2_y))  # draws our second pipe on bottom
        screen.blit(pipe2_2, (pipe2_x, pipe2_2_y))  # draws the second pipe on top
        screen.blit(pipe3, (pipe3_x, pipe3_y))  # draws our third pipe on bottom
        screen.blit(pipe3_2, (pipe3_x, pipe3_2_y))  # draws the third pipe on top
        screen.blit(base, (base_x, 450))  # draws first base
        screen.blit(base, (base_x2, 450))  # draws the second base

        # Get new rect of bird and move it to image pos
        birdRect = bird.get_rect()
        birdRect = birdRect.move(bird_x, bird_y)

        # Get new rect of both first pipe and move it to image pos
        pipe1rect = pipe1.get_rect()
        pipe1rect = pipe1rect.move(pipe1_x, pipe1_y)
        pipe1_2rect = pipe1_2.get_rect()
        pipe1_2rect = pipe1_2rect.move(pipe1_x, pipe1_2_y)

        # Get new rect of both second pipe and move it to image pos
        pipe2rect = pipe2.get_rect()
        pipe2rect = pipe2rect.move(pipe2_x, pipe2_y)
        pipe2_2rect = pipe2_2.get_rect()
        pipe2_2rect = pipe2_2rect.move(pipe2_x, pipe2_2_y)

        # Get new rect of both first pipe and move it to image pos
        pipe3rect = pipe3.get_rect()
        pipe3rect = pipe3rect.move(pipe3_x, pipe3_y)
        pipe3_2rect = pipe3_2.get_rect()
        pipe3_2rect = pipe3_2rect.move(pipe3_x, pipe3_2_y)

        # Get new rect of both bases and move it to image pos
        baserect = base.get_rect()
        baserect = baserect.move(base_x, 450)
        base1rect = base.get_rect()
        base1rect = base1rect.move(base_x2, 450)

        # Render and center score
        font = pygame.font.SysFont(None, 48)
        scoreText = font.render(f'{score}', True, white)
        textRect = scoreText.get_rect()
        textRect.center = (width // 2, height // 7)
        screen.blit(scoreText, textRect)  # draws score

        pygame.display.update()  # updates the screen

        bg_x -= 1.4  # Move both background images back
        bg_x2 -= 1.4

        base_x -= 1  # Move both bases back
        base_x2 -= 1

        pipe1_x -= 1  # Move both first pipes back
        pipe2_x -= 1  # Move both second pipes back
        pipe3_x -= 1  # Move both third pipes back

        bird_y += 3  # Moves bird down

        # Get key pressed
        playerKey = pygame.key.get_pressed()
        # If space is pressed bird moves up
        if playerKey[pygame.K_SPACE]:
            if not birdRect.top < 0:
                bird_y -= 8

        # If background is at the -width then reset its position
        if bg_x < background.get_width() * -1:
            bg_x = background.get_width()

        if bg_x2 < background.get_width() * -1:
            bg_x2 = background.get_width()

        # If base is at the -width then reset its position
        if base_x < base.get_width() * -1:
            base_x = base.get_width()

        if base_x2 < base.get_width() * -1:
            base_x2 = base.get_width()

        # If first pipe is at the -width then reset its position with new Y
        if pipe1_x < pipe1rect.width - 120:
            pipe1_x = pipe3_x + pipeGap_x
            pipe1_y = random.randint(192, 400)
            pipe1_2_y = pipe1_y - pipeGap_y

        # If second pipe is at the -width then reset its position with new Y
        if pipe2_x < pipe2rect.width - 120:
            pipe2_x = pipe1_x + pipeGap_x
            pipe2_y = random.randint(192, 400)
            pipe2_2_y = pipe2_y - pipeGap_y

        # If third pipe is at the -width then reset its position with new Y
        if pipe3_x < pipe3rect.width - 120:
            pipe3_x = pipe2_x + pipeGap_x
            pipe3_y = random.randint(192, 400)
            pipe3_2_y = pipe3_y - pipeGap_y

        # Collision detection
        # Detect if bird and point collied and give +1 point
        if pygame.Rect.colliderect(birdRect, point1Rect) and pipe1_x == bird_x:
            score += 1

        if pygame.Rect.colliderect(birdRect, point2Rect) and pipe2_x == bird_x:
            score += 1

        if pygame.Rect.colliderect(birdRect, point3Rect) and pipe3_x == bird_x:
            score += 1

        # Detect if bird hits base or pipes. If bird does, end game
        if pygame.Rect.colliderect(birdRect, pipe1rect):
            gameRunning = False

        if pygame.Rect.colliderect(birdRect, pipe1_2rect):
            gameRunning = False

        if pygame.Rect.colliderect(birdRect, pipe2rect):
            gameRunning = False

        if pygame.Rect.colliderect(birdRect, pipe2_2rect):
            gameRunning = False

        if pygame.Rect.colliderect(birdRect, pipe3rect):
            gameRunning = False

        if pygame.Rect.colliderect(birdRect, pipe3_2rect):
            gameRunning = False

        if pygame.Rect.colliderect(birdRect, baserect):
            gameRunning = False

    # Display gameover and popup with score
    screen.blit(gameover, (width / 4, height / 5))
    pygame.display.update()
    if score > highScore:
        highScore = score

    choice = Mbox('Game Over',
                  f'You scored {score}\n'
                  f'Your current highscore is {highScore}\n'
                  'Do you want to play again?', 4)

    YES = 6
    NO = 7
    if choice == YES:
        continue

    if choice == NO:
        isRunning = False
