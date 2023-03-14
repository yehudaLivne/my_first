import pygame

def main():

    pygame.init()
    clock = pygame.time.Clock()
    REFRESH_RATE = 60
    IMAGE = 'imagepuma.jpg'

    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    window_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    SCREEN_COLOR_GRAY =  (130, 130, 130)

    GREEN_SPRITE = (0, 199, 10)

    SOUND_FILE = "kaboom.mp3"
    pygame.mixer.init()



    pygame.display.set_caption("catch the ball!!;-)")
    screen = pygame.display.set_mode(window_size)
    screen.fill(SCREEN_COLOR_GRAY)
    img = pygame.image.load(IMAGE)
    screen.blit(img, (0, 0))

    pygame.display.flip()

    pygame.mouse.set_visible(False)
    LEFT_MOUSE_BUTTON = 1
    SCROLL_MOUSE_BUTTON = 2
    RIGHT_MOUSE_BUTTON = 3
    mouse_pos_list = []
    key_switch = -1


    x_position,y_position = 0,0
    pos = [x_position, y_position]

    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == LEFT_MOUSE_BUTTON:
                    mouse_pos_list.append(pygame.mouse.get_pos())
                elif event.button == RIGHT_MOUSE_BUTTON:
                    pygame.mixer.music.load(SOUND_FILE)
                    pygame.mixer.music.play()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_position -= 10
                elif event.key == pygame.K_d:
                    x_position += 10
                elif event.key == pygame.K_w:
                    y_position -= 10
                elif event.key == pygame.K_x:
                    y_position += 10
                elif event.key == pygame.K_q:
                    key_switch = key_switch * -1
                elif event.key == pygame.K_SPACE:
                    mouse_pos_list = []
        screen.blit(img, (0, 0))

        player_image = pygame.image.load('parrot_sprite.png').convert()
        player_image.set_colorkey(GREEN_SPRITE)

        for position in mouse_pos_list:
            screen.blit(player_image, position)


        if pos[0]<0:
            pos[0] = 0
        if pos[1] < 0:
            pos[1] = 0
        if pos[0] > 599:
            pos[0] = 599
        if pos[1] > 599:
            pos[1] = 599

        pos = [x_position, y_position]
        mouse_point = pygame.mouse.get_pos()
        if (key_switch == 1):
            pos = mouse_point
        screen.blit(player_image, pos)
        pygame.display.flip()

        clock.tick(REFRESH_RATE)


    pygame.quit()

if __name__ == '__main__':
    main()