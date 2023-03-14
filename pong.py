import pygame
import random
def main():


    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 580
    RED =  (255, 0, 0)
    IMAGE = 'imagepuma.jpg'
    X_Y_pos = [100,100]
    GREEN_SPRITE = (0, 199, 10)
    LEFT = 1
    SCROLL = 2
    RIGHT = 3

    clock = pygame.time.Clock()
    REFRESH_RATE = 60


    size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    pygame.init()
    pygame.mouse.set_visible(False)
    pygame.display.set_caption("Pong game!!!")
    screen = pygame.display.set_mode(size)
    img = pygame.image.load(IMAGE)
    screen.blit(img, (0, 0))
    pygame.display.flip()
    direction_x = 1
    direction_y = 1
    finish = False

    mouse_pos_list = []
    a= 0
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            elif event.type == pygame.MOUSEBUTTONDOWN \
                and event.button == LEFT:
                mouse_pos_list.append(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    a+=1


        screen.blit(img, (0, 0))
        pygame.draw.circle(screen, RED, X_Y_pos, 10)
        if a ==3:
            pygame.draw.circle(screen, RED, pygame.mouse.get_pos(), 100)
        mouse_point = pygame.mouse.get_pos()

        player_image = pygame.image.load('parrot_sprite.png').convert()
        player_image.set_colorkey(GREEN_SPRITE)
        screen.blit(player_image, mouse_point)
        for position in mouse_pos_list:
            screen.blit(player_image, position)
        pygame.display.flip()

        X_Y_pos[0] += direction_x
        X_Y_pos[1] += direction_y
        if X_Y_pos[0]==0:
            direction_x = direction_x*-1
        if X_Y_pos[1] == 0:
            direction_y = direction_y * -1
        if X_Y_pos[0] == 1279:
            direction_x = direction_x * -1
        if X_Y_pos[1] == 579:
            direction_y = direction_y * -1



        clock.tick(REFRESH_RATE)


    pygame.quit()

if __name__ == '__main__':
    main()