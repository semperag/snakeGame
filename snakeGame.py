import pygame
from random import randrange
import sys
import time

# initializing the constructor
pygame.init()

# screen resolution
res = (505, 505)

# opens up a window
window = pygame.display.set_mode(res)

# white color
color = (255, 255, 255)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

# stores the width of the
# screen into a variable
width = window.get_width()

# stores the height of the
# screen into a variable
height = window.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in
# this font
quitText = smallfont.render('quit', True, color)
startText = smallfont.render('start', True, color)
snakeTitle = smallfont.render('Snake Game', True, color)


def playGame():
    #pygame.init()

    #window = pygame.display.set_mode((505, 505))

    pygame.display.set_caption('Snake Game')

    eatSound = pygame.mixer.Sound('Game./Crunch.wav')
    loseSound = pygame.mixer.Sound('Game./HitWall.wav')
    moveSound = pygame.mixer.Sound('Game./ChangeDirection.wav')

    clock = pygame.time.Clock()

    def drawLines():
        for line in range(0, 19):
            pygame.draw.line(window, (255, 255, 255), (line * 28, 0), (line * 28, 504), 1)
            pygame.draw.line(window, (255, 255, 255), (0, line * 28), (504, line * 28), 1)

    pygame.display.update()

    class snake(object):
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.head = (self.x, self.y, self.width, self.height)
            self.vel = 28
            self.facingRight = False
            self.facingLeft = False
            self.facingDown = True
            self.facingUp = False
            self.hasEaten = False
            self.length = 1
            self.body = [(self.x, self.y)]

        def draw(self, window, snakeBody):
            for block in snakeBody:
                pygame.draw.rect(window, (255, 0, 0), (block[0], block[1], self.width, self.height))

            pygame.draw.circle(window, (0, 0, 0), (self.x + 14, self.y + 6), 3, 3)
            pygame.display.update()

        def eat(self):
            self.length += 1

    def redrawGameWindow(snakeBody):
        window.fill((0, 0, 0))
        drawLines()
        snake.draw(window, snakeBody)
        pygame.draw.rect(window, (0, 0, 255), (random[0], random[1], 27, 27))
        pygame.display.update()

    random = [int(randrange(0, 18) * 28 + 1), int(randrange(0, 18) * 28 + 1)]

    # MainLoop
    snake = snake(85, 85, 27, 27)
    snakeBody = []
    run = True
    end = False

    while run:
        clock.tick(6)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN] and snake.y < 504 - snake.vel and not snake.facingUp and not snake.facingDown:
            moveSound.play()
            snake.facingDown = True
            snake.facingRight = False
            snake.facingLeft = False
            snake.facingUp = False
        elif keys[pygame.K_UP] and snake.y > snake.vel and not snake.facingDown and not snake.facingUp:
            moveSound.play()
            snake.facingUp = True
            snake.facingRight = False
            snake.facingLeft = False
            snake.facingDown = False
        elif keys[pygame.K_RIGHT] and snake.x < 504 - snake.vel and not snake.facingLeft and not snake.facingRight:
            moveSound.play()
            snake.facingRight = True
            snake.facingLeft = False
            snake.facingDown = False
            snake.facingUp = False
        elif keys[pygame.K_LEFT] and snake.x > snake.vel and not snake.facingRight and not snake.facingLeft:
            moveSound.play()
            snake.facingLeft = True
            snake.facingRight = False
            snake.facingDown = False
            snake.facingUp = False

        if snake.facingDown:
            snake.y += snake.vel
        elif snake.facingUp:
            snake.y -= snake.vel
        elif snake.facingRight:
            snake.x += snake.vel
        elif snake.facingLeft:
            snake.x -= snake.vel

        snakeHead = [int(snake.x), int(snake.y)]
        snakeBody.append(snakeHead)

        if len(snakeBody) > snake.length:
            del snakeBody[0]

        for x in snakeBody[:-1]:
            if x == snakeHead:
                loseSound.play()
                end = True
                time.sleep(1)
                return
                while end:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            end = False
                            run = False

        if snake.x >= 504 or snake.x <= 0 or snake.y >= 504 or snake.y <= 0:
            loseSound.play()
            end = True
            time.sleep(1)
            return
            while end:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        end = False
                        run = False
        else:
            while random[0] == snake.x and random[1] == snake.y:
                random = [int(randrange(0, 18) * 28 + 1), int(randrange(0, 18) * 28 + 1)]

                if not snake.hasEaten:
                    eatSound.play()
                    snake.eat()
                    snake.hasEaten = True

                changePos = True
                while changePos:
                    changePos = False
                    for block in snakeBody:
                        if block[0] == random[0] and block[1] == random[1]:
                            random = [int(randrange(0, 18) * 28 + 1), int(randrange(0, 18) * 28 + 1)]
                            changePos = True

            snake.hasEaten = False

        if run:
            redrawGameWindow(snakeBody)

    pygame.quit()


while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

            # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN and width / 2 - 50 <= mouse[0] <= width / 2 + 90 and height / 2 + 50 <= mouse[1] <= height / 2 + 90:

            # if the mouse is clicked on the
            # button the game is terminated
            if width / 2 - 50 <= mouse[0] <= width / 2 + 90 and height / 2 + 50 <= mouse[1] <= height / 2 + 90:
                pygame.quit()

        if ev.type == pygame.MOUSEBUTTONDOWN and width / 2 - 50 <= mouse[0] <= width / 2 + 90 and height / 2 - 50 <= mouse[1] <= height / 2 - 10:

            # if the mouse is clicked on the
            # button the game is terminated
            if width / 2 - 50 <= mouse[0] <= width / 2 + 90 and height / 2 - 50 <= mouse[1] <= height / 2 - 10:
                playGame()

                # fills the screen with a color
    window.fill((5, 5, 5))

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if width / 2 - 50 <= mouse[0] <= width / 2 + 90 and height / 2 + 50 <= mouse[1] <= height / 2 + 90:
        pygame.draw.rect(window, color_light, [int(width / 2) - 50, int(height / 2) + 50, 140, 40])
        pygame.draw.rect(window, color_dark, [int(width / 2) - 50, int(height / 2) - 50, 140, 40])

    elif width / 2 - 50 <= mouse[0] <= width / 2 + 90 and height / 2 - 50 <= mouse[1] <= height / 2 - 10:
        pygame.draw.rect(window, color_dark, [int(width / 2) - 50, int(height / 2) + 50, 140, 40])
        pygame.draw.rect(window, color_light, [int(width / 2) - 50, int(height / 2) - 50, 140, 40])

    else :
        pygame.draw.rect(window, color_dark, [int(width / 2) - 50, int(height / 2) + 50, 140, 40])
        pygame.draw.rect(window, color_dark, [int(width / 2) - 50, int(height / 2) - 50, 140, 40])

        # superimposing the text onto our button
    window.blit(quitText, (int(width / 2), int(height / 2) + 50))
    window.blit(startText, (int(width / 2), int(height / 2) - 50))
    window.blit(snakeTitle, (int(width / 2) - 75, int(height / 2) - 150))

    # updates the frames of the game
    pygame.display.update()
