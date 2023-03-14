import pygame
import random
import math
def main():

    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 580
    pygame.init()
    size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Game")
    WHITE = (255, 255, 255)
    RED =  (255, 0, 0)
    screen.fill(WHITE)
    pygame.display.flip()
    IMAGE = 'imagepuma.jpg'
    img = pygame.image.load(IMAGE)
    screen.blit(img, (0, 0))
    pygame.display.flip()
    X_start_pos = 550
    Y_start_pos = 290
    X_Y_start_pos = [X_start_pos, Y_start_pos]
    logtidute = 350
    width = 1
    i=0
    X_end_pos = X_start_pos + logtidute*math.cos(i*math.pi/50)
    Y_end_pos = Y_start_pos + logtidute*math.sin(i*math.pi/50)
    X_Y_end_pos = [X_end_pos,Y_end_pos]
    pygame.draw.line(screen, RED, X_Y_start_pos, X_Y_end_pos, width)

    pygame.draw.circle(screen,WHITE,X_Y_start_pos,400,1)

    pygame.display.flip()

    finish = False
    clock = pygame.time.Clock()
    REFRESH_RATE = 60

    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

        screen.blit(img, (0, 0))

        X_Y_end_pos = [X_end_pos+i, Y_end_pos+i]
        pygame.draw.line(screen, RED, X_Y_start_pos, X_Y_end_pos, width)
        pygame.display.flip()
        i+=random.randint(0,10)
        clock.tick(REFRESH_RATE)

    pygame.quit()

if __name__ == '__main__':
    main()
