import pygame
import random

PINK = (255, 20, 147)
MOVING_IMAGE = 'baseball.png'
HORIZONTAL_VELOCITY = 3
VERTICAL_VELOCITY = 5
NUMBER_OF_BALLS = 5
DISTANCE = 100
LEFT = 1
IMAGE = 'imagepuma.jpg'
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 1000
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
MAX_VELOCITY = 30


class Ball(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Ball,self).__init__()
        self.image = pygame.image.load(MOVING_IMAGE).convert()
        self.image.set_colorkey(PINK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.__vx = HORIZONTAL_VELOCITY
        self.__vy = VERTICAL_VELOCITY

    def update_v(self, vx, vy):
        self.__vx = vx
        self.__vy = vy

    def update_loc(self):
        self.rect.x += self.__vx
        self.rect.y += self.__vy

    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_v(self):
        return self.__vx, self.__vy

def main():

    clock = pygame.time.Clock()
    REFRESH_RATE = 60
    screen = pygame.display.set_mode(size)

    img = pygame.image.load(IMAGE)
    screen.blit(img, (0, 0))

    pygame.init()
    pygame.display.set_caption("Game")
    ball1 = Ball(100, 100)
    ball2 = Ball(200, 200)
    screen.blit(ball1.image, ball1.get_pos())
    screen.blit(ball2.image, ball2.get_pos())
    ball1.update_v(10,50)


    finish = False
    while not finish:
        balls_list = pygame.sprite.Group()
        """for i in range(NUMBER_OF_BALLS):
            ball = Ball(i * DISTANCE, i * DISTANCE)
            balls_list.add(ball)
        balls_list.draw(screen)"""
        clock.tick(REFRESH_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            elif event  .type == pygame.MOUSEBUTTONDOWN \
                    and event.button == LEFT:
                x, y = pygame.mouse.get_pos()
                ball = Ball(x, y)
                vx = random.randint(-MAX_VELOCITY, MAX_VELOCITY)
                vy = random.randint(-MAX_VELOCITY, MAX_VELOCITY)
                ball.update_v(vx, vy)
                balls_list.add(ball)
                for ball in balls_list:
                    ball.update_loc()
         # update screen with balls
        balls_list.draw(screen)



        pygame.display.flip()
        clock.tick(REFRESH_RATE)






    pygame.quit()

if __name__ == '__main__':
    main()
